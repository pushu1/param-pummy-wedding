import os
import qrcode
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register fonts
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

def generate_kuldeep_tina_pdf(
    output_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\Kuldeep_Tina_Royal_Wedding_Invitation.pdf',
    website_url='https://pushu1.github.io/param-pummy-wedding/',
    maps_url='https://maps.app.goo.gl/hPi6DXWJZEpUG5Vm9',
    qr_img_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\venue_maps_qr.png',
    seal_img_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\kt_wax_seal.png'
):
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
    c.setTitle('Kuldeep & Tina - Royal Wedding Invitation')
    c.setAuthor('Upadhyay & Vajpayee Family')
    c.setSubject('Official Wedding Invitation of Chiranjeev Kuldeep & Sou. Ka. Tina')

    # Background: Warm Ivory / Cream (#FBF8F2)
    c.setFillColor(colors.HexColor('#F8F4EC'))
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Inner Pearl Border
    c.setFillColor(colors.HexColor('#FFFDF9'))
    c.roundRect(14, 14, width - 28, height - 28, 14, stroke=0, fill=1)

    # Double Antique Gold Ornamental Borders
    gold_outer = colors.HexColor('#C59B27')
    gold_inner = colors.HexColor('#E5C478')
    gold_bright = colors.HexColor('#F8E5B8')
    ink_deep = colors.HexColor('#2E2018')
    ink_muted = colors.HexColor('#6B5547')

    c.setStrokeColor(gold_outer)
    c.setLineWidth(1.8)
    c.roundRect(24, 24, width - 48, height - 48, 10, stroke=1, fill=0)

    c.setStrokeColor(gold_inner)
    c.setLineWidth(0.8)
    c.roundRect(30, 30, width - 60, height - 60, 6, stroke=1, fill=0)

    # Corner decorative filigree marks
    def draw_corner(cx, cy, flip_x, flip_y):
        c.saveState()
        c.setStrokeColor(gold_outer)
        c.setLineWidth(1.2)
        c.setFillColor(gold_outer)
        s = 18
        c.line(cx, cy, cx + flip_x * s, cy)
        c.line(cx, cy, cx, cy + flip_y * s)
        c.circle(cx + flip_x * 6, cy + flip_y * 6, 2, fill=1, stroke=0)
        c.restoreState()

    draw_corner(34, height - 34, 1, -1)
    draw_corner(width - 34, height - 34, -1, -1)
    draw_corner(34, 34, 1, 1)
    draw_corner(width - 34, 34, -1, 1)

    # Top Sacred Emblem & Shloka
    y = height - 52
    c.setFont('Nirmala-Bold', 14)
    c.setFillColor(gold_outer)
    c.drawCentredString(width / 2, y, '॥ श्री गणेशाय नमः ॥')

    y -= 14
    c.setFont('Georgia-Italic', 10)
    c.setFillColor(ink_muted)
    c.drawCentredString(width / 2, y, 'With the boundless divine blessings of Lord Shri Vinayakji Maharaj')

    # Ancestral Blessings
    y -= 18
    c.setFont('Nirmala', 9)
    c.setFillColor(ink_muted)
    c.drawCentredString(width / 2, y, 'स्व. श्रीमती जमना देवी - स्व. श्री हरचंदजी उपाध्याय (सुपड़पौत्र) एवं स्व. श्रीमती पेपी देवी - स्व. श्री चम्पालालजी उपाध्याय (सुपौत्र)')

    # Invitation Announcement
    y -= 20
    c.setFont('Georgia', 9.5)
    c.setFillColor(ink_deep)
    c.drawCentredString(width / 2, y, 'Smt. Chandra Devi & Shri Jasrajji Upadhyay')
    y -= 13
    c.drawCentredString(width / 2, y, 'cordially invite you to celebrate the auspicious wedding ceremony of their beloved son')

    # Couple's Names in Opulent Serif Calligraphy
    y -= 30
    c.setFont('Georgia-Bold', 22)
    c.setFillColor(colors.HexColor('#8B5A10'))
    c.drawCentredString(width / 2, y, 'Chiranjeev Kuldeep')

    y -= 16
    c.setFont('Georgia-Italic', 13)
    c.setFillColor(gold_outer)
    c.drawCentredString(width / 2, y, '— weds —')

    y -= 22
    c.setFont('Georgia-Bold', 22)
    c.setFillColor(colors.HexColor('#8B5A10'))
    c.drawCentredString(width / 2, y, 'Sou. Ka. Tina')

    y -= 14
    c.setFont('Georgia-Italic', 8.5)
    c.setFillColor(ink_muted)
    c.drawCentredString(width / 2, y, 'Daughter of Smt. Manju Devi & Shri Ramgopalji Vajpayee')
    y -= 11
    c.drawCentredString(width / 2, y, 'Granddaughter of Late Smt. Janki Devi & Late Shri Chhogalalji Vajpayee')

    # Auspicious Date Line
    y -= 18
    c.setFont('Georgia-Bold', 10.5)
    c.setFillColor(colors.HexColor('#9E6D18'))
    c.drawCentredString(width / 2, y, '✦ FRIDAY, 11 DECEMBER 2026 • AUSPICIOUS WEDDING MUHURAT ✦')

    y -= 12
    c.setFont('Nirmala', 8)
    c.setFillColor(ink_muted)
    c.drawCentredString(width / 2, y, 'विक्रम संवत् 2083 रा मिगसर सुदी 2 बीज • Pali, Rajasthan')

    # Wedding Functions Schedule Grid Box
    y -= 14
    box_w = width - 84
    box_h = 138
    box_x = (width - box_w) / 2
    box_y = y - box_h

    c.setFillColor(colors.HexColor('#FDFBF7'))
    c.setStrokeColor(gold_inner)
    c.setLineWidth(1)
    c.roundRect(box_x, box_y, box_w, box_h, 8, stroke=1, fill=1)

    c.setFont('Georgia-Bold', 9.5)
    c.setFillColor(gold_outer)
    c.drawCentredString(width / 2, box_y + box_h - 14, 'AUSPICIOUS CELEBRATIONS & CEREMONIES')

    c.setFont('Georgia', 7.5)
    c.setFillColor(ink_deep)
    events = [
        ('Dhupawan (Ghritpan):', '05 Dec 2026, Saturday — 07:30 AM (Residence)'),
        ('Vinayak Sthapana:', '07 Dec 2026, Monday — 09:15 AM (Residence)'),
        ('Mayra Ceremony:', '10 Dec 2026, Thursday — 10:00 AM (Residence)'),
        ('Jeneu Sanskar:', '10 Dec 2026, Thursday — 04:00 PM (Residence)'),
        ('Bandoli Celebration:', '10 Dec 2026, Thursday — 07:00 PM (Residence)'),
        ('Baraat Prasthan:', '11 Dec 2026, Friday — 07:30 AM (Residence)'),
        ('Panigrahan Sanskar (Wedding):', '11 Dec 2026, Friday — Madhyaratri 02:00 AM'),
        ('Blessing Ceremony & Reception:', '13 Dec 2026, Sunday — 06:00 PM onwards at Jain Bagbera Dadawadi'),
    ]

    ey = box_y + box_h - 28
    for ev_name, ev_time in events:
        c.setFont('Georgia-Bold', 7.5)
        c.drawString(box_x + 16, ey, ev_name)
        c.setFont('Georgia', 7.5)
        c.drawString(box_x + 148, ey, ev_time)
        ey -= 13.5

    # Wax Seal in center above banner
    if os.path.exists(seal_img_path):
        seal_size = 56
        c.drawImage(seal_img_path, (width - seal_size) / 2, box_y - seal_size - 4, width=seal_size, height=seal_size, mask='auto')

    # CLICKABLE BANNER SECTION (OPENS DIGITAL WEBSITE)
    banner_w = width - 96
    banner_h = 52
    banner_x = (width - banner_w) / 2
    banner_y = box_y - seal_size - banner_h - 10

    # Banner Outer Shadow / Gold Gradient Fill
    c.setStrokeColor(colors.HexColor('#C59B27'))
    c.setLineWidth(1.8)
    c.setFillColor(colors.HexColor('#D4AF37'))
    c.roundRect(banner_x, banner_y, banner_w, banner_h, 10, stroke=1, fill=1)

    c.setStrokeColor(colors.HexColor('#FFF2D1'))
    c.setLineWidth(0.8)
    c.roundRect(banner_x + 3, banner_y + 3, banner_w - 6, banner_h - 6, 8, stroke=1, fill=0)

    # Banner Text
    c.setFont('Georgia-Bold', 12.5)
    c.setFillColor(colors.HexColor('#2A1A0C'))
    c.drawCentredString(width / 2, banner_y + 29, '✨ OPEN YOUR WEDDING INVITATION ✨')

    c.setFont('Georgia-Italic', 8.5)
    c.setFillColor(colors.HexColor('#3D2510'))
    c.drawCentredString(width / 2, banner_y + 13, 'Tap here to experience our cinematic royal invitation website ↗')

    # EMBEDDED REAL HYPERLINK ON BANNER!
    c.linkURL(website_url, (banner_x, banner_y, banner_x + banner_w, banner_y + banner_h), relative=0)

    # GOOGLE MAPS LOCATION & QR CODE SECTION
    qr_size = 60
    bottom_y = banner_y - qr_size - 16

    # QR Code on Left
    qr_x = (width / 2) - qr_size - 70
    if os.path.exists(qr_img_path):
        c.setFillColor(colors.white)
        c.roundRect(qr_x - 3, bottom_y - 3, qr_size + 6, qr_size + 6, 4, stroke=0, fill=1)
        c.drawImage(qr_img_path, qr_x, bottom_y, width=qr_size, height=qr_size)
        c.linkURL(maps_url, (qr_x - 3, bottom_y - 3, qr_x + qr_size + 3, bottom_y + qr_size + 3), relative=0)

    # Venue & Maps Text on Right
    note_x = qr_x + qr_size + 14
    c.setFont('Georgia-Bold', 8.5)
    c.setFillColor(gold_outer)
    c.drawString(note_x, bottom_y + 46, 'RECEPTION VENUE & GOOGLE MAPS')

    c.setFont('Georgia-Bold', 8)
    c.setFillColor(ink_deep)
    c.drawString(note_x, bottom_y + 34, 'Jain Bagbera Dadawadi, Venkatesh Marg, Pali (Raj.)')

    c.setFont('Georgia', 7)
    c.setFillColor(ink_muted)
    c.drawString(note_x, bottom_y + 23, '• Scan or tap QR code for direct GPS Google Maps navigation')
    c.drawString(note_x, bottom_y + 12, '• Tap here: View Reception Location in Google Maps ↗')
    c.linkURL(maps_url, (note_x, bottom_y + 10, note_x + 230, bottom_y + 22), relative=0)
    c.drawString(note_x, bottom_y + 1, '• Enquiries: Jasraj Upadhyay (9461061236, 9887997822)')

    # Footer Acknowledgement
    c.setFont('Georgia', 6.8)
    c.setFillColor(ink_muted)
    footer_text = 'With Best Compliments from Jasraj Mangilal Upadhyay & Family • 255, 256, Ram Nagar, Pali (Raj.)'
    c.drawCentredString(width / 2, 36, footer_text)

    c.save()
    print(f'Successfully generated PDF at: {output_path}')
    return output_path

if __name__ == '__main__':
    generate_kuldeep_tina_pdf()
