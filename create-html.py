#!/usr/bin/env python
import subprocess
import glob

content = ''

with open('html.pre') as fp:
    content += fp.read()

files = sorted([f for f in glob.glob('*.md') if f not in ('LICENSE.md', 'README.md')])

# I am not proud of this
content += subprocess.check_output('cat README.md {} |markdown'.format(' '.join(files)), shell=True)

with open('html.post') as fp:
    content += fp.read()

print content
