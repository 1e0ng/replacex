#!/usr/bin/python
import os
import re
import sys

def replace(infile, outfile, from_re, to_re):
    f1 = open(infile)
    f0 = open(outfile, 'w')
    data = f1.read()
    f0.write(re.sub(from_re, to_re, data, flags=re.M))
    f1.close()
    f0.close()

def rep_folder(path, from_re, to_re, file_re):
    print("Current Path: %s" % path)
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if re.search(file_re, filename):
                print("> %s ..." % filename)
                fi = open(os.path.join(dirpath, filename))
                fo = open(os.path.join(dirpath, filename + ".bk"), 'w')
                fo.write(fi.read())
                fo.close()
                fi.close()
                replace(os.path.join(dirpath, filename + ".bk"),
                          os.path.join(dirpath, filename), from_re, to_re)
                print("Done.")
                os.remove(os.path.join(dirpath, filename + ".bk"))

def main():
    nums = len(sys.argv)
    if nums not in (3, 4):
        print('Usage: replacex FROM_REGEX TO_REGEX [FILENAME_REGEX]')
        exit()

    path = os.getcwd()
    from_regex = sys.argv[1]
    to_regex = sys.argv[2]
    filename_regex = r'^[^.].*\.(h|m|mm|md|cpp|inl|def|txt|php|tpl|css|js|py|go)$' if nums == 3 else sys.argv[3]

    rep_folder(path, from_regex, to_regex, filename_regex)
