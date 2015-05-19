#!/usr/bin/env python
from glob import glob
import subprocess
import sys

for filename in glob('*.md'):
    if filename in ('README.md', 'LICENSE.md'):
        continue

    sys.stderr.write('Checking {}\n'.format(filename))
    try:
        subprocess.check_call(('python', 'check-file.py', filename, '1000-words.txt', filename[:-3] + '.words.txt'))
    except:
        sys.exit(1)
