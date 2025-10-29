import streamlit as st

st.set_page_config(page_title="Coalitiebouwer (Freesers)", layout="wide")
st.title("Coalitiebouwer (Freesers)")

# Hard-coded zetels + kleuren
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

# Bewaar selectie
if "geselecteerd" not in st.session_state:
    st.session_state.geselecteerd = set()

def toggle(naam):
    if naam in st.session_state.geselecteerd:
        st.session_state.geselecteerd.remove(naam)
    else:
        st.session_state.geselecteerd.add(naam)

st.header("Klik op een partij:")

# ✅ CSS die werkt op ALLE Streamlit-versies
st.markdown("""
<style>
button.st-form-submit-button {
    width: 100% !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 8px 12px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# 3 kolommen → op mobiel automatisch 1 kolom
cols = st.columns(3)

for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 3]
    selected = naam in st.session_state.geselecteerd

    bg = kleur
    shade = "inset 0 0 8px rgba(0,0,0,0.6)" if selected else "none"
    label = f"{'✅ ' if selected else ''}{naam} ({zetels})"

    with kolom:
        with st.form(key=naam):
            st.markdown(
                f"<div style='background:{bg}; border-radius:8px; "
                f"box-shadow:{shade}; margin-bottom:8px;'>",
                unsafe_allow_html=True
            )
            clicked = st.form_submit_button(label)
            st.markdown("</div>", unsafe_allow_html=True)

            if clicked:
                toggle(naam)
                st.experimental_rerun()

# Totaal
totaal = sum(z for n, z, c in partijen if n in st.session_state.geselecteerd)

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
