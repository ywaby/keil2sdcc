# Copyright (c) 2017 ywaby@163.com
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
# python src/c512sdcc
import os


class C512SDCC():
    """
    unsporrt bdata
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
    __keil_memory_types = ["code", "data", "idata", "pdata", "xdata", "bdata", "far"]
    __keil_register_types = ["sfr", "sfr16", "sbit"]

    def __init__(self, keil_srcs=[], encode="utf8"):
        self.__encode = encode
        self.__mulit_start = False
        self.__register_map = {}
        if len(keil_srcs) != 0:
            self.keil_srcs = keil_srcs
            self.convert_all()

    def convert_all(self):
        for keil_src in self.keil_srcs:
            self.convert_file(keil_src)

    def convert_file(self, keil_src):
        if not os.path.exists(keil_src):
            raise Exception(f"keil_src not exist: {keil_src}")
        base, ext = os.path.splitext(keil_src)
        sdcc_src = base + ".sdcc.c"
        f_keil = open(keil_src, "r", encoding=self.__encode)
        f_sdcc = open(sdcc_src, "w", encoding="utf8")
        for line in f_keil.readlines():
            sdcc_line = self.__convert_line(line)
            f_sdcc.write(sdcc_line)
        f_keil.close()
        f_sdcc.close()
        print(f"{keil_src} --> {sdcc_src}")

    def __get_words(self, statements):
        statements.replace("=", " = ")
        words = statements.split(" ")
        while "" in words:
            words.remove("")
        return words

    def __parse_line(self, c_line):
        c_line = c_line.expandtabs(4)
        if self.__mulit_start is True:
            if c_line.find("*/") != -1:
                self.__mulit_start = False
            return 0, None, "", c_line
        indent = len(c_line) - len(c_line.lstrip(" "))
        if c_line.find("/*") != -1:
            statements_line, comments = c_line.split("/*")
            comments = "/*" + comments
            self.__mulit_start = True
            if comments.find("*/"):
                self.__mulit_start = False
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
        statements_words = [self.__get_words(statements)
                            for statements in statements]
        return indent, statements_words, statements_line_end, comments

    def __convert_line(self, c51_line):
        indent, statements_words, statements_line_end, comments = self.__parse_line(c51_line)
        # keil 2 sdcc
        if not statements_words:
            if comments is not None:
                sdcc_line = comments
            else:
                sdcc_line = "\n"
            sdcc_line = f"{' '*indent}{sdcc_line}"
            return sdcc_line
        for idx, statements in enumerate(statements_words):
            # translate memory at
            # char xdata text[256]   _at_ 0xE000;
            if "_at_" in statements:
                addr = statements[-1]
                for word in statements:
                    if word in C512SDCC.__keil_memory_types:
                        statements.remove(word)
                        statements.remove(addr)
                        statements.remove("_at_")
                        statements = [word, "__at", f"({addr})"] + statements
                        break
                else:
                    raise Exception(f"unsupport keil memory types")

            # translate register_type
            # sfr name = address;
            if statements[0] in C512SDCC.__keil_register_types:
                register_type, name = statements[0:2]
                addr = "".join(statements[3:])
                self.__register_map[name] = addr
                if register_type == "sbit" and "^" in addr:
                    base_addr, sub_addr = addr.split("^", 1)
                    if base_addr in self.__register_map:
                        base_addr = self.__register_map[base_addr]
                    addr = f"{base_addr}+{sub_addr}"
                statements = [register_type, "__at", f"({addr})", name]

                # traslate keyword
            for word in statements:
                if word in C512SDCC.__keil2sdcc_dict:
                    statements[statements.index(
                        word)] = C512SDCC.__keil2sdcc_dict[word]
            statements_words[idx] = statements  # update
        statements_line = ";".join([" ".join(statements) for statements in statements_words]) + statements_line_end
        if comments is not None:
            sdcc_line = statements_line + f"{comments}"
        else:
            sdcc_line = statements_line + "\n"
        sdcc_line = f"{' '*indent}{sdcc_line}"
        return sdcc_line
