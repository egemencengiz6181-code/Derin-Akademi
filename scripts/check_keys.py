import json

with open('locales/tr.json') as f:
    tr = json.load(f)
with open('locales/en.json') as f:
    en = json.load(f)

keys_to_check = [
    'idx.cta.title','idx.cta.title1','idx.cta.title2',
    'kurs.hero.title','kurs.hero.title1','kurs.hero.title2',
    'danis.hero.title','danis.hero.title1','danis.hero.title2',
    'danis.section.title','danis.section.title1','danis.section.title2',
    'danis.approach.title','danis.approach.title1','danis.approach.title2',
    'danis.cta.title','danis.cta.title1','danis.cta.title2',
    'danis.sectors.title','danis.sectors.title1','danis.sectors.title2',
    'shared.challenge.title','shared.solution.title',
    'shared.process.label','shared.process.title','shared.scope.title',
    'shared.footer.brandesc','shared.footer.gizlilik',
    'danis.aileden.cta.title','danis.aileden.cta.desc',
    'danis.gelecege.category','danis.gelecege.title','danis.gelecege.subtitle',
    'danis.gelisimi.category','danis.gelisimi.title','danis.gelisimi.subtitle',
    'danis.iceriden.category','danis.iceriden.title','danis.iceriden.subtitle',
    'danis.strateji.category','danis.strateji.title','danis.strateji.subtitle',
    'danis.ucret.category','danis.ucret.title','danis.ucret.subtitle',
    'danis.yetenek.category','danis.yetenek.title','danis.yetenek.subtitle',
]

print("=== TR STATUS ===")
for k in keys_to_check:
    v = tr.get(k)
    if v:
        print(f"  OK  {k}: {str(v)[:70]}")
    else:
        print(f"  !!  {k}: MISSING")

print()
print("=== EN STATUS ===")
for k in keys_to_check:
    v = en.get(k)
    if v:
        print(f"  OK  {k}: {str(v)[:70]}")
    else:
        print(f"  !!  {k}: MISSING")
