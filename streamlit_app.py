import streamlit as st

# Konfiguracja strony - szeroki układ
st.set_page_config(page_title="SQM LOGISTICS HUB", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS DLA WYGLĄDU PREMIUM ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1582192732213-8be32117514c?q=80&w=2000&auto=format&fit=crop'); /* Profesjonalne tło targowe */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        border-radius: 15px;
        padding: 30px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        transition: all 0.4s ease;
        text-align: center;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .glass-card:hover {
        transform: scale(1.03);
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    h1, h2, h3, p {
        color: white !important;
        font-family: 'Inter', sans-serif;
    }
    
    a { text-decoration: none !important; }

    .category-title {
        border-left: 5px solid #FFD700;
        padding-left: 15px;
        margin: 30px 0 20px 0;
        font-weight: bold;
        letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 3.5rem; margin-bottom: 0;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.6; margin-bottom: 50px;'>SQM Multimedia Solutions | Logistics & Operations</p>", unsafe_allow_html=True)

# --- SEKCJA 1: SYSTEMY FIRMOWE ---
st.markdown("<div class='category-title'><h2>🏢 SYSTEMY PRACOWE (SQM)</h2></div>", unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""<a href="https://sqmprojects.eu/panel/fairs/" target="_blank"><div class="glass-card">
        <h3 style="color: #FFD700 !important;">📅 Pro Projekty</h3>
        <p>Eventy i Sprzedaż</p>
    </div></a>""", unsafe_allow_html=True)

with c2:
    st.markdown("""<a href="https://sqm.current-rms.com/" target="_blank"><div class="glass-card">
        <h3 style="color: #00FFCC !important;">⚙️ Current RMS</h3>
        <p>Magazyn i Sprzęt</p>
    </div></a>""", unsafe_allow_html=True)

with c3:
    st.markdown("""<a href="https://reveal.eu.fleetmatics.com/pl-PL/live-map/" target="_blank"><div class="glass-card">
        <h3 style="color: #FF4B4B !important;">📍 Verizon GPS</h3>
        <p>Monitoring Floty</p>
    </div></a>""", unsafe_allow_html=True)

with c4:
    st.markdown("""<a href="https://transport.sqm.eu/lista" target="_blank"><div class="glass-card">
        <h3 style="color: #1E90FF !important;">📋 Tablica</h3>
        <p>Logistyka Wyjazdów</p>
    </div></a>""", unsafe_allow_html=True)

# --- SEKCJA 2: TWOJE APLIKACJE ---
st.markdown("<div class='category-title'><h2>🚀 MOJE NARZĘDZIA (STREAMLIT)</h2></div>", unsafe_allow_html=True)
c5, c6, c7 = st.columns(3)

with c5:
    st.markdown("""<a href="https://sqm-logistyka-rbwcgzpqbdojmahqg7yn9v.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #FF4B4B;">
        <h3 style="color: #FF4B4B !important;">📊 Nadzór Imprezy</h3>
        <p>Live Event Management</p>
    </div></a>""", unsafe_allow_html=True)

with c6:
    st.markdown("""<a href="https://optymalizator2-6eurzxtfvrsy4xoj3g6hdu.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #1E90FF;">
        <h3 style="color: #1E90FF !important;">📦 Naczepy</h3>
        <p>Optymalizacja Załadunku</p>
    </div></a>""", unsafe_allow_html=True)

with c7:
    st.markdown("""<a href="https://logistyka-notes-2026.streamlit.app/" target="_blank"><div class="glass-card" style="border-bottom: 5px solid #2E8B57;">
        <h3 style="color: #2E8B57 !important;">📝 Notes 2026</h3>
        <p>Kalendarz i Zadania</p>
    </div></a>""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
