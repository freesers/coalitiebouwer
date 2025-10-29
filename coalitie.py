import streamlit as st

st.set_page_config(page_title="Coalitie-tool", layout="wide")
st.title("Coalitie-combinatie tool (Peilingwijzer)")

# Hard-coded zetels en kleuren
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

st.header("Klik partijen om de coalitie te vormen")

# ---- Grote knoppen (mobielvriendelijk) ----
st.markdown("""
<style>
.big-button button {
    padding: 16px 20px !important;
    border-radius: 12px !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    width: 100% !important;
    margin-bottom: 8px !important;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(2)  # 2 per rij → betere touchbaarheid

for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 2]
    geselecteerd = naam in st.session_state.geselecteerd

    container_style = f"""
        background-color: {kleur};
        color: white;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        margin-bottom: 6px;
        {"box-shadow: inset 0 0 8px #00000088;" if geselecteerd else ""}
    """

    with kolom:
        st.markdown(f"<div style='{container_style}' class='big-button'>{naam} ({zetels})</div>", unsafe_allow_html=True)
        st.button("Selecteer / verwijder", key=naam, on_click=toggle, args=(naam,))

# ---- Totaal berekening ----
totaal = sum(zetels for naam, zetels, _ in partijen if naam in st.session_state.geselecteerd)

st.subheader("Totaal aantal zetels")
st.metric("Totaal", totaal)

if totaal >= 76:
    st.success("🎉 76 of meer zetels — meerderheidscoalitie.")
elif totaal > 0:
    st.info("Nog geen meerderheid.")
else:
    st.write("Selecteer partijen om te beginnen.")

if st.session_state.geselecteerd:
    st.write("Geselecteerde partijen:", ", ".join(st.session_state.geselecteerd))
