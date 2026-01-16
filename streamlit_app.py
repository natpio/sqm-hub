import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="SQM COMMAND CENTER", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS DLA EFEKTU WOW ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('https://images.unsplash.com/photo-1540575861501-7cf05a4b125a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'); /* Zdjęcie eventowe/targowe */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: 0.3s transform ease-in-out;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        background: rgba(255, 255, 255, 0.2);
    }

    h1, h3, p {
        color: white !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    a { text-decoration: none !important; }
    
    .badge {
        font-size: 0.8rem;
        padding: 4px 8px;
        border-radius: 5px;
        text-transform: uppercase;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛠 SQM COMMAND CENTER")
st.markdown("<p style='font-size: 1.2rem; opacity: 0.8;'>Pulpit Nawigacyjny Logistyki SQM Multimedia Solutions</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SEKCJA 1: SYSTEMY FIRMOWE ---
st.subheader("🏢 Systemy Operacyjne SQM")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""<a href="https://sqmprojects.eu/panel/fairs/" target="_blank"><div class="glass-card">
        <h3 style="color: #FFD700 !important;">📅 Pro Projekty</h3>
        <p>Eventy i sprzedaż</p>
    </div></a>""", unsafe_allow_html=True)

with col2:
    st.markdown("""<a href="https://sqm.current-rms.com/" target="_blank"><div class="glass-card">
        <h3 style="color: #00FFCC !important;">⚙️ Current RMS</h3>
        <p>Szczegóły projektów</p>
    </div></a>""", unsafe_allow_html=True)

with col3:
    st.markdown("""<a href="https://reveal.eu.fleetmatics.com/pl-PL/live-map/" target="_blank"><div class="glass-card">
        <h3 style="color: #FF4B4B !important;">📍 Verizon Reveal</h3>
        <p>Monitoring GPS floty</p>
    </div></a>""", unsafe_allow_html=True)

with col4:
    st.markdown("""<a href="https://transport.sqm.eu/lista" target="_blank"><div class="glass-card">
        <h3 style="color: #1E90FF !important;">📋 Tablica Transportowa</h3>
        <p>Nadchodzące wyjazdy</p>
    </div></a>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- SEKCJA 2: TWOJE APLIKACJE (KOLOROWE) ---
st.subheader("🚀 Moje Autorskie Narzędzia")
c1, c2, c3 = st.columns(3)

with c1:
    # NADZÓR IMPREZY (Zmienne kolory/treść)
    st.markdown(f"""<a href="https://sqm-logistyka-rbwcgzpqbdojmahqg7yn9v.streamlit.app/" target="_blank">
        <div class="glass-card" style="border-top: 5px solid #FF4B4B;">
            <span class="badge" style="background: #FF4B4B;">OPERACJE</span>
            <h3>📊 Nadzór Imprezy</h3>
            <p>Aktualny Event / LIVE</p>
        </div></a>""", unsafe_allow_html=True)

with c2:
    # OPTYMALIZATOR
    st.markdown(f"""<a href="https://optymalizator2-6eurzxtfvrsy4xoj3g6hdu.streamlit.app/" target="_blank">
        <div class="glass-card" style="border-top: 5px solid #1E90FF;">
            <span class="badge" style="background: #1E90FF;">LOGISTYKA</span>
            <h3>📦 Planowanie Naczepy</h3>
            <p>Optymalizator 2.0</p>
        </div></a>""", unsafe_allow_html=True)

with c3:
    # NOTES 2026
    st.markdown(f"""<a href="https://logistyka-notes-2026.streamlit.app/" target="_blank">
        <div class="glass-card" style="border-top: 5px solid #2E8B57;">
            <span class="badge" style="background: #2E8B57;">KALENDARZ</span>
            <h3>📝 Notes & Eventy</h3>
            <p>Planowanie 2026</p>
        </div></a>""", unsafe_allow_html=True)

st.markdown("---")
st.caption("Zalogowany jako Logistyk SQM | ISE Barcelona & WTM London Edition")
