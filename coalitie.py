import streamlit as st

st.set_page_config(page_title="Coalitiecalculator", layout="centered")

# Data
PARTIJEN = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

# Init state
if "gekozen" not in st.session_state:
    st.session_state.gekozen = set()

st.title("Coalitiecalculator (mobiel)")

st.caption("Tik op de knoppen om partijen aan/uit te zetten.")

# UI: lijst met toggle-knoppen (één kolom, werkt stabiel op mobiel)
for naam, zetels in PARTIJEN:
    geselecteerd = naam in st.session_state.gekozen
    label = f"{'✅' if geselecteerd else '➕'} {naam} ({zetels})"
    if st.button(label, key=f"btn_{naam}", use_container_width=True):
        if geselecteerd:
            st.session_state.gekozen.remove(naam)
        else:
            st.session_state.gekozen.add(naam)

# Totaal
totaal = sum(zet for naam, zet in PARTIJEN if naam in st.session_state.gekozen)

st.divider()
st.subheader("Resultaat")
gekozen_lijst = [p for p, _ in PARTIJEN if p in st.session_state.gekozen]
st.write("**Gekozen partijen:** " + (", ".join(gekozen_lijst) if gekozen_lijst else "—"))
st.write(f"**Totaal zetels:** {totaal}")

if totaal >= 76:
    st.success("Meerderheid ✅")
else:
    st.info("Geen meerderheid ❌")

# Reset-knop
st.divider()
if st.button("Reset selectie", type="secondary", use_container_width=True, key="reset"):
    st.session_state.gekozen.clear()
    st.rerun()
