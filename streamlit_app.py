import streamlit as st
import datetime
import base64
import calendar

# Konfiguracja strony
st.set_page_config(page_title="SQM Hub", layout="wide", initial_sidebar_state="collapsed")

# Funkcja do konwersji obrazu lokalnego na Base64
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

# Obsługa tła
bin_str = get_base64_of_bin_file('tlo.jpg')
if bin_str:
    bg_img_style = f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(bg_img_style, unsafe_allow_html=True)

# --- STYLE CSS ---
st.markdown("""
    <style>
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        margin-bottom: 20px;
        min-height: 160px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        transition: transform 0.3s ease, background 0.3s ease;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.15);
    }
    h1, h2, h3, p, th, td { color: white !important; font-family: 'Inter', sans-serif; }
    a { text-decoration: none !important; }
    
    .cal-container {
        display: flex;
        justify-content: center;
        margin-top: 50px;
    }
    .cal-table { 
        width: 400px; 
        border-collapse: collapse; 
        background: rgba(0,0,0,0.3); 
        border-radius: 15px; 
        overflow: hidden;
    }
    .cal-table th { background: rgba(255,255,255,0.15); padding: 12px; font-size: 0.9rem; }
    .cal-table td { padding: 12px; text-align: center; border: 1px solid rgba(255,255,255,0.05); font-size: 1rem; }
    .today { 
        background: #FF4B4B; 
        color: white; 
        padding: 5px 10px; 
        border-radius: 5px; 
        font-weight: bold; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- POWITANIE ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>Logistics Department</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8; font-size: 1.5rem;'>SQM Operations Center</p>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# --- SEKCJA 1: MOJE APLIKACJE (6 ELEMENTÓW w układzie 3x2 dla lepszej czytelności) ---
st.subheader("🚀 Moje Aplikacje")
row1_1, row1_2, row1_3 = st.columns(3)
row2_1, row2_2, row2_3 = st.columns(3)

with row1_1:
    st.markdown('<a href="https://transport.sqm.eu/lista" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #1E90FF;"><h3>📋 Tablica</h3><p>Logistyka Wyjazdów</p></div></a>', unsafe_allow_html=True)
with row1_2:
    st.markdown('<a href="https://sqm-logistyka-rbwcgzpqbdojmahqg7yn9v.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #FF4B4B;"><h3>📊 Nadzór Imprezy</h3><p>Aktualny Event</p></div></a>', unsafe_allow_html=True)
with row1_3:
    st.markdown('<a href="https://optymalizator2-6eurzxtfvrsy4xoj3g6hdu.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #1E90FF;"><h3>📦 Naczepy</h3><p>Optymalizator Załadunku</p></div></a>', unsafe_allow_html=True)

with row2_1:
    st.markdown('<a href="https://logistyka-notes-2026.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #2E8B57;"><h3>📝 Notes 2026</h3><p>Kalendarz i Zadania</p></div></a>', unsafe_allow_html=True)
with row2_2:
    st.markdown('<a href="https://flota-sqm.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #FFA500;"><h3>🚛 Flota SQM</h3><p>Zarządzanie Pojazdami</p></div></a>', unsafe_allow_html=True)
with row2_3:
    st.markdown('<a href="https://vecturasqmtransporty.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #8A2BE2;"><h3>🚚 Vectura SQM</h3><p>System Transportowy</p></div></a>', unsafe_allow_html=True)

# --- SEKCJA 2: SYSTEMY PRACOWE ---
st.subheader("🏢 Systemy Pracowe (SQM)")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<a href="https://sqmprojects.eu/panel/fairs/" target="_blank"><div class="glass-card"><h3>📅 SQM Projects</h3><p>Eventy i Sprzedaż</p></div></a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://sqm.current-rms.com/" target="_blank"><div class="glass-card"><h3>⚙️ Current RMS</h3><p>Szczegóły Projektów</p></div></a>', unsafe_allow_html=True)
with col3:
    st.markdown('<a href="https://reveal.eu.fleetmatics.com/pl-PL/live-map/" target="_blank"><div class="glass-card"><h3>📍 Verizon GPS</h3><p>Monitoring Floty</p></div></a>', unsafe_allow_html=True)

# --- SEKCJA 3: KALENDARZ NA ŚRODKU ---
st.markdown("<br><hr style='opacity:0.2;'><br>", unsafe_allow_html=True)

now = datetime.datetime.now()
cal = calendar.Calendar(firstweekday=0)
month_days = cal.monthdayscalendar(now.year, now.month)
month_name_pl = ["STYCZEŃ", "LUTY", "MARZEC", "KWIECIEŃ", "MAJ", "CZERWIEC", "LIPIEC", "SIERPIEŃ", "WRZESIEŃ", "PAŹDZIERNIK", "LISTOPAD", "GRUDZIEŃ"][now.month-1]

html_cal = f"""
<div class="cal-container">
    <table class="cal-table">
        <tr><th colspan="7" style="font-size: 1.2rem; letter-spacing: 2px;">{month_name_pl} {now.year}</th></tr>
        <tr><th>Pn</th><th>Wt</th><th>Śr</th><th>Czw</th><th>Pt</th><th>Sob</th><th>Nd</th></tr>
"""

for week in month_days:
    html_cal += "<tr>"
    for day in week:
        if day == 0:
            html_cal += "<td></td>"
        elif day == now.day:
            html_cal += f"<td><span class='today'>{day}</span></td>"
        else:
            html_cal += f"<td>{day}</td>"
    html_cal += "</tr>"

html_cal += "</table></div>"
st.markdown(html_cal, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("<p style='text-align: center; opacity: 0.5;'>SQM Hub | Operations Center</p>", unsafe_allow_html=True)
