import sys
from pypdf import PdfReader

pdf_path = r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\Param_Pummy_Royal_Wedding_Invitation.pdf'
reader = PdfReader(pdf_path)

print(f'Total pages: {len(reader.pages)}')
page = reader.pages[0]

annotations = page.get('/Annots')
print(f'Total annotations found: {len(annotations) if annotations else 0}')

verified_links = []
if annotations:
    for i, annot_ref in enumerate(annotations):
        annot = annot_ref.get_object()
        subtype = annot.get('/Subtype')
        rect = annot.get('/Rect')
        action = annot.get('/A')
        uri = action.get('/URI') if action else None
        print(f'Annotation {i}: Subtype={subtype}, Rect={rect}, URI={uri}')
        if subtype == '/Link' and uri:
            verified_links.append((uri, rect))

if verified_links:
    print('\n[SUCCESS] Hyperlinks successfully verified in PDF:')
    for uri, rect in verified_links:
        print(f'  -> Link to: {uri} at coordinates {rect}')
else:
    print('\n[FAILED] No hyperlinks found in PDF!')
    sys.exit(1)
