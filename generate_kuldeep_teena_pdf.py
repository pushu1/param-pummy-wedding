import os
import qrcode
from PIL import Image, ImageDraw, ImageOps
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register system fonts
try:
    pdfmetrics.registerFont(TTFont('Georgia', r'C:\Windows\Fonts\georgia.ttf'))
    pdfmetrics.registerFont(TTFont('Georgia-Bold', r'C:\Windows\Fonts\georgiab.ttf'))
    pdfmetrics.registerFont(TTFont('Georgia-Italic', r'C:\Windows\Fonts\georgiai.ttf'))
except Exception as e:
    print('Georgia font fallback:', e)

try:
    pdfmetrics.registerFont(TTFont('Nirmala', r'C:\Windows\Fonts\Nirmala.ttf'))
    pdfmetrics.registerFont(TTFont('Nirmala-Bold', r'C:\Windows\Fonts\NirmalaB.ttf'))
except Exception as e:
    print('Nirmala font fallback:', e)

def create_arched_portrait(img_path, output_path, size=(400, 500), border_color=(212, 175, 55), border_w=6):
    """Crop an image into a regal arched frame with gold border for the royal cover."""
    img = Image.open(img_path).convert("RGBA")
    w, h = size
    
    # Resize and center crop
    aspect_target = w / h
    img_w, img_h = img.size
    aspect_img = img_w / img_h
    
    if aspect_img > aspect_target:
        new_w = int(img_h * aspect_target)
        left = (img_w - new_w) // 2
        img = img.crop((left, 0, left + new_w, img_h))
    else:
        new_h = int(img_w / aspect_target)
        top = (img_h - new_h) // 2
        img = img.crop((0, top, img_w, top + new_h))
        
    img = img.resize((w, h), Image.Resampling.LANCZOS)
    
    # Create arch mask (top half ellipse/round, bottom rect)
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    radius = w // 2
    draw.pieslice([(0, 0), (w, w)], 180, 360, fill=255)
    draw.rectangle([(0, radius), (w, h)], fill=255)
    
    # Apply mask
    result = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    result.paste(img, (0, 0), mask=mask)
    
    # Draw gold border
    draw_res = ImageDraw.Draw(result)
    for i in range(border_w):
        draw_res.arc([(i, i), (w - 1 - i, w - 1 - i)], 180, 360, fill=border_color)
        draw_res.line([(i, radius), (i, h - 1 - i)], fill=border_color)
        draw_res.line([(w - 1 - i, radius), (w - 1 - i, h - 1 - i)], fill=border_color)
        draw_res.line([(i, h - 1 - i), (w - 1 - i, h - 1 - i)], fill=border_color)
        
    result.save(output_path, "PNG")
    return output_path

