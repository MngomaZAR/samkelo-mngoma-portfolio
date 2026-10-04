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
add('<b>Software:</b> Python, TypeScript, JavaScript, React Native, FastAPI, Node.js, REST APIs.<br/><b>Data:</b> SQL, PostgreSQL, Power BI, data cleaning, transformation, modeling and reporting.<br/><b>Cloud &amp; delivery:</b> AWS Lambda/API Gateway/Amplify/CloudWatch, Oracle Cloud, Docker, GitHub Actions, Linux, Expo/EAS and integration testing.<br/><b>Operations:</b> Requirements, documentation, stakeholder communication, role-based access, secret hygiene and release coordination.')
section('Professional Experience')
job('Co-founder &amp; Chief Operating Officer', 'SAICTS', 'Mar 2024 - present', [
    'Coordinate project delivery, operational processes, resources, risks and stakeholder communication.',
    'Contribute software, API, data and cloud implementation across institutional elections, USSD services, learning and marketplace platforms.',
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
section('Leadership')
add('Esayidi TVET SRC President (2021/2022) and Secretary General (2022/2023): student representation, governance, administration and stakeholder coordination.')
story.append(PageBreak())
add('SELECTED PROJECTS &amp; DEVELOPMENT', 'role')
section('Selected Engineering & Analytics Work')
job('MUT SRC elections - voter verification &amp; operations', 'SAICTS institutional delivery', '2025', [
    'Prepared voter-roll imports covering 12,000+ records, with cleaning, duplicate handling and database integrity checks.',
    'Worked on barcode verification, administrative controls, activity logs and reporting using AWS Lambda, API Gateway, Amplify and CloudWatch.',
])
job('Elangeni TVET SRC elections &amp; USSD services', 'SAICTS institutional delivery', '2025', [
    'Contributed USSD/web voting workflows, voter eligibility checks, administrative monitoring and campus results/reporting.',
    'Co-authored the August 2025 election report; analyzed USSD sessions, retries, menu interactions and time-based billing reconciliation.',
])
job('Madabukela Academy - integrated learning platform', 'SAICTS technical delivery', '2026 | live public platform', [
    'Worked on assessments, evidence portfolios, offline queues, immediate feedback and context-aware tutor routing for tablet learners.',
    'Node.js/PostgreSQL/Docker on Oracle Cloud; verified public desktop/tablet flows. <link href="https://www.madabukela-academy.co.za">madabukela-academy.co.za</link>',
])
job('Papzi - creator marketplace', 'SAICTS contracted engineering', '2026 | deployed TestFlight beta', [
    'Worked across Expo/React Native, FastAPI/PostgreSQL, role access, scheduled bookings, messaging, road routing and release configuration.',
    'Delivered Oracle Docker/GHCR backend and TestFlight beta; CI verified 300 concurrent read-test sessions and 3,000 requests without errors.',
])
job('Commercial performance reporting', 'Independent Power BI assignment', '2026', [
    'Built native multi-page sales reporting with executive, regional, sales-manager, brand-trend and customer views, interactive filters and recommendations. Independent assignment; private source data is not published.',
])
job('Drone telemetry &amp; Phepha safety intelligence', 'Engineering prototypes', '2026', [
    'ESP32/Raspberry Pi: inertial/distance sensing, receiver decoding, JSON serial telemetry, CSV/web monitoring and heartbeat/arming failsafes. Bench prototypes, not flight-certified systems.',
    'Phepha: Express/WebSocket API aggregation, MapLibre layers, TTL caching and source-attributed public-data integration.',
])
section('Education & Professional Development')
add('<b>NCV Finance, Economics &amp; Accounting, Levels 2-4</b><br/>Esayidi TVET College | 2020-2022')
add('<b>Online professional development:</b> IBM Applied Data Science, data engineering, DevOps, CI/CD and application security; Google Data Analytics; Microsoft/freeCodeCamp Foundational C#; Alison database systems, networking and cybersecurity (CPD). Certificate copies available on request.')
add('<b>Forage virtual job simulations (2023):</b> KPMG Data Analytics and JPMorgan Chase analyst/private-banking exercises. Training, not employment.')

doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=42, leftMargin=42, topMargin=39, bottomMargin=51,
                        title='Samkelo Mngoma - Professional CV', author='Samkelo Sithembiso Mngoma',
                        subject='Software and data engineering, cloud delivery and technical operations')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
