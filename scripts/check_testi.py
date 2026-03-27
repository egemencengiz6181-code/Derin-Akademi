import re

content = open('index.html', encoding='utf-8').read()

# Find testimonials section lines
lines = content.split('\n')
for i, l in enumerate(lines):
    if 'CTA' in l and '==' in l:
        print(f'CTA at line {i+1}')
    if 'tsc-name' in l:
        print(f'tsc-name at line {i+1}: {l[:80]}')
    if 'Fatih' in l or 'Burak' in l or 'Onur' in l:
        print(f'Line {i+1}: {l[:80]}')