def generate_kuldeep_teena_pdf(
    output_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\Kuldeep_Teena_Royal_Wedding_Invitation.pdf',
    website_url='https://pushu1.github.io/param-pummy-wedding/',
    maps_url='https://maps.app.goo.gl/hPi6DXWJZEpUG5Vm9',
    groom_img=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\groom_kuldeep.jpg',
    bride_img=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\bride_teena.jpg',
    qr_img_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\venue_maps_qr.png',
    seal_img_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\kt_wax_seal.png'
):
    assets_dir = os.path.dirname(output_path)
    groom_arch = os.path.join(assets_dir, 'groom_arch.png')
    bride_arch = os.path.join(assets_dir, 'bride_arch.png')
    
    create_arched_portrait(groom_img, groom_arch, size=(360, 460))
    create_arched_portrait(bride_img, bride_arch, size=(360, 460))
    
    # Ensure maps QR code exists
    if not os.path.exists(qr_img_path):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2,
        )
        qr.add_data(maps_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='#3D2E24', back_color='#FFFDF9')
        img.save(qr_img_path)

    width, height = A4
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setTitle('Kuldeep & Teena - Royal Wedding Invitation')
    c.setAuthor('Upadhyay & Vajpayee Family')
    c.setSubject('Official Royal Wedding Invitation of Chiranjeev Kuldeep & Sou. Ka. Teena')

    # Color palette
    c_maroon = colors.HexColor('#4A0E17')
    c_deep_maroon = colors.HexColor('#38070F')
    c_gold = colors.HexColor('#D4AF37')
    c_gold_light = colors.HexColor('#F3E5AB')
    c_gold_dim = colors.HexColor('#AA820A')
    c_ivory = colors.HexColor('#FDFBF7')
    c_ink_deep = colors.HexColor('#2E2018')
    c_ink_muted = colors.HexColor('#6B5547')

    # =========================================================================
    # PAGE 1: LUXURY ROYAL WEDDING COVER (MINIMAL, OPULENT, STRICTLY SPECIFIED)
    # User Requirement:
    # - Groom photograph
    # - Bride photograph
    # - Wedding date: 11 DECEMBER 2026
    # - Couple's names: KULDEEP WEDS TEENA (main visual focus!)
    # - Strictly NO family details, NO long paragraphs, NO schedules, NO countdown.
    # =========================================================================
    
    # Deep royal maroon luxury background
    c.setFillColor(c_maroon)
    c.rect(0, 0, width, height, stroke=0, fill=1)
    
    # Outer ornamental gold border
    c.setStrokeColor(c_gold)
    c.setLineWidth(2.0)
    c.roundRect(20, 20, width - 40, height - 40, 12, stroke=1, fill=0)
    
    # Inner delicate gold border
    c.setStrokeColor(c_gold_light)
    c.setLineWidth(0.8)
    c.roundRect(26, 26, width - 52, height - 52, 8, stroke=1, fill=0)
    
    # Corner filigree accents
    def draw_cover_corner(cx, cy, flip_x, flip_y):
        c.saveState()
        c.setStrokeColor(c_gold)
        c.setLineWidth(1.4)
        c.setFillColor(c_gold)
        s = 22
        c.line(cx, cy, cx + flip_x * s, cy)
        c.line(cx, cy, cx, cy + flip_y * s)
        c.circle(cx + flip_x * 7, cy + flip_y * 7, 2.5, fill=1, stroke=0)
        c.circle(cx + flip_x * 14, cy + flip_y * 4, 1.5, fill=1, stroke=0)
        c.circle(cx + flip_x * 4, cy + flip_y * 14, 1.5, fill=1, stroke=0)
        c.restoreState()

    draw_cover_corner(30, height - 30, 1, -1)
    draw_cover_corner(width - 30, height - 30, -1, -1)
    draw_cover_corner(30, 30, 1, 1)
    draw_cover_corner(width - 30, 30, -1, 1)

    # Top Royal Auspicious Emblem
    y_cover = height - 58
    c.setFont('Nirmala-Bold', 15)
    c.setFillColor(c_gold)
    c.drawCentredString(width / 2, y_cover, '॥ श्री गणेशाय नमः ॥')
    
    y_cover -= 16
    c.setFont('Georgia-Italic', 11)
    c.setFillColor(c_gold_light)
    c.drawCentredString(width / 2, y_cover, '✦   A U S P I C I O U S   W E D D I N G   I N V I T A T I O N   ✦')

    # Portraits Showcase: Groom and Bride in arched royal frames
    # Sizing for side-by-side arched portraits
    pw, ph = 190, 242
    spacing = 26
    total_w = pw * 2 + spacing
    start_x = (width - total_w) / 2
    portraits_y = y_cover - 24 - ph
    
    # Groom Arch Image
    c.drawImage(groom_arch, start_x, portraits_y, width=pw, height=ph, mask='auto')
    # Bride Arch Image
    c.drawImage(bride_arch, start_x + pw + spacing, portraits_y, width=pw, height=ph, mask='auto')
    
    # Decorative ornamental flourish between portraits
    mid_x = width / 2
    mid_y = portraits_y + (ph / 2)
    c.setFillColor(c_gold)
    c.setFont('Georgia', 18)
    c.drawCentredString(mid_x, mid_y - 6, '❦')

    # Main Visual Focus: Couple's Names
    # KULDEEP
    # WEDS
    # TEENA
    names_top_y = portraits_y - 45
    c.setFont('Georgia-Bold', 36)
    c.setFillColor(c_gold_light)
    c.drawCentredString(width / 2, names_top_y, 'K U L D E E P')
    
    c.setFont('Georgia-Italic', 20)
    c.setFillColor(c_gold)
    c.drawCentredString(width / 2, names_top_y - 28, '—   w e d s   —')
    
    c.setFont('Georgia-Bold', 36)
    c.setFillColor(c_gold_light)
    c.drawCentredString(width / 2, names_top_y - 62, 'T E E N A')

    # Date Headline: 11 DECEMBER 2026
    date_y = names_top_y - 110
    c.setStrokeColor(c_gold)
    c.setLineWidth(1)
    line_len = 80
    c.line((width / 2) - line_len - 110, date_y + 5, (width / 2) - 110, date_y + 5)
    c.line((width / 2) + 110, date_y + 5, (width / 2) + line_len + 110, date_y + 5)
    
    c.setFont('Georgia-Bold', 18)
    c.setFillColor(c_gold)
    c.drawCentredString(width / 2, date_y, '11  DECEMBER  2026')
    
    c.setFont('Georgia', 10.5)
    c.setFillColor(c_gold_light)
    c.drawCentredString(width / 2, date_y - 18, 'P A L I ,   R A J A S T H A N')
    
    # Subtle tap hint for Page 2
    c.setFont('Georgia-Italic', 9.5)
    c.setFillColor(colors.HexColor('#E0C58A'))
    c.drawCentredString(width / 2, 42, 'Scroll / Turn page for Celebrations & Invitation Schedule ➔')

    # End Page 1
    c.showPage()

    # =========================================================================
    # PAGE 2: CEREMONIAL INVITATION, SACRED SCHEDULE, BANNER & GPS QR CODE
    # =========================================================================
    
    # Warm Ivory / Rich Cream Luxury Background
    c.setFillColor(c_ivory)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Double Gold Ornamental Borders
    c.setStrokeColor(c_gold)
    c.setLineWidth(1.8)
    c.roundRect(20, 20, width - 40, height - 40, 10, stroke=1, fill=0)

    c.setStrokeColor(colors.HexColor('#E5C478'))
    c.setLineWidth(0.8)
    c.roundRect(26, 26, width - 52, height - 52, 6, stroke=1, fill=0)

    draw_cover_corner(30, height - 30, 1, -1)
    draw_cover_corner(width - 30, height - 30, -1, -1)
    draw_cover_corner(30, 30, 1, 1)
    draw_cover_corner(width - 30, 30, -1, 1)

    # Top Sacred Invocation
    y2 = height - 48
    c.setFont('Nirmala-Bold', 13)
    c.setFillColor(colors.HexColor('#8B5A10'))
    c.drawCentredString(width / 2, y2, '॥ श्री विनायकजी महाराज की असीम अनुकम्पा से ॥')

    # Ancestral Blessings
    y2 -= 16
    c.setFont('Nirmala', 8.5)
    c.setFillColor(c_ink_muted)
    c.drawCentredString(width / 2, y2, 'स्व. श्रीमती जमना देवी - स्व. श्री हरचंदजी उपाध्याय (सुपड़पौत्र) एवं स्व. श्रीमती पेपी देवी - स्व. श्री चम्पालालजी उपाध्याय (सुपौत्र)')

    # Formal Invitation Announcement
    y2 -= 18
    c.setFont('Georgia-Bold', 10)
    c.setFillColor(c_ink_deep)
    c.drawCentredString(width / 2, y2, 'Smt. Chandra Devi & Shri Jasrajji Upadhyay')
    y2 -= 12
    c.setFont('Georgia', 8.5)
    c.drawCentredString(width / 2, y2, 'cordially invite you to celebrate the auspicious wedding ceremony of their beloved son')

    # Couple names with family lineage
    y2 -= 20
    c.setFont('Georgia-Bold', 15)
    c.setFillColor(c_maroon)
    c.drawCentredString(width / 2, y2, 'Chiranjeev Kuldeep')
    
    y2 -= 12
    c.setFont('Georgia-Italic', 11)
    c.setFillColor(c_gold)
    c.drawCentredString(width / 2, y2, '— संग —')
    
    y2 -= 15
    c.setFont('Georgia-Bold', 15)
    c.setFillColor(c_maroon)
    c.drawCentredString(width / 2, y2, 'Sou. Ka. Teena')
    
    y2 -= 11
    c.setFont('Georgia-Italic', 8)
    c.setFillColor(c_ink_muted)
    c.drawCentredString(width / 2, y2, 'Daughter of Smt. Manju Devi & Shri Ramgopalji Vajpayee • Granddaughter of Late Smt. Janki Devi & Late Shri Chhogalalji Vajpayee')

    # Wedding Functions Schedule Box (Exact Hindi Ceremonies from Original Card)
    y2 -= 15
    box_w = width - 70
    box_h = 162
    box_x = (width - box_w) / 2
    box_y = y2 - box_h

    # Ornate background for schedule
    c.setFillColor(colors.HexColor('#FDF7ED'))
    c.setStrokeColor(c_gold)
    c.setLineWidth(1.2)
    c.roundRect(box_x, box_y, box_w, box_h, 8, stroke=1, fill=1)

    c.setFont('Nirmala-Bold', 11)
    c.setFillColor(c_maroon)
    c.drawCentredString(width / 2, box_y + box_h - 15, 'मांगलिक पलों का सफर • WEDDING CEREMONIES SCHEDULE')

    c.setStrokeColor(colors.HexColor('#E5C478'))
    c.setLineWidth(0.6)
    c.line(box_x + 20, box_y + box_h - 20, box_x + box_w - 20, box_y + box_h - 20)

    # 8 Ceremonies in Hindi & Timings
    ceremonies = [
        ('घृतपान (धूपवान):', '05 दिसम्बर 2026, शनिवार — प्रातः 07.30 बजे (निज निवास)'),
        ('विनायक:', '07 दिसम्बर 2026, सोमवार — प्रातः 09.15 बजे (निज निवास)'),
        ('मायरा:', '10 दिसम्बर 2026, गुरूवार — प्रातः 10.00 बजे (निज निवास)'),
        ('जनेऊ संस्कार:', '10 दिसम्बर 2026, गुरूवार — शाम 04.00 बजे (निज निवास)'),
        ('बंदोली:', '10 दिसम्बर 2026, गुरूवार — शाम 07.00 बजे (निज निवास)'),
        ('बारात प्रस्थान:', '11 दिसम्बर 2026, शुक्रवार — प्रातः 07.30 बजे (निज निवास)'),
        ('पाणिग्रहण संस्कार:', '11 दिसम्बर 2026, शुक्रवार — मध्यरात्रि 02.00 बजे (शुभ विवाह मंडप)'),
        ('आशीर्वाद समारोह एवं प्रीतिभोज:', '13 दिसम्बर 2026, रविवार — सायं 06.00 बजे से (जैन बागबेरा दादावाडी, पाली)'),
    ]

    cur_ey = box_y + box_h - 34
    for c_title, c_desc in ceremonies:
        c.setFont('Nirmala-Bold', 8)
        c.setFillColor(colors.HexColor('#6B1724'))
        c.drawString(box_x + 14, cur_ey, c_title)
        
        c.setFont('Nirmala', 8)
        c.setFillColor(c_ink_deep)
        c.drawString(box_x + 140, cur_ey, c_desc)
        cur_ey -= 16

    # Wax Seal in Center
    seal_y = box_y - 20
    if os.path.exists(seal_img_path):
        seal_size = 46
        c.drawImage(seal_img_path, (width - seal_size) / 2, seal_y - seal_size / 2, width=seal_size, height=seal_size, mask='auto')

    # =========================================================================
    # CLICKABLE BANNER SECTION (OPENS THE LIVE DIGITAL EXPERIENCE)
    # =========================================================================
    banner_w = width - 80
    banner_h = 56
    banner_x = (width - banner_w) / 2
    banner_y = seal_y - 32 - banner_h

    # Banner Deep Maroon / Gold Border
    c.setFillColor(c_maroon)
    c.setStrokeColor(c_gold)
    c.setLineWidth(1.8)
    c.roundRect(banner_x, banner_y, banner_w, banner_h, 10, stroke=1, fill=1)

    c.setStrokeColor(c_gold_light)
    c.setLineWidth(0.8)
    c.roundRect(banner_x + 3, banner_y + 3, banner_w - 6, banner_h - 6, 8, stroke=1, fill=0)

    # Banner Typography
    c.setFont('Georgia-Bold', 13)
    c.setFillColor(c_gold_light)
    c.drawCentredString(width / 2, banner_y + 32, '✨ OPEN YOUR ROYAL WEDDING INVITATION ✨')

    c.setFont('Georgia-Italic', 9)
    c.setFillColor(colors.HexColor('#FFF2D1'))
    c.drawCentredString(width / 2, banner_y + 15, 'Tap anywhere on this banner to experience the interactive 3D digital invitation ↗')

    # EMBED CLICKABLE HYPERLINK ON BANNER!
    c.linkURL(website_url, (banner_x, banner_y, banner_x + banner_w, banner_y + banner_h), relative=0)

    # =========================================================================
    # VENUE & GOOGLE MAPS NAVIGATION QR CODE SECTION
    # =========================================================================
    qr_size = 66
    bottom_y = banner_y - qr_size - 18

    # QR Code on Left
    qr_x = (width / 2) - qr_size - 80
    if os.path.exists(qr_img_path):
        c.setFillColor(colors.white)
        c.setStrokeColor(c_gold)
        c.roundRect(qr_x - 3, bottom_y - 3, qr_size + 6, qr_size + 6, 4, stroke=1, fill=1)
        c.drawImage(qr_img_path, qr_x, bottom_y, width=qr_size, height=qr_size)
        c.linkURL(maps_url, (qr_x - 3, bottom_y - 3, qr_x + qr_size + 3, bottom_y + qr_size + 3), relative=0)

    # Venue Details & Tap Link on Right
    note_x = qr_x + qr_size + 14
    c.setFont('Nirmala-Bold', 9)
    c.setFillColor(c_maroon)
    c.drawString(note_x, bottom_y + 52, 'आशीर्वाद समारोह स्थल (Reception Venue):')

    c.setFont('Nirmala-Bold', 8.5)
    c.setFillColor(c_ink_deep)
    c.drawString(note_x, bottom_y + 39, 'जैन बागबेरा दादावाडी, वेंकटेश मार्ग, पाली (राज.)')

    c.setFont('Georgia', 7.5)
    c.setFillColor(c_ink_muted)
    c.drawString(note_x, bottom_y + 27, '• Scan or tap QR code for direct GPS Google Maps navigation')
    
    c.setFont('Georgia-Bold', 7.5)
    c.setFillColor(c_gold_dim)
    c.drawString(note_x, bottom_y + 15, '• Tap here: Open Reception Location in Google Maps ↗')
    c.linkURL(maps_url, (note_x, bottom_y + 13, note_x + 230, bottom_y + 25), relative=0)

    c.setFont('Nirmala', 7.5)
    c.setFillColor(c_ink_muted)
    c.drawString(note_x, bottom_y + 3, '• संपर्क: जसराजजी उपाध्याय (9461061236, 9887997822)')

    # Footer Acknowledgement (Uttarakanxi / Hosts)
    c.setFont('Nirmala', 7)
    c.setFillColor(c_ink_muted)
    footer_text = 'उत्तराकांक्षी: जसराज मांगीलाल उपाध्याय (सुपुत्र स्व. श्री चम्पालालजी उपाध्याय) • 255, 256, राम नगर, तीसरी गली, पाली (राज.)'
    c.drawCentredString(width / 2, 34, footer_text)

    c.save()
    print(f'Successfully generated 2-page Royal Wedding PDF at: {output_path}')
    return output_path

if __name__ == '__main__':
    generate_kuldeep_teena_pdf()
