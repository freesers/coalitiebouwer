import streamlit as st

st.set_page_config(page_title="Coalitiecalculator", layout="wide")

partijen = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

# Initialize toggles
for naam, _ in partijen:
    if naam not in st.session_state:
        st.session_state[naam] = False

st.title("Coalitiecalculator (mobiel vriendelijk)")

st.write("Tik op partijen om ze toe te voegen of te verwijderen:")

# Maak knoppen in eenvoudige kolommen (werkt op mobiel)
cols = st.columns(2)
for i, (naam, zetels) in enumerate(partijen):
    col = cols[i % 2]
    if st.session_state[naam]:
        if col.button(f"✅ {naam} ({zetels})"):
            st.session_state[naam] = False
    else:
        if col.button(f"{naam} ({zetels})"):
            st.session_state[naam] = True

# Bereken totaal
gekozen = [p for p, _ in partijen if st.session_state[p]]
totaal = sum(z for p, z in partijen if st.session_state[p])

st.write("### Gekozen partijen:")
st.write(", ".join(gekozen) if gekozen else "—")

st.write("### Totaal zetels:")
st.write(f"**{totaal}**")

if totaal >= 76:
    st.success("Meerderheid ✅")
else:
    st.info("Geen meerderheid ❌")
