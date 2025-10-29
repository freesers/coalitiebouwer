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

st.header("Klik om partijen toe te voegen of te verwijderen")

# ---- CSS voor knop-styling ----
st.markdown("""
<style>
button[kind="secondary"] {
    width: 100% !important;
    border-radius: 10px !important;
    padding: 14px !important;
    font-size: 16px !important;
    font-weight: 600 !important;
    border: none !important;
}
</style>
""", unsafe_allow_html=True)

# ---- 3 kolommen voor compact mobiel beeld ----
cols = st.columns(3)

for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 3]
    geselecteerd = naam in st.session_state.geselecteerd

    label = f"{'✅ ' if geselecteerd else ''}{naam} ({zetels})"
    bg = ("inset 0 0 10px rgba(0,0,0,0.6)" if geselecteerd else "none")

    with kolom:
        st.markdown(
            f"<div style='background-color:{kleur}; padding:6px; border-radius:10px; "
            f"box-shadow:{bg}; text-align:center;'>",
            unsafe_allow_html=True
        )
        st.button(label, key=naam, on_click=toggle, args=(naam,))
        st.markdown("</div>", unsafe_allow_html=True)

# ---- Zeteltelling ----
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
    st.write("Geselecteerde partijen:", ", ".join(sorted(st.session_state.geselecteerd)))
