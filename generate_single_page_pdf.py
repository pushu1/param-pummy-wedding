import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Georgia fonts for opulent classical serif typography
fonts_dir = r'C:\Windows\Fonts'
try:
    pdfmetrics.registerFont(TTFont('Georgia', os.path.join(fonts_dir, 'georgia.ttf')))
    pdfmetrics.registerFont(TTFont('Georgia-Bold', os.path.join(fonts_dir, 'georgiab.ttf')))
    pdfmetrics.registerFont(TTFont('Georgia-Italic', os.path.join(fonts_dir, 'georgiai.ttf')))
    pdfmetrics.registerFont(TTFont('Georgia-BoldItalic', os.path.join(fonts_dir, 'georgiaz.ttf')))
except Exception as e:
    print('Error registering Georgia fonts:', e)

def draw_diamond(c, cx, cy, rx, ry, color):
    c.saveState()
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(cx, cy + ry)
    p.lineTo(cx + rx, cy)
    p.lineTo(cx, cy - ry)
    p.lineTo(cx - rx, cy)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()

def build_royal_wedding_pdf():
    pdf_path = r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\Kuldeep_Teena_Royal_Wedding_Invitation.pdf'
    assets_dir = r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets'

    page_w, page_h = A4
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.setTitle('Kuldeep & Teena — Royal Wedding Invitation')
    c.setAuthor('Upadhyay Family, Pali')
    c.setSubject('Official Royal Wedding Invitation of Chiranjeev Kuldeep & Sou. Ka. Teena')

    # Color Palette: Royal Marwari / Upadhyay Aesthetic
    c_maroon = colors.HexColor('#54171E')       # Royal Deep Maroon
    c_maroon_dim = colors.HexColor('#75222B')   # Soft Maroon
    c_gold = colors.HexColor('#B88E4F')         # Antique Royal Gold
    c_gold_light = colors.HexColor('#D9B372')   # Shimmering Gold
    c_gold_bright = colors.HexColor('#F5D796')  # Champagne Gold
    c_ivory_bg = colors.HexColor('#FAF6F0')     # Warm Ivory Parchment
    c_card_bg = colors.HexColor('#FFFFFF')      # Pure Card Base
    c_ink_dark = colors.HexColor('#2E2018')     # Deep Espresso Ink
    c_ink_muted = colors.HexColor('#6B5547')    # Muted Warm Brown
    c_line_soft = colors.HexColor('#E5D7C5')    # Soft separator

    # 1. Base Ivory Background
    c.setFillColor(c_ivory_bg)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    # 2. Draw Botanical Garden Gateway Background if available
    bg_card = os.path.join(assets_dir, 'pinterest_card_bg.jpg')
    if os.path.exists(bg_card):
        c.drawImage(bg_card, 0, 0, width=page_w, height=page_h, preserveAspectRatio=False)

    # 3. Soft Ivory Translucent Overlay to ensure crystal-clear text readability
    c.setFillColor(c_ivory_bg, alpha=0.92)
    c.roundRect(18, 18, page_w - 36, page_h - 36, 14, fill=1, stroke=0)

    # 4. Antique Gold Royal Double Border
    c.setFillColor(c_gold, alpha=1.0)
    c.setStrokeColor(c_gold)
    c.setLineWidth(1.8)
    c.roundRect(22, 22, page_w - 44, page_h - 44, 12, fill=0, stroke=1)

    c.setStrokeColor(c_gold_light)
    c.setLineWidth(0.8)
    c.roundRect(27, 27, page_w - 54, page_h - 54, 9, fill=0, stroke=1)

    # Ornate Corner Accents
    def draw_corner(cx, cy, fx, fy):
        c.saveState()
        c.setStrokeColor(c_gold)
        c.setLineWidth(1.2)
        c.setFillColor(c_maroon)
        s = 20
        c.line(cx, cy, cx + fx * s, cy)
        c.line(cx, cy, cx, cy + fy * s)
        c.circle(cx + fx * 6, cy + fy * 6, 2.2, fill=1, stroke=0)
        c.circle(cx + fx * 12, cy + fy * 3, 1.4, fill=1, stroke=0)
        c.circle(cx + fx * 3, cy + fy * 12, 1.4, fill=1, stroke=0)
        c.restoreState()

    draw_corner(32, page_h - 32, 1, -1)
    draw_corner(page_w - 32, page_h - 32, -1, -1)
    draw_corner(32, 32, 1, 1)
    draw_corner(page_w - 32, 32, -1, 1)

    mid_x = page_w / 2

    # =========================================================================
    # HEADER SECTION: SACRED INVOCATION & LORD GANESHA EMBLEM
    # =========================================================================
    ganesha_emblem = os.path.join(assets_dir, 'gold_ganesha_emblem.png')
    emblem_y = page_h - 70
    if os.path.exists(ganesha_emblem):
        es = 38
        c.drawImage(ganesha_emblem, mid_x - es/2, emblem_y, width=es, height=es, mask='auto')
        y_text = emblem_y - 13
    else:
        y_text = page_h - 48

    c.setFillColor(c_maroon)
    c.setFont("Georgia-Bold", 10.5)
    c.drawCentredString(mid_x, y_text, "SHRI GANESHAYA NAMAH")
    draw_diamond(c, mid_x - 105, y_text + 3.5, 4, 4, c_gold)
    draw_diamond(c, mid_x + 105, y_text + 3.5, 4, 4, c_gold)

    y_text -= 13
    c.setFillColor(c_gold)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(mid_x, y_text, "WITH THE DIVINE BLESSINGS OF LORD GANESHA")

    y_text -= 21
    c.setFillColor(c_maroon)
    c.setFont("Georgia-Bold", 16)
    c.drawCentredString(mid_x, y_text, "UPADHYAY FAMILY CORDIALLY INVITES YOU")

    y_text -= 13
    c.setFillColor(c_ink_muted)
    c.setFont("Georgia-Italic", 9.2)
    c.drawCentredString(mid_x, y_text, "to celebrate the auspicious wedding ceremony of their beloved son and daughter")

    # Flourish Divider with center diamond & side dots
    y_text -= 8
    c.setStrokeColor(c_gold_light)
    c.setLineWidth(0.7)
    fl_w = 75
    c.line(mid_x - fl_w - 20, y_text, mid_x - 14, y_text)
    c.line(mid_x + 14, y_text, mid_x + fl_w + 20, y_text)
    draw_diamond(c, mid_x, y_text, 4.5, 4.5, c_gold)
    c.setFillColor(c_maroon)
    c.circle(mid_x - 8, y_text, 1.3, fill=1, stroke=0)
    c.circle(mid_x + 8, y_text, 1.3, fill=1, stroke=0)

    # =========================================================================
    # COUPLE NAMES & WEDDING DATE (PRIMARY VISUAL EMPHASIS)
    # =========================================================================
    y_couple = y_text - 24
    c.setFillColor(c_maroon)
    c.setFont("Georgia-BoldItalic", 27)
    c.drawCentredString(mid_x, y_couple, "Kuldeep   &   Teena")

    y_couple -= 15
    c.setFillColor(c_gold)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawCentredString(mid_x, y_couple, "K U L D E E P   W E D S   T E E N A")

    # Elegant Date Pill Badge
    y_couple -= 22
    badge_w, badge_h = 280, 20
    badge_x = (page_w - badge_w) / 2
    c.setFillColor(c_maroon)
    c.roundRect(badge_x, y_couple, badge_w, badge_h, 10, fill=1, stroke=0)
    c.setFillColor(c_gold_bright)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(mid_x, y_couple + 5.5, "FRIDAY  •  11 DECEMBER 2026  •  PALI (RAJ.)")

    # =========================================================================
    # COUPLE PHOTOGRAPHS & PARENTAGE SHOWCASE
    # =========================================================================
    groom_img = os.path.join(assets_dir, 'groom_photo.jpg')
    bride_img = os.path.join(assets_dir, 'bride_photo.jpg')

    pw = 114
    ph = 144
    gap = 72
    photo_y = y_couple - 156

    # Left: Groom Photo
    left_x = mid_x - pw - (gap / 2)
    if os.path.exists(groom_img):
        c.drawImage(groom_img, left_x, photo_y, width=pw, height=ph, preserveAspectRatio=True)
        c.setStrokeColor(c_gold)
        c.setLineWidth(1.6)
        c.rect(left_x, photo_y, pw, ph, fill=0, stroke=1)
        c.setStrokeColor(c_gold_light)
        c.setLineWidth(0.6)
        c.rect(left_x + 2, photo_y + 2, pw - 4, ph - 4, fill=0, stroke=1)

    # Right: Bride Photo
    right_x = mid_x + (gap / 2)
    if os.path.exists(bride_img):
        c.drawImage(bride_img, right_x, photo_y, width=pw, height=ph, preserveAspectRatio=True)
        c.setStrokeColor(c_gold)
        c.setLineWidth(1.6)
        c.rect(right_x, photo_y, pw, ph, fill=0, stroke=1)
        c.setStrokeColor(c_gold_light)
        c.setLineWidth(0.6)
        c.rect(right_x + 2, photo_y + 2, pw - 4, ph - 4, fill=0, stroke=1)

    # Center Wax Seal between photos
    seal_img = os.path.join(assets_dir, 'kt_wax_seal_final.png')
    seal_y = photo_y + (ph / 2)
    if os.path.exists(seal_img):
        ss = 46
        c.drawImage(seal_img, mid_x - ss/2, seal_y - ss/2, width=ss, height=ss, mask='auto')

    # Groom Info Under Photo
    g_info_y = photo_y - 13
    c.setFillColor(c_maroon)
    c.setFont("Georgia-Bold", 10.5)
    c.drawCentredString(left_x + pw/2, g_info_y, "Chiranjeev Kuldeep")
    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 7.8)
    c.drawCentredString(left_x + pw/2, g_info_y - 11, "Son of Smt. Chandra Devi &")
    c.setFillColor(c_ink_dark)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawCentredString(left_x + pw/2, g_info_y - 21, "Shri Jasrajji Upadhyay")

    # Bride Info Under Photo
    b_info_y = photo_y - 13
    c.setFillColor(c_maroon)
    c.setFont("Georgia-Bold", 10.5)
    c.drawCentredString(right_x + pw/2, b_info_y, "Sou. Ka. Teena")
    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 7.8)
    c.drawCentredString(right_x + pw/2, b_info_y - 11, "Daughter of Smt. Manju Devi &")
    c.setFillColor(c_ink_dark)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawCentredString(right_x + pw/2, b_info_y - 21, "Shri Ramgopalji Vajpayee")
    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 6.8)
    c.drawCentredString(right_x + pw/2, b_info_y - 30, "Granddaughter of Late Smt. Janaki Devi & Late Shri Chhogalalji Vajpayee")

    # =========================================================================
    # TWO-COLUMN FAMILY LINEAGE, ANCESTRAL BLESSINGS & HOSTS
    # =========================================================================
    box_top = g_info_y - 39
    box_h = 108
    col_w = (page_w - 74) / 2
    col1_x = 34
    col2_x = col1_x + col_w + 6

    # Column 1 Box (Left): Ancestral Blessings & Sons-in-Law (Janwai Paksh)
    c.setFillColor(c_card_bg)
    c.setStrokeColor(c_gold)
    c.setLineWidth(0.8)
    c.roundRect(col1_x, box_top - box_h, col_w, box_h, 6, fill=1, stroke=1)

    c.setFillColor(c_maroon)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawCentredString(col1_x + col_w/2, box_top - 12, "WITH ETERNAL ANCESTRAL BLESSINGS")

    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 6.9)
    c.drawCentredString(col1_x + col_w/2, box_top - 23, "Late Smt. Jamna Devi & Late Shri Harchandji Upadhyay (Great-Grandson)")
    c.drawCentredString(col1_x + col_w/2, box_top - 33, "Late Smt. Pepi Devi & Late Shri Champalalji Upadhyay (Grandson)")

    # Divider line
    c.setStrokeColor(c_line_soft)
    c.setLineWidth(0.5)
    c.line(col1_x + 12, box_top - 40, col1_x + col_w - 12, box_top - 40)

    # Janwai Paksh
    c.setFillColor(c_maroon)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawCentredString(col1_x + col_w/2, box_top - 50, "SONS-IN-LAW & FAMILY (JANWAI PAKSH)")

    c.setFillColor(c_ink_dark)
    c.setFont("Helvetica", 7.1)
    c.drawCentredString(col1_x + col_w/2, box_top - 62, "Smt. Santoshdevi & Shri Mangilalji Upadhyay")
    c.drawCentredString(col1_x + col_w/2, box_top - 73, "Smt. Hemlata & Shri Gajendrakumarji Upadhyay")
    c.drawCentredString(col1_x + col_w/2, box_top - 84, "Smt. Aishwarya & Shri Khushwantji Paiswal")
    c.setFillColor(c_maroon_dim)
    c.setFont("Helvetica-Bold", 7.1)
    c.drawCentredString(col1_x + col_w/2, box_top - 96, "Pushpendra  •  Premprakash  •  Bhumika")

    # Column 2 Box (Right): Solicitous Hosts & Contact
    c.setFillColor(c_card_bg)
    c.setStrokeColor(c_gold)
    c.setLineWidth(0.8)
    c.roundRect(col2_x, box_top - box_h, col_w, box_h, 6, fill=1, stroke=1)

    c.setFillColor(c_maroon)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawCentredString(col2_x + col_w/2, box_top - 12, "SOLICITOUS HOSTS (UTTARAKANKSHI)")

    c.setFillColor(c_maroon)
    c.setFont("Georgia-Bold", 9.8)
    c.drawCentredString(col2_x + col_w/2, box_top - 25, "Jasraj Mangilal Upadhyay")

    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 7.1)
    c.drawCentredString(col2_x + col_w/2, box_top - 36, "(Son of Late Shri Champalalji Upadhyay)")
    c.drawCentredString(col2_x + col_w/2, box_top - 47, "255, 256, Ram Nagar, 3rd Gali, Pali (Rajasthan)")

    c.setFillColor(c_gold)
    c.setFont("Helvetica-Bold", 7.4)
    c.drawCentredString(col2_x + col_w/2, box_top - 59, "Tel: +91 94610 61236   •   +91 98879 97822")

    # Divider line
    c.setStrokeColor(c_line_soft)
    c.line(col2_x + 12, box_top - 66, col2_x + col_w - 12, box_top - 66)

    c.setFillColor(c_maroon)
    c.setFont("Helvetica-Bold", 7.6)
    c.drawCentredString(col2_x + col_w/2, box_top - 76, "BRIDE'S RESPECTED FAMILY (VAJPAYEE FAMILY)")
    c.setFillColor(c_ink_dark)
    c.setFont("Helvetica", 7.1)
    c.drawCentredString(col2_x + col_w/2, box_top - 87, "Smt. Manju Devi & Shri Ramgopalji Vajpayee (Parents)")
    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 6.8)
    c.drawCentredString(col2_x + col_w/2, box_top - 98, "Late Smt. Janaki Devi & Late Shri Chhogalalji Vajpayee (Grandparents)")

    # =========================================================================
    # RECEPTION & VENUE BOX WITH GOOGLE MAPS QR CODE
    # =========================================================================
    rec_top = box_top - box_h - 10
    rec_h = 100
    rec_w = page_w - 68
    rec_x = 34

    c.setFillColor(c_card_bg)
    c.setStrokeColor(c_gold)
    c.setLineWidth(1.1)
    c.roundRect(rec_x, rec_top - rec_h, rec_w, rec_h, 8, fill=1, stroke=1)

    # QR Code on Left of Reception Box
    qr_img = os.path.join(assets_dir, 'venue_maps_qr.png')
    qr_s = 76
    qr_x = rec_x + 14
    qr_y = rec_top - rec_h + 12

    if os.path.exists(qr_img):
        c.drawImage(qr_img, qr_x, qr_y, width=qr_s, height=qr_s, preserveAspectRatio=True)
        c.setStrokeColor(c_gold)
        c.setLineWidth(0.6)
        c.rect(qr_x, qr_y, qr_s, qr_s, fill=0, stroke=1)

    # Reception Details on Right of QR Code
    info_x = qr_x + qr_s + 16
    c.setFillColor(c_maroon)
    c.setFont("Georgia-Bold", 11)
    c.drawString(info_x, rec_top - 18, "WEDDING RECEPTION BANQUET  (AASHIRVAAD & PREETIBHOJ)")

    c.setFillColor(c_gold)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(info_x, rec_top - 32, "SUNDAY, 13 DECEMBER 2026   •   06:00 PM ONWARDS")

    c.setFillColor(c_ink_dark)
    c.setFont("Georgia-Bold", 9.5)
    c.drawString(info_x, rec_top - 46, "Venue: Jain Bagbera Dadawadi, Venkatesh Marg, Pali (Rajasthan)")

    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 7.5)
    c.drawString(info_x, rec_top - 58, "Panigrahan Sanskar (Auspicious Vows): Friday, 11 Dec 2026 • 02:00 AM Midnight")

    # Clickable Google Maps Pill Button
    btn_w = 210
    btn_h = 20
    btn_y = rec_top - rec_h + 12
    c.setFillColor(c_maroon)
    c.roundRect(info_x, btn_y, btn_w, btn_h, 10, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 7.8)
    c.drawCentredString(info_x + btn_w/2, btn_y + 6, "Click to Open Location in Google Maps")
    draw_diamond(c, info_x + 16, btn_y + 10, 3, 3, c_gold_bright)
    draw_diamond(c, info_x + btn_w - 16, btn_y + 10, 3, 3, c_gold_bright)
    c.linkURL("https://maps.app.goo.gl/hPi6DXWJZEpUG5Vm9", (info_x, btn_y, info_x + btn_w, btn_y + btn_h), relative=0)

    # QR Scan Hint below QR
    c.setFillColor(c_ink_muted)
    c.setFont("Helvetica", 6.5)
    c.drawCentredString(qr_x + qr_s/2, qr_y - 8, "Scan QR with Camera")

    # =========================================================================
    # CLICKABLE INTERACTIVE DIGITAL INVITATION BANNER (BOTTOM)
    # =========================================================================
    ban_y = 34
    ban_h = 32
    ban_w = page_w - 68
    ban_x = 34

    c.setFillColor(c_maroon)
    c.roundRect(ban_x, ban_y, ban_w, ban_h, 16, fill=1, stroke=0)

    # Gold accent inner border
    c.setStrokeColor(c_gold_light)
    c.setLineWidth(0.8)
    c.roundRect(ban_x + 2, ban_y + 2, ban_w - 4, ban_h - 4, 14, fill=0, stroke=1)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawCentredString(mid_x, ban_y + 17, "CLICK HERE TO OPEN INTERACTIVE DIGITAL INVITATION & MUSIC")
    draw_diamond(c, ban_x + 26, ban_y + 16, 4, 4, c_gold_bright)
    draw_diamond(c, ban_x + ban_w - 26, ban_y + 16, 4, 4, c_gold_bright)

    c.setFillColor(c_gold_bright)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(mid_x, ban_y + 6.5, "Experience the 3D royal opening envelope, photo gallery, calendar & wishes")

    c.linkURL("https://pushu1.github.io/param-pummy-wedding/", (ban_x, ban_y, ban_x + ban_w, ban_y + ban_h), relative=0)

    # STRICTLY ONLY ONE PAGE
    c.save()
    print("Royal Single-Page Wedding PDF created successfully!")

if __name__ == '__main__':
    build_royal_wedding_pdf()
