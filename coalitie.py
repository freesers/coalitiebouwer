import streamlit as st

st.set_page_config(page_title="Coalitiebouwer", layout="centered")

PARTIJEN = [
    ("PVV", 25), ("GL/PvdA", 20), ("D66", 27), ("CDA", 19),
    ("VVD", 23), ("JA21", 9), ("FvD", 6), ("SP", 3),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 2), ("50PLUS", 2), ("Volt", 1), 
]

if "gekozen" not in st.session_state:
    st.session_state.gekozen = set()

st.title("Coalitiecalculator")

# --- RESULTAAT BOVENAAN ---
totaal = sum(z for n, z in PARTIJEN if n in st.session_state.gekozen)
gekozen_lijst = [p for p, _ in PARTIJEN if p in st.session_state.gekozen]

st.write("**Gekozen partijen:** " + (", ".join(gekozen_lijst) if gekozen_lijst else "—"))
st.write(f"**Totaal zetels:** {totaal}")

if totaal >= 76:
    st.success("Meerderheid ✅")
else:
    st.info("Geen meerderheid ❌")

st.divider()

# --- KNOPPEN ---
for naam, zetels in PARTIJEN:
    is_geselecteerd = naam in st.session_state.gekozen
    label = f"{'✅' if is_geselecteerd else '➕'} {naam} ({zetels})"

    if st.button(label, key=f"btn_{naam}", use_container_width=True):
        if is_geselecteerd:
            st.session_state.gekozen.remove(naam)
        else:
            st.session_state.gekozen.add(naam)
        st.rerun()

st.divider()

# --- RESET ---
if st.button("Reset selectie", type="secondary", use_container_width=True):
    st.session_state.gekozen.clear()
    st.rerun()
