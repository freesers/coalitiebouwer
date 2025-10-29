import streamlit as st

st.set_page_config(page_title="Coalitiebouwer (Freesers)", layout="wide")
st.title("Coalitiebouwer (Freesers)")

# Zetels
partijen = [
    ("PVV", 26),
    ("GL/PvdA", 24),
    ("D66", 23),
    ("CDA", 20),
    ("VVD", 17),
    ("JA21", 10),
    ("FvD", 5),
    ("SP", 4),
    ("BBB", 4),
    ("Denk", 3),
    ("PvdD", 3),
    ("SGP", 3),
    ("CU", 3),
    ("50PLUS", 2),
    ("Volt", 2),
    ("NSC", 1),
]

if "geselecteerd" not in st.session_state:
    st.session_state.geselecteerd = set()

st.header("Klik op een partij:")

cols = st.columns(3)

for i, (naam, zetels) in enumerate(partijen):
    col = cols[i % 3]
    selected = naam in st.session_state.geselecteerd
    klik = col.checkbox(f"{naam} ({zetels})", value=selected, key=naam)

    if klik:
        st.session_state.geselecteerd.add(naam)
    else:
        st.session_state.geselecteerd.discard(naam)

# Zeteltelling
totaal = sum(z for n, z in partijen if n in st.session_state.geselecteerd)

st.subheader("Totaal aantal zetels")
st.metric("Totaal", totaal)

if totaal >= 76:
    st.success("🎉 76 of meer zetels — meerderheidscoalitie.")
elif totaal > 0:
    st.info("Nog niet boven de 76.")
else:
    st.write("Selecteer partijen om te beginnen.")

if st.session_state.geselecteerd:
    st.write("Geselecteerde partijen:", ", ".join(sorted(st.session_state.geselecteerd)))
