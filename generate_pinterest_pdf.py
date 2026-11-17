import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

pdf_path = r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets\Kuldeep_Teena_Royal_Wedding_Invitation.pdf'
assets_dir = r'C:\Users\Hp\.gemini\antigravity\scratch\param-pummy-wedding\assets'

page_w, page_h = A4

c = canvas.Canvas(pdf_path, pagesize=A4)
c.setTitle('Kuldeep & Teena — Royal Wedding Invitation')
c.setAuthor('Upadhyay & Vajpayee Family')
c.setSubject('Official Royal Wedding Invitation of Chiranjeev Kuldeep & Sou. Ka. Teena')

# ===================================================================
# PAGE 1: PINTEREST STYLE WEDDING INVITATION COVER
# ===================================================================

# 1. Background Parchment Color
c.setFillColor(colors.HexColor('#FAF6F0'))
c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

# 2. Draw Golden Gate & Landscape
bg_card = os.path.join(assets_dir, 'pinterest_card_bg.jpg')
if os.path.exists(bg_card):
    c.drawImage(bg_card, 0, 0, width=page_w, height=page_h, preserveAspectRatio=False)

# Semi-transparent parchment plate
c.setFillColor(colors.HexColor('#FAF6F0'), alpha=0.90)
c.roundRect(32, 40, page_w - 64, page_h - 80, 16, fill=1, stroke=0)
c.setFillColor(colors.HexColor('#B88E4F'), alpha=0.45)
c.setLineWidth(1)
c.roundRect(38, 46, page_w - 76, page_h - 92, 14, fill=0, stroke=1)

# Top Sacred Invocation
c.setFillColor(colors.HexColor('#7E5B32'), alpha=1.0)
c.setFont("Helvetica-Bold", 10)
c.drawCentredString(page_w / 2, page_h - 75, "BY THE DIVINE BLESSINGS OF LORD GANESHA")

# "SAVE THE DATE"
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-Bold", 24)
c.drawCentredString(page_w / 2, page_h - 105, "SAVE THE DATE")

# "FOR THE WEDDING OF"
c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica", 10.5)
c.drawCentredString(page_w / 2, page_h - 125, "FOR THE WEDDING OF")

# Couple Names in Luxury English Serif
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-BoldItalic", 34)
c.drawCentredString(page_w / 2, page_h - 168, "Kuldeep   &   Teena")

# Prominent "KULDEEP WEDS TEENA"
c.setFillColor(colors.HexColor('#9E7A44'))
c.setFont("Helvetica-Bold", 13.5)
c.drawCentredString(page_w / 2, page_h - 198, "KULDEEP  WEDS  TEENA")

# Couple Photographs
groom_img = os.path.join(assets_dir, 'groom_photo.jpg')
bride_img = os.path.join(assets_dir, 'bride_photo.jpg')

photo_w = 126
photo_h = 168
gap = 62
center_x = page_w / 2

# Left Photo: Groom
left_x = center_x - photo_w - (gap / 2)
photo_y = page_h - 395

if os.path.exists(groom_img):
    c.drawImage(groom_img, left_x, photo_y, width=photo_w, height=photo_h, preserveAspectRatio=True)
    c.setStrokeColor(colors.HexColor('#B88E4F'))
    c.setLineWidth(1.8)
    c.rect(left_x, photo_y, photo_w, photo_h, fill=0, stroke=1)

# Groom Badge
c.setFillColor(colors.HexColor('#F7E9CE'))
c.roundRect(left_x + (photo_w - 90)/2, photo_y - 20, 90, 16, 8, fill=1, stroke=0)
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Helvetica-Bold", 9)
c.drawCentredString(left_x + photo_w/2, photo_y - 16, "GROOM • KULDEEP")

# Center Union Symbol (Spacious and cleanly centered)
c.setFillColor(colors.HexColor('#9E7A44'))
c.setFont("Times-BoldItalic", 15)
c.drawCentredString(center_x, photo_y + photo_h/2 + 6, "WEDS")
c.setFont("Helvetica", 14)
c.drawCentredString(center_x, photo_y + photo_h/2 - 14, "❦")

# Right Photo: Bride
right_x = center_x + (gap / 2)
if os.path.exists(bride_img):
    c.drawImage(bride_img, right_x, photo_y, width=photo_w, height=photo_h, preserveAspectRatio=True)
    c.setStrokeColor(colors.HexColor('#B88E4F'))
    c.setLineWidth(1.8)
    c.rect(right_x, photo_y, photo_w, photo_h, fill=0, stroke=1)

