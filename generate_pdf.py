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
    print('Georgia font not found, falling back to Times-Roman:', e)

try:
    pdfmetrics.registerFont(TTFont('Nirmala', r'C:\Windows\Fonts\Nirmala.ttf'))
    pdfmetrics.registerFont(TTFont('Nirmala-Bold', r'C:\Windows\Fonts\NirmalaB.ttf'))
except Exception as e:
    print('Nirmala font not found:', e)

def generate_invitation_pdf(
    output_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\Param_Pummy_Royal_Wedding_Invitation.pdf',
    website_url='https://pushu1.github.io/param-pummy-wedding/',
    couple_img_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\wedding_couple_0.jpg',
    qr_img_path=r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\invitation_qr.png'
):
    # Ensure QR code exists
    if not os.path.exists(qr_img_path):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=2,
        )
        qr.add_data(website_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='#4A1734', back_color='#FFFDF9')
        img.save(qr_img_path)

    width, height = A4
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setTitle('Param & Pummy - Royal Wedding Invitation')
    c.setAuthor('Rodh & Bhati Family')
    c.setSubject('Official Wedding Invitation of Paramveer Singh & Manpreet Kaur')

    # Background: Royal Wine (#4A1734) with deeper plum (#291326) border
    c.setFillColor(colors.HexColor('#240D1B'))
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Inner rich gradient rectangle
    c.setFillColor(colors.HexColor('#4A1734'))
    c.roundRect(14, 14, width - 28, height - 28, 16, stroke=0, fill=1)

    # Double Antique Gold ornamental borders
    gold_outer = colors.HexColor('#D7B778')
    gold_inner = colors.HexColor('#B8934E')
    gold_bright = colors.HexColor('#F3D99F')

    c.setStrokeColor(gold_outer)
    c.setLineWidth(2)
    c.roundRect(24, 24, width - 48, height - 48, 12, stroke=1, fill=0)

    c.setStrokeColor(gold_inner)
    c.setLineWidth(0.8)
    c.roundRect(30, 30, width - 60, height - 60, 8, stroke=1, fill=0)

    # Corner decorative marks
    def draw_corner(cx, cy, flip_x, flip_y):
        c.saveState()
        c.setStrokeColor(gold_bright)
        c.setLineWidth(1.2)
        c.setFillColor(gold_bright)
        s = 18
        c.line(cx, cy, cx + flip_x * s, cy)
        c.line(cx, cy, cx, cy + flip_y * s)
        c.circle(cx + flip_x * 6, cy + flip_y * 6, 2, fill=1, stroke=0)
        c.restoreState()

    draw_corner(34, height - 34, 1, -1)
    draw_corner(width - 34, height - 34, -1, -1)
    draw_corner(34, 34, 1, 1)
    draw_corner(width - 34, 34, -1, 1)

    # Top Emblem: ੴ
    y = height - 58
    c.setFont('Nirmala-Bold', 30)
    c.setFillColor(gold_bright)
    c.drawCentredString(width / 2, y, 'ੴ')

    y -= 18
    c.setFont('Georgia-Italic', 11)
    c.setFillColor(colors.HexColor('#EBD5AB'))
    c.drawCentredString(width / 2, y, 'With the blessings of Waheguru')

    # Punjabi Gurbani verse
    y -= 20
    c.setFont('Nirmala', 10)
    c.setFillColor(colors.HexColor('#F4E3C4'))
    c.drawCentredString(width / 2, y, 'ਸਤਿਗੁਰ ਦਾਤੇ ਕਾਜ ਰਚਾਇਆ ਆਪਣੀ ਮੇਹਰ ਕਰਾਈ ॥')
    y -= 13
    c.drawCentredString(width / 2, y, 'ਦਾਸਾ ਕਾਰਜ ਆਪ ਸਵਾਰੇ ਇਹੁ ਉਸ ਦੀ ਵਡਿਆਈ ॥')

    # Parents' Invitation line
    y -= 22
    c.setFont('Georgia', 8.5)
    c.setFillColor(colors.HexColor('#D5B4C2'))
    c.drawCentredString(width / 2, y, 'Mr. Sewa Singh Rodh & Mrs. Gurmeet Kaur Rodh')
    y -= 12
    c.drawCentredString(width / 2, y, 'cordially invite you to celebrate the wedding ceremony of their beloved son')

    # Couple's Names
    y -= 28
    c.setFont('Georgia-Bold', 22)
    c.setFillColor(colors.HexColor('#FFF2DB'))
    c.drawCentredString(width / 2, y, 'Paramveer Singh (Param)')

    y -= 16
    c.setFont('Georgia-Italic', 13)
    c.setFillColor(gold_bright)
    c.drawCentredString(width / 2, y, 'weds')

    y -= 20
    c.setFont('Georgia-Bold', 22)
    c.setFillColor(colors.HexColor('#FFF2DB'))
    c.drawCentredString(width / 2, y, 'Manpreet Kaur (Pummy)')

    y -= 12
    c.setFont('Georgia-Italic', 8.5)
    c.setFillColor(colors.HexColor('#D5B4C2'))
    c.drawCentredString(width / 2, y, 'Daughter of Mr. Ranjeet Singh & Mrs. Rajvinder Kaur')

    # Date and Key Function
    y -= 18
    c.setFont('Georgia-Bold', 10.5)
    c.setFillColor(gold_bright)
    c.drawCentredString(width / 2, y, '✦ WEDNESDAY, 02 DECEMBER 2026 • 11:00 AM ✦')
    y -= 12
    c.setFont('Georgia', 9)
    c.setFillColor(colors.HexColor('#FFF7ED'))
    c.drawCentredString(width / 2, y, 'Anand Karaj & Grand Reception • Uday Vatika, Pali, Rajasthan')

    # Embedded Couple Photograph / Illustration
    # We place an elegant frame in center
    img_h = 245
    img_w = 165
    img_x = (width - img_w) / 2
    img_y = y - img_h - 12

    # Photo gold border
    c.setStrokeColor(gold_outer)
    c.setLineWidth(1.5)
    c.setFillColor(colors.HexColor('#1E0B16'))
    c.roundRect(img_x - 3, img_y - 3, img_w + 6, img_h + 6, 8, stroke=1, fill=1)

    if os.path.exists(couple_img_path):
        c.drawImage(couple_img_path, img_x, img_y, width=img_w, height=img_h, preserveAspectRatio=True, anchor='c')

    # CLICKABLE BANNER SECTION
    # Banner bounds
    banner_w = width - 110
    banner_h = 56
    banner_x = (width - banner_w) / 2
    banner_y = img_y - banner_h - 16

    # Banner Outer Shadow / Glow
    c.setStrokeColor(colors.HexColor('#F5D58C'))
    c.setLineWidth(2)
    c.setFillColor(colors.HexColor('#D4A853'))
    c.roundRect(banner_x, banner_y, banner_w, banner_h, 12, stroke=1, fill=1)

    # Banner Inner highlight gradient line
    c.setStrokeColor(colors.HexColor('#FFF3D1'))
    c.setLineWidth(0.8)
    c.roundRect(banner_x + 3, banner_y + 3, banner_w - 6, banner_h - 6, 9, stroke=1, fill=0)

    # Banner Text
    c.setFont('Georgia-Bold', 13.5)
    c.setFillColor(colors.HexColor('#2A1120'))
    c.drawCentredString(width / 2, banner_y + 31, '✨ OPEN YOUR WEDDING INVITATION ✨')

    c.setFont('Georgia-Italic', 9.5)
    c.setFillColor(colors.HexColor('#3D192F'))
    c.drawCentredString(width / 2, banner_y + 14, 'Tap here to experience our cinematic royal invitation ↗')

    # REAL PDF HYPERLINK ON BANNER!
    c.linkURL(website_url, (banner_x, banner_y, banner_x + banner_w, banner_y + banner_h), relative=0)

    # QR Code & Scan Instructions below banner
    qr_size = 62
    bottom_y = banner_y - qr_size - 14

    # QR code on left side of bottom area
    qr_x = (width / 2) - qr_size - 60
    if os.path.exists(qr_img_path):
        c.setFillColor(colors.white)
        c.roundRect(qr_x - 3, bottom_y - 3, qr_size + 6, qr_size + 6, 4, stroke=0, fill=1)
        c.drawImage(qr_img_path, qr_x, bottom_y, width=qr_size, height=qr_size)
        c.linkURL(website_url, (qr_x - 3, bottom_y - 3, qr_x + qr_size + 3, bottom_y + qr_size + 3), relative=0)

    # Scan & RSVP notes on right side
    note_x = qr_x + qr_size + 14
    c.setFont('Georgia-Bold', 8.5)
    c.setFillColor(gold_bright)
    c.drawString(note_x, bottom_y + 46, 'SCAN OR TAP TO EXPLORE')

    c.setFont('Georgia', 7.5)
    c.setFillColor(colors.HexColor('#E7D1DA'))
    c.drawString(note_x, bottom_y + 34, '• Complete wedding celebrations & timings')
    c.drawString(note_x, bottom_y + 23, '• Interactive Google Maps venue navigation')
    c.drawString(note_x, bottom_y + 12, '• Wedding photo gallery & RSVP confirmation')
    c.drawString(note_x, bottom_y + 1, 'Website: ' + website_url)
    c.linkURL(website_url, (note_x, bottom_y, note_x + 240, bottom_y + 10), relative=0)

    # Footer Acknowledgement & Contact
    c.setFont('Georgia', 7)
    c.setFillColor(colors.HexColor('#C8A4B4'))
    footer_text = 'With best compliments from Rodh & Bhati Family • Enquiries: 9829312488 · 9079012387'
    c.drawCentredString(width / 2, 38, footer_text)

    c.save()
    print(f'Successfully generated PDF at: {output_path}')
    return output_path

if __name__ == '__main__':
    generate_invitation_pdf()
