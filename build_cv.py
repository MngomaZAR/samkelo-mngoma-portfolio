"""Build the public, text-based CV. No private source documents are bundled."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'Samkelo-Mngoma-CV.pdf'
GREEN = colors.HexColor('#126b5e')
INK = colors.HexColor('#172522')
MUTED = colors.HexColor('#52615e')
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=25, leading=29, textColor=INK, spaceAfter=6),
    'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=11, leading=15, textColor=GREEN, spaceAfter=7),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=13, textColor=MUTED, spaceAfter=6),
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=GREEN, spaceBefore=14, spaceAfter=8),
    'job': ParagraphStyle('job', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=INK, spaceAfter=3),
    'meta': ParagraphStyle('meta', fontName='Helvetica', fontSize=9, leading=12, textColor=MUTED, spaceAfter=5),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, leading=14, textColor=INK, spaceAfter=6),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=9.5, leading=14, textColor=INK, leftIndent=10, firstLineIndent=-8, spaceAfter=4),
}
story = []
def p(text, style='body'):
    return Paragraph(text, styles[style])
def add(text, style='body'):
    story.append(p(text, style))
def section(text):
    add(text.upper(), 'section')
def job(title, company, dates, bullets):
    story.append(KeepTogether([p(title, 'job'), p(f'{company} | {dates}', 'meta')] + [p('- ' + text, 'bullet') for text in bullets]))
def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#d7e1de'))
    canvas.line(42, 39, A4[0]-42, 39)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(42, 26, 'Samkelo Mngoma | smngoma22@gmail.com | Updated October 2026')
    canvas.drawRightString(A4[0]-42, 26, f'{doc.page} / 2')
    canvas.restoreState()

add('SAMKELO SITHEMBISO MNGOMA', 'name')
add('SOFTWARE &amp; DATA ENGINEERING | CLOUD DELIVERY | TECHNICAL OPERATIONS', 'role')
add('South Africa | +27 66 146 6960 | <link href="mailto:smngoma22@gmail.com">smngoma22@gmail.com</link>', 'contact')
add('<link href="https://mngomazar.github.io/samkelo-mngoma-portfolio/">Portfolio: mngomazar.github.io/samkelo-mngoma-portfolio</link><br/><link href="https://github.com/MngomaZAR">GitHub: github.com/MngomaZAR</link> | <link href="https://www.linkedin.com/in/samkelo-mngoma-72461b12a">LinkedIn: samkelo-mngoma-72461b12a</link>', 'contact')
section('Professional Profile')
add('Hands-on software and data practitioner with experience in database administration, analytics, technical operations and cloud delivery. Co-founder and COO of SAICTS, combining stakeholder coordination with implementation across mobile applications, learning platforms and data systems. Seeking software, data, cloud delivery or technical operations opportunities.')
section('Core Skills')
add('<b>Software:</b> Python, TypeScript, JavaScript, React Native, FastAPI, Node.js, REST APIs.<br/><b>Data:</b> SQL, PostgreSQL, Power BI, data cleaning, transformation, modeling and reporting.<br/><b>Delivery:</b> Git/GitHub, Docker, GitHub Actions, Oracle Cloud, Linux, Expo/EAS, regression and integration testing.<br/><b>Operations:</b> Requirements, documentation, stakeholder communication, role-based access, secret hygiene and release coordination.')
section('Professional Experience')
job('Co-founder &amp; Chief Operating Officer', 'SAICTS', 'Mar 2024 - present', [
    'Coordinate project delivery, operational processes, resources, risks and stakeholder communication.',
    'Contribute hands-on software, API, data and cloud implementation for learning and marketplace platforms.',
    'Maintain deployment documentation, test evidence and release checks across GitHub, Oracle and Expo delivery workflows.',
])
job('Data Specialist (contract)', 'Lindbong Development', 'Jan 2023 - Mar 2024', [
    'Cleaned, transformed and analyzed data; prepared visualizations and reports to support business decisions.',
    'Translated analysis into stakeholder-facing insights and coordinated technical requirements.',
])
job('Database Administrator (contract)', 'Colman Protection', 'Aug - Dec 2023', [
    'Worked on database setup, cloud configuration, access control, backup/recovery and integration planning.',
])
job('Customer Retention &amp; Data Operations', 'AA Wealth (insurance)', '2020 - 2023', [
    'Supported customer retention, data processing and cleaning, financial-data review and business communication.',
])
story.append(PageBreak())
add('SELECTED PROJECTS &amp; DEVELOPMENT', 'role')
section('Selected Engineering & Analytics Work')
job('Madabukela Academy - integrated learning platform', 'SAICTS technical delivery', '2026 | live public platform', [
    'Worked across onboarding, assessments, learner evidence portfolios and placement/in-service structures.',
    'Implemented offline queue handling, immediate quiz feedback, context-aware tutor routing and tablet-oriented interfaces.',
    'Used Node.js, PostgreSQL, Docker and Oracle Cloud; verified public desktop/tablet flows. <link href="https://www.madabukela-academy.co.za">madabukela-academy.co.za</link>',
])
job('Papzi - creator marketplace', 'SAICTS contracted engineering', '2026 | deployed TestFlight beta', [
    'Worked across Expo/React Native, FastAPI/PostgreSQL, role access, scheduled bookings, messaging, road routing and release configuration.',
    'Delivered Oracle Docker/GHCR backend and TestFlight beta; CI verified 300 concurrent read-test sessions and 3,000 requests without errors.',
    'Restricted beta, not a completed public financial marketplace; live payment and device acceptance remain ongoing.',
])
job('Commercial performance reporting', 'Independent Power BI assignment', '2026', [
    'Built native multi-page sales reporting with executive, regional, sales-manager, brand-trend and customer views, interactive filtering and recommendations. Private datasets are not public; no AB InBev/SAB employment claim.',
])
job('ESP32 telemetry &amp; Phepha safety intelligence', 'Engineering prototypes', '2026', [
    'ESP32/MPU6050 firmware: sensor fusion, receiver decoding, serial diagnostics and arming safety gates; hardware acceptance remains incomplete.',
    'Phepha: Express/WebSocket API aggregation, MapLibre layers, TTL caching and source-attributed public-data integration.',
])
section('Education & Professional Development')
add('<b>NCV Finance, Economics &amp; Accounting, Levels 2-4</b><br/>Esayidi TVET College | 2020-2022')
add('<b>Online courses and certificates:</b> IBM Applied Data Science; Google Data Analytics; IBM data engineering, DevOps, CI/CD, application security and cloud computing; Microsoft/freeCodeCamp Foundational C#; Alison database systems, computer networking and cybersecurity (online CPD). Certificate copies available on request.')
add('<b>Virtual job simulations:</b> KPMG Data Analytics and JPMorgan Chase analyst/private-banking exercises via Forage (2023). These are training simulations, not employment or internships.')
section('Leadership')
add('Esayidi TVET SRC President (2021/2022) and Secretary General (2022/2023): student representation, governance, administration and stakeholder coordination.')

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=42, leftMargin=42, topMargin=39, bottomMargin=51,
                        title='Samkelo Mngoma - Professional CV', author='Samkelo Sithembiso Mngoma',
                        subject='Software and data engineering, cloud delivery and technical operations')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
