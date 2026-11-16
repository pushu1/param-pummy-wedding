import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'src=["\']([^"\']+)["\']', html)
hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)

all_assets = set([s for s in srcs if not s.startswith('http') and not s.startswith('#')] + 
                 [h for h in hrefs if not h.startswith('http') and not h.startswith('#') and not h.startswith('tel:') and not h.startswith('mailto:')])

missing = []
for a in sorted(all_assets):
    clean_a = a.split('?')[0].split('#')[0]
    if not os.path.exists(clean_a):
        missing.append(a)
    else:
        print(f'  [OK] {clean_a} (size: {os.path.getsize(clean_a)} bytes)')

if missing:
    print('MISSING ASSETS:', missing)
else:
    print('\nALL ASSETS VERIFIED SUCCESSFULLY!')
