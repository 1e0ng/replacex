#!/usr/bin/python
import os
import re
import sys

def replace(filename, original, updated):
    print("%s" % filename)

    fo = open(filename + ".bk", 'w')
    fo.write(original)
    fo.close()

    fi = open(filename, 'w')
    fi.write(updated)
    fi.close()

    os.remove(filename + ".bk")

def rep_folder(path, from_re, to_re, file_re):
    print("Current Path: %s" % path)
    for dirpath, dirs, files in os.walk(path):
        for filename in files:
            if re.search(file_re, filename):
                infile = os.path.join(dirpath, filename)
                original = open(infile).read()
                updated = re.sub(from_re, to_re, original, flags=re.M)
                if updated != original:
                    replace(infile, original, updated)

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
