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

# UI
st.header("Klik partijen om de coalitie te vormen")

cols = st.columns(4)
for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 4]
    geselecteerd = naam in st.session_state.geselecteerd
    style = f"background-color:{kleur}; padding:6px; border-radius:6px; color:white;"

    label = f"✅ {naam} ({zetels})" if geselecteerd else f"{naam} ({zetels})"

    # kleur direct achter knop via HTML (knoppen zelf zijn niet stylebaar)
    kolom.markdown(f"<div style='{style}'>{label}</div>", unsafe_allow_html=True)
    kolom.button(label, on_click=toggle, args=(naam,))

# Berekening
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
