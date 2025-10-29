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

# selectie bewaren
if "geselecteerd" not in st.session_state:
    st.session_state.geselecteerd = set()

def toggle(naam):
    if naam in st.session_state.geselecteerd:
        st.session_state.geselecteerd.remove(naam)
    else:
        st.session_state.geselecteerd.add(naam)

# handle ?toggle=partij
query = st.experimental_get_query_params()
if "toggle" in query:
    toggle(query["toggle"][0])
    st.experimental_set_query_params()  # URL weer schoonmaken
    st.experimental_rerun()

st.header("Klik partijen om te selecteren / deselecteren")

# CSS knop-styling
st.markdown("""
<style>
.party-btn {
    display: block;
    width: 100%;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 600;
    border: none;
    cursor: pointer;
    margin-bottom: 8px;
    text-align: left;
    color: white;
}
.party-selected {
    box-shadow: inset 0 0 8px rgba(0,0,0,0.6);
}
</style>
""", unsafe_allow_html=True)

# 3 kolommen op desktop → automatisch 1 kolom op mobiel
cols = st.columns(3)

for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 3]
    selected = naam in st.session_state.geselecteerd
    extra = " party-selected" if selected else ""

    kolom.markdown(
        f"""
        <button class="party-btn{extra}" 
                style="background:{kleur};"
                onclick="window.location.search='toggle={naam}'">
            {naam} ({zetels})
        </button>
        """,
        unsafe_allow_html=True
    )

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
