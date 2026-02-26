import streamlit as st
import pandas as pd
import random
import time

# --- LOGIKA LUDKA ---
class Ludek:
    def __init__(self, id):
        self.id = id
        self.x = random.randint(0, 50)
        self.y = random.randint(0, 50)
        self.energia = random.randint(50, 100)

    def rusz_sie(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.energia -= 1

# --- KONFIGURACJA STRONY ---
st.set_page_config(page_title="AI Creatures", layout="wide")
st.title("🌍 Żywa Symulacja AI")

# Inicjalizacja stanu
if 'ludki' not in st.session_state:
    st.session_state.ludki = [Ludek(i) for i in range(15)]
    st.session_state.tura = 0

# Panel boczny ze sterowaniem
st.sidebar.header("Ustawienia świata")
running = st.sidebar.toggle("▶️ Uruchom symulację", value=False)
speed = st.sidebar.slider("Prędkość (sekundy)", 0.1, 2.0, 0.5)

if st.sidebar.button("Resetuj świat"):
    st.session_state.ludki = [Ludek(i) for i in range(15)]
    st.session_state.tura = 0
    st.rerun()

# Główna pętla ruchu
if running:
    for l in st.session_state.ludki:
        if l.energia > 0:
            l.rusz_sie()
    st.session_state.tura += 1

# --- WIZUALIZACJA ---
data = pd.DataFrame([{'x': l.x, 'y': l.y, 'energia': l.energia, 'id': l.id} for l in st.session_state.ludki if l.energia > 0])

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"Mapa Świata (Tura: {st.session_state.tura})")
    # Wykres punktowy jako mapa
    st.scatter_chart(data, x='x', y='y', size='energia', color='energia')

with col2:
    st.subheader("Statystyki")
    st.write(f"Żyjących: {len(data)}")
    st.dataframe(data[['id', 'energia']].sort_values(by='energia', ascending=False))

# Automatyczne odświeżanie
if running:
    time.sleep(speed)
    st.rerun()