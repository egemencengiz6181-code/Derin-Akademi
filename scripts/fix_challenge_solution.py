import os
import re
import json

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get page identifier from file name
    page_id = os.path.basename(file_path).replace('.html', '')
    # Map file names to the keys used in tr.json
    file_to_key_map = {
        'aileden-kuruma': 'aileden',
        'gelecege-hazir-kadro': 'kadro',
        'gelisimi-olc': 'olc',
        'hoshin-kanri': 'hoshin',
        'iceriden-guclen': 'guclen',
        'stratejiyi-gundelik-hayata': 'strateji',
        'ucret-stratejisi': 'ucret',
        'yetenek-yonetimi': 'yetenek'
    }
    short_id = file_to_key_map.get(page_id, page_id)

    # 1. Handle Challenge Title
    # Look for the section title within cs-col-challenge
    challenge_title_pattern = r'(<div class="cs-col cs-col-challenge">.*?<span class="cs-col-title")[^>]*>(.*?)</span>'
    content = re.sub(challenge_title_pattern, r'\1 data-i18n="shared.challenge.title">\2</span>', content, flags=re.DOTALL)

    # 2. Handle Solution Title
    solution_title_pattern = r'(<div class="cs-col cs-col-solution">.*?<span class="cs-col-title")[^>]*>(.*?)</span>'
    content = re.sub(solution_title_pattern, r'\1 data-i18n="shared.solution.title">\2</span>', content, flags=re.DOTALL)

    # 3. Handle Challenge List Items
    def challenge_replacer(match):
        col_content = match.group(0)
        items = re.findall(r'<li><span class="bullet">✖</span> (.*?)</li>', col_content)
        new_col_content = col_content
        for i, text in enumerate(items):
            key = f"danis.{short_id}.prob{i+1}"
            old_li = f'<li><span class="bullet">✖</span> {text}</li>'
            if 'data-i18n' not in old_li:
                new_li = f'<li><span class="bullet">✖</span> <span data-i18n="{key}">{text}</span></li>'
                new_col_content = new_col_content.replace(old_li, new_li)
        return new_col_content

    content = re.sub(r'<div class="cs-col cs-col-challenge">.*?</ul>', challenge_replacer, content, flags=re.DOTALL)

    # 4. Handle Solution List Items
    def solution_replacer(match):
        col_content = match.group(0)
        items = re.findall(r'<li><span class="bullet">✔</span> (.*?)</li>', col_content)
        new_col_content = col_content
        for i, text in enumerate(items):
            key = f"danis.{short_id}.sol{i+1}"
            old_li = f'<li><span class="bullet">✔</span> {text}</li>'
            if 'data-i18n' not in old_li:
                new_li = f'<li><span class="bullet">✔</span> <span data-i18n="{key}">{text}</span></li>'
                new_col_content = new_col_content.replace(old_li, new_li)
        return new_col_content

    content = re.sub(r'<div class="cs-col cs-col-solution">.*?</ul>', solution_replacer, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

path = 'danismanliklar/'
files = [f for f in os.listdir(path) if f.endswith('.html')]
for filename in files:
    print(f"Processing {filename}...")
    process_file(os.path.join(path, filename))

print("Done!")
