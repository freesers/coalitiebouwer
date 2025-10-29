import streamlit as st

st.set_page_config(page_title="Coalitiebouwer (Freesers)", layout="wide")
st.title("Coalitiebouwer (Freesers)")

partijen = [
    ("PVV", 26, "#73BFF1"),
    ("GL/PvdA", 24, "#C62828"),
    ("D66", 23, "#4CAF50"),
    ("CDA", 20, "#2E7D32"),
    ("VVD", 17, "#1E3A8A"),
    ("JA21", 10, "#172554"),
    ("FvD", 5, "#6D2C2C"),
    ("SP", 4, "#E53958"),
    ("BBB", 4, "#A3C344"),
    ("Denk", 3, "#00A6A6"),
    ("PvdD", 3, "#567D46"),
    ("SGP", 3, "#9E9E9E"),
    ("CU", 3, "#C0C0C0"),
    ("50PLUS", 2, "#A16BB3"),
    ("Volt", 2, "#6D28D9"),
    ("NSC", 1, "#424242"),
]

if "geselecteerd" not in st.session_state:
    st.session_state.geselecteerd = set()

def toggle(naam):
    if naam in st.session_state.geselecteerd:
        st.session_state.geselecteerd.remove(naam)
    else:
        st.session_state.geselecteerd.add(naam)

st.header("Klik op een partij:")

# Basisknop styling (transparant → container doet de kleur)
st.markdown("""
<style>
div.stButton > button {
    width: 100% !important;
    border: none !important;
    background: transparent !important;
    color: white !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: 8px 12px !important;
    text-align: left !important;
    cursor: pointer !important;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(3)

for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 3]
    selected = naam in st.session_state.geselecteerd
    label = f"{'✅ ' if selected else ''}{naam} ({zetels})"

    shadow = "inset 0 0 8px rgba(0,0,0,.6)" if selected else "none"

    with kolom:
        # unieke container-ID zodat styling per partij werkt
        st.markdown(
            f"<div id='tile-{naam}' style='background:{kleur}; border-radius:8px; box-shadow:{shadow}; margin-bottom:8px;'>",
            unsafe_allow_html=True
        )

        if st.button(label, key=naam):
            toggle(naam)
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# Totaal
totaal = sum(z for n, z, _ in partijen if n in st.session_state.geselecteerd)
st.subheader("Totaal aantal zetels")
st.metric("Totaal", totaal)

if totaal >= 76:
    st.success("🎉 76 of meer zetels — meerderheidscoalitie.")
elif totaal > 0:
    st.info("Nog geen meerderheid.")
else:
    st.write("Selecteer partijen om te beginnen.")

if st.session_state.geselecteerd:
    st.write("Geselecteerd:", ", ".join(sorted(st.session_state.geselecteerd)))
