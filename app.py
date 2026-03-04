import streamlit as st
import pandas as pd
import plotly.express as px # Per grafici interattivi superiori

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="Trading Journal PRO", layout="wide")

# --- LOGIN SEMPLICE ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    pw = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Entra"):
        if pw == "TuaPassword2024": # CAMBIA QUESTA
            st.session_state.authenticated = True
            st.rerun()
    st.stop()

# --- CARICAMENTO DATI (Simulato, poi collegheremo Google Sheets) ---
@st.cache_data
def get_data():
    # Qui caricheremo i dati dal tuo foglio Google
    return pd.DataFrame(columns=["Data", "Asset", "Esito", "Percentuale", "Link", "Saldo"])

df = get_data()

# --- SIDEBAR: INSERIMENTO TRADE ---
st.sidebar.header("➕ Nuovo Trade")
with st.sidebar.form("trade_form"):
    date = st.date_input("Data")
    asset = st.text_input("Asset (es. BTC/USD)")
    outcome = st.selectbox("Esito", ["Profitto", "Perdita"])
    perc = st.number_input("Percentuale (%)", step=0.1)
    tv_link = st.text_input("Link Analisi TradingView")
    submit = st.form_submit_button("Registra Operazione")

# --- DASHBOARD PRINCIPALE ---
st.title("📊 Trading Performance Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Win Rate", "65%", "+2%") # Esempio dinamico
with col2:
    st.metric("Profitto Totale", "+12.5%", "Settimana")
with col3:
    st.metric("Trade Eseguiti", len(df))

# --- GRAFICO DELL'ACCOUNT (EQUITY CURVE) ---
st.subheader("📈 Andamento dell'Account")
# Esempio di grafico avanzato con Plotly
if not df.empty:
    fig = px.line(df, x="Data", y="Saldo", title="Equity Curve")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Aggiungi i primi trade per vedere il grafico dell'andamento.")

# --- TABELLA DETTAGLIATA ---
st.subheader("📜 Storico Operazioni")
st.dataframe(df, use_container_width=True)
