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
    keil_memory_types = ["code", "data", "idata", "pdata", "xdata", "bdata", "far"]
    keil_register_types = ["sfr", "sfr16", "sbit"]
    src_encode = "utf8"
    register_map = {}

    def __init__(self, keil_file):
        if not os.path.exists(keil_file):
            raise Exception(f"keil_file not exist: {keil_file}")
        base, ext = os.path.splitext(keil_file)
        sdcc_file = f"{base}.sdcc.{ext}"
        f_keil = open(keil_file, "r", encoding=self.src_encode)
        f_sdcc = open(sdcc_file, "w", encoding=self.src_encode)
        for line in f_keil.readlines():
            sdcc_line = self.translate_line(line)
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
        indent = len(c_line) - len(c_line.lstrip(" "))
        if c_line.find("//") != -1:
            statements_line, comments = c_line.split("//")
            comments = "//"+comments
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

    def translate_line(self, c51_line):
        indent, statements_words, statements_line_end, comments = self.parse_line(c51_line)
        # keil 2 sdcc
        if not statements_words:
            if comments is not None:
                sdcc_line = f"{comments}"
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
                    if word in self.keil_memory_types:
                        statements.remove(word)
                        statements.remove(addr)
                        statements.remove("_at_")
                        statements = [word, "__at", f"({addr})"] + statements
                        break
                else:
                    raise Exception(f"unsupport keil memory types")

            # translate register_type
            # sfr name = address;
            if statements[0] in self.keil_register_types:
                register_type, name = statements[0:2]
                addr = "".join(statements[3:])
                self.register_map[name] = addr
                if register_type == "sbit" and "^" in addr:
                    base_addr, sub_addr = addr.split("^", 1)
                    if base_addr in self.register_map:
                        base_addr = self.register_map[base_addr]
                    addr = f"{base_addr}+{sub_addr}"
                statements = [register_type, "__at", f"({addr})", name]

                # traslate keyword
            for word in statements:
                if word in self.keil2sdcc_dict:
                    statements[statements.index(
                        word)] = self.keil2sdcc_dict[word]
            statements_words[idx] = statements  # update
        statements_line = ";".join([" ".join(statements) for statements in statements_words]) + statements_line_end
        if comments is not None:
            sdcc_line = statements_line + f"{comments}"
        else:
            sdcc_line = statements_line + "\n"
        sdcc_line = f"{' '*indent}{sdcc_line}"
        return sdcc_line


C512SDCC("src/c512sdcc.c")
