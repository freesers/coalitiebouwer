import streamlit as st

st.set_page_config(page_title="Coalitiebouwer (Freesers)", layout="wide")
st.title("Coalitiebouwer (Freesers)")

# Zetels + partijkleuren
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

st.header("Klik op een partij:")

# 3 kolommen desktop → 1 mobiel (Streamlit doet dat automatisch)
cols = st.columns(3)

for i, (naam, zetels, kleur) in enumerate(partijen):
    col = cols[i % 3]

    selected = naam in st.session_state.geselecteerd
    label = f"{naam} ({zetels})"

    # kleurblok + checkbox in één horizontale regel
    with col:
        col1, col2 = st.columns([0.25, 0.75])
        with col1:
            st.markdown(f"<div style='background:{kleur}; width:100%; height:22px; border-radius:4px;'></div>", unsafe_allow_html=True)
        with col2:
            klik = st.checkbox(label, value=selected, key=naam)

        if klik and not selected:
            st.session_state.geselecteerd.add(naam)
        if not klik and selected:
            st.session_state.geselecteerd.remove(naam)

# Zeteltelling
totaal = sum(z for n, z, _ in partijen if n in st.session_state.geselecteerd)

st.subheader("Totaal aantal zetels")
st.metric("Totaal", totaal)

if totaal >= 76:
    st.success("🎉 76 of meer zetels — meerderheid!")
elif totaal > 0:
    st.info("Nog onder de 76.")
else:
    st.write("Selecteer partijen om te beginnen.")

if st.session_state.geselecteerd:
    st.write("Geselecteerd:", ", ".join(sorted(st.session_state.geselecteerd)))
