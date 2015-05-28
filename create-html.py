#!/usr/bin/env python
# I am not proud by the content of this file, but it does what needs to be done
import subprocess
import sys
import glob

def render_file(f):
    return subprocess.check_output(('markdown', f))

with open('html.pre') as fp:
    sys.stdout.write(fp.read())

sys.stdout.write(render_file('README.md'))

files = sorted([f for f in glob.glob('*.md') if f not in ('LICENSE.md', 'README.md')])

index = {}
sys.stdout.write('<h2>Index</h2><ul>')
for f in files:
    with open(f) as fp:
        title = fp.readline().replace('#', '')
    if f[0:5] == '01-00':
        sys.stdout.write('<li><a href="#{}">{}</a><ul>'.format(f[:-3], title))
    elif f[3:5] == '00':
        sys.stdout.write('</ul></li><li><a href="#{}">{}</a><ul>'.format(f[:-3], title))
    else:
        sys.stdout.write('<li><a href="#{}">{}</a></li>'.format(f[:-3], title))
sys.stdout.write('</ul></li></ul>')

for f in files:
    sys.stdout.write('<a name="{}"></a>'.format(f[:-3]))
    sys.stdout.write(render_file(f))

with open('html.post') as fp:
    sys.stdout.write(fp.read())
