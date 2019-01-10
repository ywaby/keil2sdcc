import os


class C51_2_SDCC():
    """
    unsupport bdata
    """
    __keil2sdcc_dict = {
        "_at_": "__at",
        "sbit": "__sbit",
        "sfr": "__sfr",
        "sfr16": "__sfr16",
        "data": "__data",
        "xdata": "__xdata",
        "idata": "__idata",
        "pdata": "__pdata",
        "code": "__code",
        "bit": "__bit",
        "far": "__far",
        "reentrant": "__reentrant",
        "using": "__using",
    }
    __c51_memory_types = ["code", "data",
                          "idata", "pdata", "xdata", "bdata", "far"]
    __c51_register_types = ["sfr", "sfr16", "sbit"]

    def __init__(self, src: str, dist: str, encode="utf8"):
        self.__encode = encode  # input files encode
        self.__multi_line_comments_start = False  # multiline comment start
        self.cur_line_num = 0  # current line num
        if not os.path.exists(src):
            raise Exception(f"c51_src not exist: {src}")
        dist_dir = os.path.dirname(dist)
        if not os.path.exists(dist_dir) and dist_dir != "":
            os.makedirs(dist_dir)
        self.c51_src = src
        self.sdcc_src = dist
        self.__register_map = {}  # register name <=> addr
        self.convert_file()

    def convert_file(self):
        sdcc_lines = ""
        f_c51 = open(self.c51_src, "r", encoding=self.__encode)
        for line in f_c51.readlines():
            self.cur_line_num += 1
            sdcc_lines += self.__convert_line(line)
        f_c51.close()

        f_sdcc = open(self.sdcc_src, "w", encoding="utf8")
        f_sdcc.write(sdcc_lines)
        f_sdcc.close()

        print(f"{self.c51_src} --> {self.sdcc_src}")

    def __get_words(self, statements: str)->list:
        """
        :param statements: "sfr PSW    = 0xD0"
        :returns: ["sfr","PSW","=","0xD0"]
        """
        statements = statements.replace("=", " = ")
        words = statements.split(" ")
        while "" in words:
            words.remove("")
        return words

    def __parse_line(self, c_line: str)-> tuple((int, tuple, bool, str)):
        """
        :returns: indent, statements_words, statements_line_end, comments
        statements_words =[statement_words]
        example
          sfr PSW    = 0xD0;//comments
        return (2,[["sfr","PSW","=","0xD0"]],"//comments")
        """
        c_line = c_line.expandtabs(4)
        if self.__multi_line_comments_start is True:
            if c_line.find("*/") != -1:
                self.__multi_line_comments_start = False
            return 0, None, "", c_line
        indent = len(c_line) - len(c_line.lstrip(" "))
        if c_line.find("/*") != -1:
            statements_line, comments = c_line.split("/*")
            comments = "/*" + comments
            self.__multi_line_comments_start = True
            if comments.find("*/") != -1:
                self.__multi_line_comments_start = False
        elif c_line.find("//") != -1:
            statements_line, comments = c_line.split("//")
            comments = "//" + comments
        else:
            statements_line, comments = c_line, None
        statements_line = statements_line.strip()
        if statements_line == "":
            return indent, None, "", comments

        if statements_line[-1] == ";":
            statements_line_end = ";"
            statements = statements_line[:-1].split(";")
        else:
            statements_line_end = ""
            statements = statements_line.split(";")
        statements_words = [self.__get_words(statement)
                            for statement in statements]
        return indent, statements_words, statements_line_end, comments

    def __convert_line(self, c51_line: str)->str:
        """
        :param c51_line: 
        :returns: sdcc line
        """
        indent, statements_words, statements_line_end, comments = self.__parse_line(
            c51_line)
        # c51 2 sdcc
        if not statements_words:
            if comments is not None:
                sdcc_line = comments
            else:
                sdcc_line = "\n"
            sdcc_line = f"{' '*indent}{sdcc_line}"
            return sdcc_line
        for idx, statement_words in enumerate(statements_words):
            # translate memory at
            # char xdata text[256] _at_ 0xE000;
            if "_at_" in statement_words:
                addr = statement_words[-1]
                for word in statement_words:
                    if word in C51_2_SDCC.__c51_memory_types:
                        statement_words.remove(word)
                        statement_words.remove(addr)
                        statement_words.remove("_at_")
                        statement_words = [word, "__at",
                                           f"({addr})"] + statement_words
                        break
                    else:
                        raise Exception(
                            f"{self.c51_src}({self.cur_line_num}): unsupport keil memory type")

            # translate register_type
            # sfr name = address;
            if statement_words[0] in C51_2_SDCC.__c51_register_types:
                register_type, name = statement_words[0:2]
                addr = "".join(statement_words[3:])
                self.__register_map[name] = addr
                if register_type == "sbit" and "^" in addr:
                    base_addr, sub_addr = addr.split("^", 1)
                    if base_addr in self.__register_map:
                        base_addr = self.__register_map[base_addr]
                    addr = f"{base_addr}+{sub_addr}"
                statement_words = [register_type, "__at", f"({addr})", name]

            # traslate keyword
            for word in statement_words:
                if word in C51_2_SDCC.__keil2sdcc_dict:
                    statement_words[statement_words.index(
                        word)] = C51_2_SDCC.__keil2sdcc_dict[word]
            statements_words[idx] = statement_words  # update
        statements_line = ";".join(
            [" ".join(statement_words) for statement_words in statements_words]) + statements_line_end
        if comments is not None:
            sdcc_line = statements_line + f"{comments}"
        else:
            sdcc_line = statements_line + "\n"
        sdcc_line = f"{' '*indent}{sdcc_line}"
        return sdcc_line
