import os


class C512SDCC():
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
    __keil_memory_types = ["code", "data",
                           "idata", "pdata", "xdata", "bdata", "far"]
    __keil_register_types = ["sfr", "sfr16", "sbit"]

    def __init__(self, keil_srcs=[str], encode="utf8"):
        self._encode = encode  # input files encode
        self._multi_line_comments_start = False  # multiline comment start
        self.cur_line_num = 0  # current line num
        self.cur_src = ""
        self._register_map = {}  # register name <=> addr
        if len(keil_srcs) != 0:
            self.keil_srcs = keil_srcs
            self.convert_all()

    def convert_all(self):
        for keil_src in self.keil_srcs:
            self.cur_src = keil_src
            self.cur_line_num = 0
            self.convert_file(keil_src)

    def convert_file(self, keil_src):
        if not os.path.exists(keil_src):
            raise Exception(f"keil_src not exist: {keil_src}")
        folder, ext = os.path.splitext(keil_src)
        sdcc_src = folder + ".sdcc.c"
        f_keil = open(keil_src, "r", encoding=self._encode)
        f_sdcc = open(sdcc_src, "w", encoding="utf8")
        for line in f_keil.readlines():
            self.cur_line_num += 1
            sdcc_line = self.__convert_line(line)
            f_sdcc.write(sdcc_line)
        f_keil.close()
        f_sdcc.close()
        print(f"{keil_src} --> {sdcc_src}")

    def __get_words(self, statements):
        statements = statements.replace("=", " = ")
        words = statements.split(" ")
        while "" in words:
            words.remove("")
        return words

    def __parse_line(self, c_line):
        # return indent, statements_words, statements_line_end, comments
        # statements_words =[statement_words]
        # example
        #   sfr PSW    = 0xD0;//comments
        # return (2,[["sfr","PSW","=","0xD0"]],"//comments")

        c_line = c_line.expandtabs(4)
        if self._multi_line_comments_start is True:
            if c_line.find("*/") != -1:
                self._multi_line_comments_start = False
            return 0, None, "", c_line
        indent = len(c_line) - len(c_line.lstrip(" "))
        if c_line.find("/*") != -1:
            statements_line, comments = c_line.split("/*")
            comments = "/*" + comments
            self._multi_line_comments_start = True
            if comments.find("*/")!= -1:
                self._multi_line_comments_start = False
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

    def __convert_line(self, c51_line):

        indent, statements_words, statements_line_end, comments = self.__parse_line(
            c51_line)
        # keil 2 sdcc
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
                    if word in C512SDCC.__keil_memory_types:
                        statement_words.remove(word)
                        statement_words.remove(addr)
                        statement_words.remove("_at_")
                        statement_words = [word, "__at",
                                           f"({addr})"] + statement_words
                        break
                else:
                    raise Exception(
                        f"{self.cur_src}({self.cur_line_num}): unsupport keil memory type")

            # translate register_type
            # sfr name = address;
            if statement_words[0] in C512SDCC.__keil_register_types:
                register_type, name = statement_words[0:2]
                addr = "".join(statement_words[3:])
                self._register_map[name] = addr
                if register_type == "sbit" and "^" in addr:
                    base_addr, sub_addr = addr.split("^", 1)
                    if base_addr in self._register_map:
                        base_addr = self._register_map[base_addr]
                    addr = f"{base_addr}+{sub_addr}"
                statement_words = [register_type, "__at", f"({addr})", name]

            # traslate keyword
            for word in statement_words:
                if word in C512SDCC.__keil2sdcc_dict:
                    statement_words[statement_words.index(
                        word)] = C512SDCC.__keil2sdcc_dict[word]
            statements_words[idx] = statement_words  # update
        statements_line = ";".join(
            [" ".join(statement_words) for statement_words in statements_words]) + statements_line_end
        if comments is not None:
            sdcc_line = statements_line + f"{comments}"
        else:
            sdcc_line = statements_line + "\n"
        sdcc_line = f"{' '*indent}{sdcc_line}"
        return sdcc_line
