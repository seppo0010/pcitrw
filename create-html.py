#!/usr/bin/env python
# I am not proud by the content of this file, but it does what needs to be done
import subprocess
import glob

content = ''

def render_file(f):
    return subprocess.check_output(('markdown', f))

with open('html.pre') as fp:
    content += fp.read()

content += render_file('README.md')

files = sorted([f for f in glob.glob('*.md') if f not in ('LICENSE.md', 'README.md')])

index = {}
content += '<h2>Index</h2><ul>'
for f in files:
    with open(f) as fp:
        title = fp.readline().replace('#', '')
    if f[0:5] == '01-00':
        content += '<li><a href="#{}">{}</a><ul>'.format(f[:-3], title)
    elif f[3:5] == '00':
        content += '</ul></li><li><a href="#{}">{}</a><ul>'.format(f[:-3], title)
    else:
        content += '<li><a href="#{}">{}</a></li>'.format(f[:-3], title)
content += '</ul></li></ul>'

for f in files:
    content += '<a name="{}"></a>'.format(f[:-3])
    content += render_file(f)

with open('html.post') as fp:
    content += fp.read()

print content
