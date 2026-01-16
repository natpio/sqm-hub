import streamlit as st
import datetime
import time

# Konfiguracja strony
st.set_page_config(page_title="SQM Hub", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://raw.githubusercontent.com/TWOJA_NAZWA_UZYTKOWNIKA/TWOJE_REPO/main/tlo.jpg'); /* Podmień link po wrzuceniu na GitHub */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: transform 0.3s ease;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.2);
    }

    h1, h2, h3, p, span { color: white !important; font-family: 'Inter', sans-serif; }
    
    .clock-text { font-size: 3rem; font-weight: bold; text-align: center; }
    .calendar-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- POWITANIE ---
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>Witaj w pracy, Logistyku SQM!</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>Gotowy na dzisiejsze wyzwania logistyczne?</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SEKCJA 1: SYSTEMY PRACOWE (Z POPRAWIONĄ KOLEJNOŚCIĄ) ---
st.subheader("🏢 Systemy Pracowe (SQM)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""<a href="https://transport.sqm.eu/lista" target="_blank"><div class="glass-card">
        <h3 style="color: #1E90FF !important;">📋 Tablica</h3>
        <p>Logistyka Wyjazdów</p>
    </div></a>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<a href="https://sqmprojects.eu/panel/fairs/" target="_blank"><div class="glass-card">
        <h3 style="color: #FFD700 !important;">📅 SQM Projects</h3>
        <p>Eventy i Sprzedaż</p>
    </div></a>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<a href="https://sqm.current-rms.com/" target="_blank"><div class="glass-card">
        <h3 style="color: #00FFCC !important;">⚙️ Current RMS</h3>
        <p>Szczegóły Projektów</p>
    </div></a>""", unsafe_allow_html=True)

with col4:
    st.markdown("""<a href="https://reveal.eu.fleetmatics.com/pl-PL/live-map/" target="_blank"><div class="glass-card">
        <h3 style="color: #FF4B4B !important;">📍 Verizon GPS</h3>
        <p>Monitoring Floty</p>
    </div></a>""", unsafe_allow_html=True)

# --- SEKCJA 2: MOJE NARZĘDZIA ---
st.subheader("🚀 Moje Autorskie Aplikacje")
c5, c6, c7 = st.columns(3)

with c5:
    st.markdown("""<a href="https://sqm-logistyka-rbwcgzpqbdojmahqg7yn9v.streamlit.app/" target="_blank"><div class="glass-card" style="border-top: 4px solid #FF4B4B;">
        <h3>📊 Nadzór Imprezy</h3>
        <p>Aktualnie Obsługiwany Event</p>
    </div></a>""", unsafe_allow_html=True)

with c6:
    st.markdown("""<a href="https://optymalizator2-6eurzxtfvrsy4xoj3g6hdu.streamlit.app/" target="_blank"><div class="glass-card" style="border-top: 4px solid #1E90FF;">
        <h3>📦 Naczepy</h3>
        <p>Optymalizator Załadunku</p>
    </div></a>""", unsafe_allow_html=True)

with c7:
    st.markdown("""<a href="https://logistyka-notes-2026.streamlit.app/" target="_blank"><div class="glass-card" style="border-top: 4px solid #2E8B57;">
        <h3>📝 Notes 2026</h3>
        <p>Kalendarz i Zadania</p>
    </div></a>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- DOLNY PANEL: ZEGAR I KALENDARZ ---
footer_col1, footer_col2 = st.columns([1, 2])

with footer_col1:
    # ZEGAR
    now = datetime.datetime.now()
    st.markdown(f"<div class='clock-text'>{now.strftime('%H:%M:%S')}</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'>{now.strftime('%d.%m.%Y')}</p>", unsafe_allow_html=True)

with footer_col2:
    # KALENDARZ (Widok miesięczny)
    import calendar
    year, month = now.year, now.month
    cal = calendar.month(year, month)
    st.markdown(f"<pre style='color: white; background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px; font-size: 1.2rem; text-align: center;'>{cal}</pre>", unsafe_allow_html=True)

st.markdown("---")
st.caption("SQM Hub | ISE Barcelona & WTM London Edition")
