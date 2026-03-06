import streamlit as st
import random

# Configurarea paginii (va arăta bine pe mobil)
st.set_page_config(page_title="Ghicește Numărul", page_icon="🎮")

st.title("🎮 Ghicește Numărul!")
st.write("Am ales un număr între 1 și 100. Poți să-l ghicești?")

# Inițializăm starea jocului (ca să nu se reseteze la fiecare click)
if 'numar_secret' not in st.session_state:
    st.session_state.numar_secret = random.randint(1, 100)
    st.session_state.vieti = 7
    st.session_state.joc_terminat = False

# Afișăm viețile rămase
st.metric(label="Vieți rămase", value=st.session_state.vieti)

# Caseta de introducere a numărului
if not st.session_state.joc_terminat:
    incercare = st.number_input("Introdu numărul tău:", min_value=1, max_value=100, step=1)

    if st.button("Verifică"):
        st.session_state.vieti -= 1

        if incercare == st.session_state.numar_secret:
            st.balloons()  # Efect vizual de sărbătorire!
            st.success(f"BRAVO! Ai ghicit numărul {st.session_state.numar_secret}!")
            st.session_state.joc_terminat = True
        elif st.session_state.vieti == 0:
            st.error(f"GAME OVER! Numărul era {st.session_state.numar_secret}.")
            st.session_state.joc_terminat = True
        elif incercare < st.session_state.numar_secret:
            st.info("Indiciu: E prea MIC! Bagă unul mai mare.")
        else:
            st.info("Indiciu: E prea MARE! Bagă unul mai mic.")

# Buton de restart
if st.session_state.joc_terminat:
    if st.button("Joacă din nou"):
        del st.session_state.numar_secret
        st.rerun()