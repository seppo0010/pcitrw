#!/usr/bin/env python
import os.path
import re
import sys

if len(sys.argv) < 3:
    sys.stderr.write('Invalid parameters. Use: {} <text file> <dictionary> [dictionaries..]\n'.format(sys.argv[0]))
    sys.exit(1)

dict_words = set()
for filename in sys.argv[2:]:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r') as fp:
        for line in fp.readlines():
            dict_words.add(line.strip())

with open(sys.argv[1], 'r') as fp:
    text = ''
    for line in fp.readlines():
        if line[0] == '!' or line[0] == '#' or line[0] == ' ':
            continue
        line = line.strip().lower()
        line = re.sub(r'https?\:\/\/[a-zA-Z0-9\=\?\&\.\/\-\%]+', '', line)
        text += re.sub(r'[#\.\,\;\:\?\"]', '', line) + '\n'
    text_words = re.split('[\s\'-\/\[\]\(\)]', text)


bad_words = set()
for word in text_words:
    if len(word) == 0 or re.match(r'^[0-9]+$', word):
        continue

    if word not in dict_words:
        bad_words.add(word)

if len(bad_words) > 0:
    for word in bad_words:
        sys.stderr.write(word + '\n')
    sys.exit(1)
