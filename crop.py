import re
base = open('figma/Untitled.svg', encoding='utf-8').read()
old = 'width="1920" height="5000" viewBox="0 0 1920 5000"'
assert old in base, 'pattern not found'
base = base.replace(old, '@@VIEWBOX@@')
# ลบพื้นหลังเต็มผืน 2 ชั้นให้รูปโปร่งใส กลืนกับพื้นเว็บ
base = re.sub(r'<rect width="1920" height="5000" fill="#[A-F0-9]+"/>\n?', '', base)
# คำบรรยายจบ y=323 ขอบบนแฟ้มเริ่ม ~370 ผ่าที่ 330 กลางช่องว่าง
open('figma/art-title.svg', 'w', encoding='utf-8').write(
    base.replace('@@VIEWBOX@@', 'viewBox="700 100 500 230"'))
open('figma/art-folder.svg', 'w', encoding='utf-8').write(
    base.replace('@@VIEWBOX@@', 'viewBox="700 330 500 410"'))
print('ok')