# Bride Badge
c.setFillColor(colors.HexColor('#F7E9CE'))
c.roundRect(right_x + (photo_w - 90)/2, photo_y - 20, 90, 16, 8, fill=1, stroke=0)
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Helvetica-Bold", 9)
c.drawCentredString(right_x + photo_w/2, photo_y - 16, "BRIDE • TEENA")

# Date Presentation Badge
c.setFillColor(colors.HexColor('#FFFFFF'))
c.setStrokeColor(colors.HexColor('#B88E4F'))
c.setLineWidth(1)
c.roundRect(center_x - 140, photo_y - 75, 280, 36, 18, fill=1, stroke=1)

c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-Bold", 14)
c.drawCentredString(center_x, photo_y - 62, "FRIDAY   •   11 DECEMBER 2026")

c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica-Bold", 9.5)
c.drawCentredString(center_x, photo_y - 95, "AT 07:30 AM ONWARDS")

c.setFont("Helvetica", 10)
c.drawCentredString(center_x, photo_y - 115, "Jain Bagbera Dadawadi, Venkatesh Marg, Pali (Rajasthan)")

# Clickable Banner at bottom
banner_y = 65
banner_h = 38
c.setFillColor(colors.HexColor('#5C4024'))
c.roundRect(60, banner_y, page_w - 120, banner_h, 19, fill=1, stroke=0)

c.setFillColor(colors.HexColor('#FFFFFF'))
c.setFont("Helvetica-Bold", 10.5)
c.drawCentredString(page_w / 2, banner_y + 14, "✦  CLICK HERE TO OPEN INTERACTIVE INVITATION & MUSIC  ✦")

c.linkURL("https://pushu1.github.io/param-pummy-wedding/", (60, banner_y, page_w - 60, banner_y + banner_h), relative=0)

c.showPage()

# ===================================================================
# PAGE 2: EVENT AGENDA TIMELINE, GOOGLE MAPS QR & COMPLETE FAMILY GRATITUDE
# ===================================================================

c.setFillColor(colors.HexColor('#FAF6F0'))
c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

# Outer decorative border
c.setStrokeColor(colors.HexColor('#B88E4F'))
c.setLineWidth(1)
c.rect(28, 28, page_w - 56, page_h - 56, fill=0, stroke=1)
c.rect(32, 32, page_w - 64, page_h - 64, fill=0, stroke=1)

# Header
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-Bold", 19)
c.drawCentredString(page_w / 2, page_h - 60, "EVENT AGENDA & WEDDING CEREMONIES")

c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica-Bold", 9)
c.drawCentredString(page_w / 2, page_h - 75, "CHIRANJEEV KULDEEP   WEDS   SOU. KA. TEENA")

# 8 Auspicious Ceremonies matching original card
events = [
    ("Ghritpaan Ceremony (Dhupawan)", "Saturday, 05 Dec 2026", "07:30 AM", "Family Residence • 255-256 Ram Nagar, Pali"),
    ("Vinayak Sthapana", "Monday, 07 Dec 2026", "09:15 AM", "Family Residence • Ram Nagar, Pali"),
    ("Mayra Ceremony (Maternal Welcome)", "Thursday, 10 Dec 2026", "10:00 AM", "Family Residence • Ram Nagar, Pali"),
    ("Janeu Sanskar (Sacred Thread Ceremony)", "Thursday, 10 Dec 2026", "04:00 PM", "Family Residence • Ram Nagar, Pali"),
    ("Bandoli Procession & Sangeet", "Thursday, 10 Dec 2026", "07:00 PM", "Joyous Musical Procession through Pali"),
    ("Baraat Prasthan (Groom's Departure)", "Friday, 11 Dec 2026", "07:30 AM", "Royal Procession from Ram Nagar to Venue"),
    ("Panigrahan Sanskar (Wedding Vows)", "Friday, 11 Dec 2026", "02:00 AM Midnight", "Sacred Mandap & Saat Pheras (Auspicious Mahurat)"),
    ("Aashirvaad Samaroh & Preetibhoj", "Sunday, 13 Dec 2026", "06:00 PM onwards", "Reception Banquet • Jain Bagbera Dadawadi, Pali")
]

