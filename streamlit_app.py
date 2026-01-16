import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="SQM Hub | Startowa", layout="wide")

# Funkcja zabezpieczająca
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if not st.session_state.password_correct:
        st.title("🔐 SQM Logistics - Terminal")
        pwd = st.text_input("Podaj kod dostępu:", type="password")
        if st.button("Wejdź"):
            if pwd == "TwojeHaslo": 
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("Błędny kod.")
        return False
    return True

if check_password():
    st.title("🛠 SQM Multimedia Solutions - Logistics Hub")
    st.markdown("---")

    # Sekcja 1: MOJE NARZĘDZIA (Aplikacje Streamlit)
    st.subheader("🚀 Moje Aplikacje Streamlit")
    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
            <a href="https://twoja-naczepa.streamlit.app" target="_blank" style="text-decoration: none;">
                <div style="background-color: #1E90FF; padding: 25px; border-radius: 12px; text-align: center; color: white; border: 1px solid #ddd;">
                    <h3 style="margin: 0;">📦 PLANOWANIE NACZEPY</h3>
                    <small>Optymalizacja przestrzeni</small>
                </div>
            </a>""", unsafe_allow_html=True)

    with c2:
        st.markdown("""
            <a href="https://twoje-sloty.streamlit.app" target="_blank" style="text-decoration: none;">
                <div style="background-color: #2E8B57; padding: 25px; border-radius: 12px; text-align: center; color: white; border: 1px solid #ddd;">
                    <h3 style="margin: 0;">📅 SLOTY / TERMINY</h3>
                    <small>Harmonogram załadunków</small>
                </div>
            </a>""", unsafe_allow_html=True)

    with c3:
        st.markdown("""
            <a href="https://twoj-transport.streamlit.app" target="_blank" style="text-decoration: none;">
                <div style="background-color: #FF4B4B; padding: 25px; border-radius: 12px; text-align: center; color: white; border: 1px solid #ddd;">
                    <h3 style="margin: 0;">🚛 TRANSPORT</h3>
                    <small>Zarządzanie flotą</small>
                </div>
            </a>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Sekcja 2: SYSTEMY FIRMOWE I ZEWNĘTRZNE
    st.subheader("🏢 Systemy Pracowe i Logistyczne")
    c4, c5, c6, c7 = st.columns(4)

    with c4:
        st.link_button("📧 Poczta firmowa", "https://outlook.office.com", use_container_width=True)
    with c5:
        st.link_button("📍 System GPS / Monitoring", "https://link-do-gps.pl", use_container_width=True)
    with c6:
        st.link_button("📂 Folder Projektów", "https://sharepoint.com", use_container_width=True)
    with c7:
        st.link_button("📊 CRM / Zamówienia", "https://crm-sqm.pl", use_container_width=True)

    # Stopka z info
    st.markdown("---")
    st.caption("Pulpit Nawigacyjny SQM Multimedia Solutions | 2026")
