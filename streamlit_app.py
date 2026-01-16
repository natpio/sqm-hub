import streamlit as st
import datetime
import base64
import calendar

# Konfiguracja strony
st.set_page_config(page_title="SQM Hub", layout="wide", initial_sidebar_state="collapsed")

# Funkcja do konwersji obrazu lokalnego na Base64 (żeby tło zawsze działało)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# INSTRUKCJA: Upewnij się, że plik ze zdjęciem nazywa się 'tlo.jpg' i jest w tym samym folderze
try:
    bin_str = get_base64_of_bin_file('tlo.jpg')
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
except:
    st.warning("Nie znaleziono pliku tlo.jpg. Wrzuć go do folderu z aplikacją.")

# --- STYLE CSS DLA KAFELKÓW I KALENDARZA ---
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
    }
    h1, h2, h3, p, th, td { color: white !important; font-family: 'Inter', sans-serif; }
    a { text-decoration: none !important; }
    
    /* Styl kalendarza */
    .cal-table { width: 100%; border-collapse: collapse; background: rgba(0,0,0,0.2); border-radius: 10px; }
    .cal-table th { background: rgba(255,255,255,0.1); padding: 10px; }
    .cal-table td { padding: 10px; text-align: center; border: 1px solid rgba(255,255,255,0.05); }
    .today { background: #FF4B4B; border-radius: 50%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- POWITANIE ---
st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-top: 50px;'>Witaj w pracy, Logistyku SQM!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8; font-size: 1.2rem;'>Gotowy na dzisiejsze wyzwania logistyczne?</p>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# --- SEKCJA 1: SYSTEMY PRACOWE ---
st.subheader("🏢 Systemy Pracowe (SQM)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<a href="https://transport.sqm.eu/lista" target="_blank"><div class="glass-card"><h3>📋 Tablica</h3><p>Logistyka Wyjazdów</p></div></a>', unsafe_allow_html=True)
with col2:
    st.markdown('<a href="https://sqmprojects.eu/panel/fairs/" target="_blank"><div class="glass-card"><h3>📅 SQM Projects</h3><p>Eventy i Sprzedaż</p></div></a>', unsafe_allow_html=True)
with col3:
    st.markdown('<a href="https://sqm.current-rms.com/" target="_blank"><div class="glass-card"><h3>⚙️ Current RMS</h3><p>Szczegóły Projektów</p></div></a>', unsafe_allow_html=True)
with col4:
    st.markdown('<a href="https://reveal.eu.fleetmatics.com/pl-PL/live-map/" target="_blank"><div class="glass-card"><h3>📍 Verizon GPS</h3><p>Monitoring Floty</p></div></a>', unsafe_allow_html=True)

# --- SEKCJA 2: MOJE NARZĘDZIA ---
st.subheader("🚀 Moje Autorskie Aplikacje")
c5, c6, c7 = st.columns(3)

with c5:
    st.markdown('<a href="https://sqm-logistyka-rbwcgzpqbdojmahqg7yn9v.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #FF4B4B;"><h3>📊 Nadzór Imprezy</h3><p>Aktualny Event</p></div></a>', unsafe_allow_html=True)
with c6:
    st.markdown('<a href="https://optymalizator2-6eurzxtfvrsy4xoj3g6hdu.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #1E90FF;"><h3>📦 Naczepy</h3><p>Optymalizator Załadunku</p></div></a>', unsafe_allow_html=True)
with c7:
    st.markdown('<a href="https://logistyka-notes-2026.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #2E8B57;"><h3>📝 Notes 2026</h3><p>Kalendarz i Zadania</p></div></a>', unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# --- PANEL DOLNY: ZEGAR I KALENDARZ ---
f_col1, f_col2 = st.columns([1, 1.5])

with f_col1:
    now = datetime.datetime.now()
    st.markdown(f"<div style='font-size: 5rem; font-weight: bold; text-align: center;'>{now.strftime('%H:%M:%S')}</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.5rem;'>{now.strftime('%d.%m.%Y')}</p>", unsafe_allow_html=True)

with f_col2:
    # Budowa tabeli kalendarza
    cal = calendar.Calendar(firstweekday=0)
    month_days = cal.monthdayscalendar(now.year, now.month)
    month_name = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"][now.month-1]
    
    html_cal = f"<h3 style='text-align:center;'>{month_name} {now.year}</h3><table class='cal-table'><tr><th>Pn</th><th>Wt</th><th>Śr</th><th>Czw</th><th>Pt</th><th>Sob</th><th>Nd</th></tr>"
    for week in month_days:
        html_cal += "<tr>"
        for day in week:
            if day == 0:
                html_cal += "<td></td>"
            elif day == now.day:
                html_cal += f"<td><span class='today'>&nbsp;{day}&nbsp;</span></td>"
            else:
                html_cal += f"<td>{day}</td>"
        html_cal += "</tr>"
    html_cal += "</table>"
    st.markdown(html_cal, unsafe_allow_html=True)

# Automatyczne odświeżanie zegara co 30 sekund (żeby nie muliło strony)
st.empty()
import time
time.sleep(30)
st.rerun()
