import streamlit as st

st.set_page_config(page_title="Coalitiecalculator", layout="centered")

PARTIJEN = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

# Init state
if "gekozen" not in st.session_state:
    st.session_state.gekozen = set()

st.title("Coalitiecalculator")

st.caption("Tik om partijen aan of uit te zetten.")

# Toggle knoppen met directe rerender
for naam, zetels in PARTIJEN:
    geselecteerd = naam in st.session_state.gekozen
    label = f"{'✅' if geselecteerd else '➕'} {naam} ({zetels})"

    if st.button(label, key=f"btn_{naam}", use_container_width=True):
        if geselecteerd:
            st.session_state.gekozen.remove(naam)
        else:
            st.session_state.gekozen.add(naam)
        st.rerun()   # ← directe UI update

# Totaal berekenen
totaal = sum(z for n, z in PARTIJEN if n in st.session_state.gekozen)
gekozen_lijst = [p for p, _ in PARTIJEN if p in st.session_state.gekozen]

st.divider()
st.subheader("Resultaat")
st.write("**Gekozen partijen:** " + (", ".join(gekozen_lijst) if gekozen_lijst else "—"))
st.write(f"**Totaal zetels:** {totaal}")

if totaal >= 76:
    st.success("Meerderheid ✅")
else:
    st.info("Geen meerderheid ❌")

# Reset
st.divider()
if st.button("Reset selectie", type="secondary", use_container_width=True):
    st.session_state.gekozen.clear()
    st.rerun()
