import streamlit as st

st.set_page_config(page_title="Coalitiecalculator", layout="centered")

partijen = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

st.title("Coalitiecalculator")

# Selectie
gekozen = st.multiselect(
    "Kies partijen:",
    options=[p[0] for p in partijen]
)

# Totaal berekenen
totaal = sum(z for (p, z) in partijen if p in gekozen)

st.write("### Totaal aantal zetels:")
st.write(f"**{totaal} zetels**")

# Eventueel extra: drempel voor meerderheid
if totaal >= 76:
    st.success("Meerderheid ✅")
else:
    st.info("Geen meerderheid ❌")
