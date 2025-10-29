import streamlit as st

st.set_page_config(page_title="Coalitie-tool", layout="wide")
st.title("Coalitiebouwer (Freesers)")

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

st.header("Klik op een partij:")

# 3 kolommen → automatisch 1 op mobiel
cols = st.columns(3)

for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 3]
    geselecteerd = naam in st.session_state.geselecteerd

    label = f"{'✅ ' if geselecteerd else ''}{naam} ({zetels})"

    # CSS: kleur + geselecteerde schaduw, specifiek per knop key
    st.markdown(
        f"""
        <style>
        div[data-testid="stButton"] button[key="{naam}"] {{
            background-color: {kleur} !important;
            color: white !important;
            border-radius: 8px !important;
            width: 100% !important;
            padding: 8px 10px !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            border: none !important;
            box-shadow: {"inset 0 0 8px rgba(0,0,0,0.6)" if geselecteerd else "none"} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    with kolom:
        st.button(label, key=naam, on_click=toggle, args=(naam,))

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