start_y = page_h - 98
card_h = 33
spacing = 38

for i, (title, dt, tm, loc) in enumerate(events):
    ey = start_y - (i * spacing)
    
    c.setFillColor(colors.HexColor('#FFFFFF'))
    c.setStrokeColor(colors.HexColor('#E4D4BE'))
    c.setLineWidth(0.8)
    c.roundRect(45, ey - card_h + 6, page_w - 90, card_h, 5, fill=1, stroke=1)
    
    # Number badge
    c.setFillColor(colors.HexColor('#F7E9CE'))
    c.circle(63, ey - card_h/2 + 6, 11, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#5C4024'))
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(63, ey - card_h/2 + 3.5, f"{i+1:02d}")
    
    # Event title
    c.setFillColor(colors.HexColor('#5C4024'))
    c.setFont("Times-Bold", 9.8)
    c.drawString(82, ey - 9, title)
    
    # Event location
    c.setFillColor(colors.HexColor('#736050'))
    c.setFont("Helvetica", 7.8)
    c.drawString(82, ey - 20, loc)
    
    # Date & Time on right
    c.setFillColor(colors.HexColor('#856133'))
    c.setFont("Helvetica-Bold", 8.2)
    c.drawRightString(page_w - 55, ey - 9, dt)
    
    c.setFillColor(colors.HexColor('#B88E4F'))
    c.setFont("Helvetica", 7.8)
    c.drawRightString(page_w - 55, ey - 20, tm)

lower_y = start_y - (len(events) * spacing) - 10
bottom_box_h = 245

# -------------------------------------------------------------
# Left Box: Google Maps Location & Directions
# -------------------------------------------------------------
map_box_w = 205
c.setFillColor(colors.HexColor('#FFFFFF'))
c.setStrokeColor(colors.HexColor('#B88E4F'))
c.setLineWidth(1)
c.roundRect(45, lower_y - bottom_box_h, map_box_w, bottom_box_h, 8, fill=1, stroke=1)

c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-Bold", 11)
c.drawCentredString(45 + map_box_w/2, lower_y - 18, "VENUE & DIRECTIONS")

qr_img = os.path.join(assets_dir, 'venue_maps_qr.png')
if os.path.exists(qr_img):
    c.drawImage(qr_img, 45 + (map_box_w - 110)/2, lower_y - 142, width=110, height=110, preserveAspectRatio=True)

c.setFillColor(colors.HexColor('#736050'))
c.setFont("Helvetica", 7.8)
c.drawCentredString(45 + map_box_w/2, lower_y - 156, "Scan QR with phone camera for directions")

# Venue Details
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Helvetica-Bold", 8)
c.drawCentredString(45 + map_box_w/2, lower_y - 172, "Jain Bagbera Dadawadi")
c.setFillColor(colors.HexColor('#736050'))
c.setFont("Helvetica", 7.5)
c.drawCentredString(45 + map_box_w/2, lower_y - 183, "Venkatesh Marg, Pali (Rajasthan)")

map_btn_y = lower_y - 230
c.setFillColor(colors.HexColor('#5C4024'))
c.roundRect(55, map_btn_y, map_box_w - 20, 28, 14, fill=1, stroke=0)
c.setFillColor(colors.HexColor('#FFFFFF'))
c.setFont("Helvetica-Bold", 9)
c.drawCentredString(45 + map_box_w/2, map_btn_y + 10, "✦ Click for Google Maps ✦")
c.linkURL("https://maps.app.goo.gl/hPi6DXWJZEpUG5Vm9", (55, map_btn_y, 55 + map_box_w - 20, map_btn_y + 28), relative=0)

# -------------------------------------------------------------
# Right Box: Solicitous Hosts, Janwai Paksh & Family Gratitude
# -------------------------------------------------------------
grat_x = 45 + map_box_w + 14
grat_w = page_w - 45 - grat_x

c.setFillColor(colors.HexColor('#FFFFFF'))
c.setStrokeColor(colors.HexColor('#B88E4F'))
c.setLineWidth(1)
c.roundRect(grat_x, lower_y - bottom_box_h, grat_w, bottom_box_h, 8, fill=1, stroke=1)

# Header
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-Bold", 10.5)
c.drawCentredString(grat_x + grat_w/2, lower_y - 16, "OUR GRATITUDE & SOLICITOUS HOSTS")

# Solicitous Host (Uttarakankshi)
c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica-Bold", 7.5)
c.drawCentredString(grat_x + grat_w/2, lower_y - 28, "SOLICITOUS HOSTS (UTTARAKANKSHI)")

c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-Bold", 10)
c.drawCentredString(grat_x + grat_w/2, lower_y - 41, "Jasraj Mangilal Upadhyay")

c.setFillColor(colors.HexColor('#736050'))
c.setFont("Helvetica", 7.5)
c.drawCentredString(grat_x + grat_w/2, lower_y - 52, "(Son of Late Shri Champalalji Upadhyay)")
c.drawCentredString(grat_x + grat_w/2, lower_y - 63, "255, 256, Ram Nagar, 3rd Gali, Pali (Rajasthan)")

c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica-Bold", 7.5)
c.drawCentredString(grat_x + grat_w/2, lower_y - 75, "Phone: +91 94610 61236  •  +91 98879 97822")

# Divider line
c.setStrokeColor(colors.HexColor('#E4D4BE'))
c.line(grat_x + 12, lower_y - 83, grat_x + grat_w - 12, lower_y - 83)

# Janwai Paksh (Sons-in-law & Daughters' Family from uploaded screenshot)
c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica-Bold", 7.5)
c.drawCentredString(grat_x + grat_w/2, lower_y - 94, "SONS-IN-LAW & FAMILY (JANWAI PAKSH)")

c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Helvetica", 7.3)
c.drawCentredString(grat_x + grat_w/2, lower_y - 106, "Smt. Santoshdevi & Shri Mangilalji Upadhyay")
c.drawCentredString(grat_x + grat_w/2, lower_y - 117, "Smt. Hemlata & Shri Gajendrakumarji Upadhyay")
c.drawCentredString(grat_x + grat_w/2, lower_y - 128, "Smt. Aishwarya & Shri Khushwantji Paiswal")

c.setFillColor(colors.HexColor('#736050'))
c.setFont("Helvetica-Bold", 7.3)
c.drawCentredString(grat_x + grat_w/2, lower_y - 139, "Pushpendra  •  Premprakash  •  Bhumika")

# Divider line
c.setStrokeColor(colors.HexColor('#E4D4BE'))
c.line(grat_x + 12, lower_y - 146, grat_x + grat_w - 12, lower_y - 146)

# Bride's Respected Family
c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica-Bold", 7.5)
c.drawCentredString(grat_x + grat_w/2, lower_y - 157, "BRIDE'S RESPECTED FAMILY (VAJPAYEE FAMILY)")

c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Helvetica", 7.3)
c.drawCentredString(grat_x + grat_w/2, lower_y - 169, "Daughter of Smt. Manju Devi & Shri Ramgopalji Vajpayee")
c.setFillColor(colors.HexColor('#736050'))
c.setFont("Helvetica", 7.1)
c.drawCentredString(grat_x + grat_w/2, lower_y - 180, "Granddaughter of Late Smt. Janaki Devi & Late Shri Chhogalalji Vajpayee")

# Divider line
c.setStrokeColor(colors.HexColor('#E4D4BE'))
c.line(grat_x + 12, lower_y - 187, grat_x + grat_w - 12, lower_y - 187)

# Ancestral Blessings
c.setFillColor(colors.HexColor('#856133'))
c.setFont("Helvetica-Bold", 7.2)
c.drawCentredString(grat_x + grat_w/2, lower_y - 197, "WITH ETERNAL ANCESTRAL BLESSINGS")

c.setFillColor(colors.HexColor('#736050'))
c.setFont("Helvetica", 6.9)
c.drawCentredString(grat_x + grat_w/2, lower_y - 208, "Late Smt. Jamna Devi & Late Shri Harchandji Upadhyay (Great-Grandson)")
c.drawCentredString(grat_x + grat_w/2, lower_y - 219, "Late Smt. Pepi Devi & Late Shri Champalalji Upadhyay (Grandson)")

# Solicitous Invitation closing
c.setFillColor(colors.HexColor('#5C4024'))
c.setFont("Times-Italic", 7.5)
c.drawCentredString(grat_x + grat_w/2, lower_y - 233, "Cordially invited by Smt. Chandra Devi & Shri Jasrajji Upadhyay")

c.save()
print('Successfully generated complete Pinterest-style wedding PDF!')
