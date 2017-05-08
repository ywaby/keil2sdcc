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
    keil2sdcc_dict = {
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
    keil_memory_types = ["code", "data", "idata",
                         "pdata", "xdata", "bdata", "far"]
    keil_register_types = ["sfr", "sfr16", "sbit"]
    register_map = {}

    def __init__(self, keil_file):
        self.src_encode = "utf8"
        self.keil_file = keil_file
        self.mulit_start = False
        base, ext = os.path.splitext(keil_file)
        self.sdcc_file = base + ".sdcc.c"
        self.convert_file()
        print(f"{keil_file} --> {self.sdcc_file}")

    def convert_file(self):
        if not os.path.exists(self.keil_file):
            raise Exception(f"keil_file not exist: {self.keil_file}")
        f_keil = open(self.keil_file, "r", encoding=self.src_encode)
        f_sdcc = open(self.sdcc_file, "w", encoding="utf8")
        for line in f_keil.readlines():
            sdcc_line = self.convert_line(line)
            f_sdcc.write(sdcc_line)
        f_keil.close()
        f_sdcc.close()

    def get_words(self, statements):
        statements.replace("=", " = ")
        words = statements.split(" ")
        while "" in words:
            words.remove("")
        return words

    def parse_line(self, c_line):
        c_line = c_line.expandtabs(4)
        if self.mulit_start is True:
            if c_line.find("*/") != -1:
                self.mulit_start = False
            return 0, None, "", c_line
        indent = len(c_line) - len(c_line.lstrip(" "))
        if c_line.find("/*") != -1:
            statements_line, comments = c_line.split("/*")
            comments = "/*" + comments
            self.mulit_start = True
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
        statements_words = [self.get_words(statements)
                            for statements in statements]
        return indent, statements_words, statements_line_end, comments

    def convert_line(self, c51_line):
        indent, statements_words, statements_line_end, comments = self.parse_line(c51_line)
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
                    if word in C512SDCC.keil_memory_types:
                        statements.remove(word)
                        statements.remove(addr)
                        statements.remove("_at_")
                        statements = [word, "__at", f"({addr})"] + statements
                        break
                else:
                    raise Exception(f"unsupport keil memory types")

            # translate register_type
            # sfr name = address;
            if statements[0] in C512SDCC.keil_register_types:
                register_type, name = statements[0:2]
                addr = "".join(statements[3:])
                C512SDCC.register_map[name] = addr
                if register_type == "sbit" and "^" in addr:
                    base_addr, sub_addr = addr.split("^", 1)
                    if base_addr in C512SDCC.register_map:
                        base_addr = C512SDCC.register_map[base_addr]
                    addr = f"{base_addr}+{sub_addr}"
                statements = [register_type, "__at", f"({addr})", name]

                # traslate keyword
            for word in statements:
                if word in C512SDCC.keil2sdcc_dict:
                    statements[statements.index(
                        word)] = C512SDCC.keil2sdcc_dict[word]
            statements_words[idx] = statements  # update
        statements_line = ";".join([" ".join(statements) for statements in statements_words]) + statements_line_end
        if comments is not None:
            sdcc_line = statements_line + f"{comments}"
        else:
            sdcc_line = statements_line + "\n"
        sdcc_line = f"{' '*indent}{sdcc_line}"
        return sdcc_line

