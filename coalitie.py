import streamlit as st

st.set_page_config(page_title="Coalitiebouwer (Freesers)", layout="wide")
st.title("Coalitiebouwer")

# Zetels
partijen = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

# Bewaar (optioneel) set met geselecteerde namen
if "geselecteerd" not in st.session_state:
    st.session_state.geselecteerd = set()

# ---- Placeholders voor UI bovenaan (vullen we na de checkboxes) ----
metric_ph = st.empty()
status_ph = st.empty()
selected_ph = st.empty()
st.markdown("---")

# ---- Partijenselectors ----
cols = st.columns(3)
nieuwe_selectie = set()

for i, (naam, zetels) in enumerate(partijen):
    col = cols[i % 3]
    # standaardwaarde: huidige selectie
    default = naam in st.session_state.geselecteerd
    checked = col.checkbox(f"{naam} ({zetels})", value=default, key=f"cb_{naam}")
    if checked:
        nieuwe_selectie.add(naam)

# Update state in één keer, ná de checkboxes
st.session_state.geselecteerd = nieuwe_selectie

# ---- Nu pas: totaal en bovenste UI invullen ----
totaal = sum(z for n, z in partijen if n in st.session_state.geselecteerd)

metric_ph.metric("Totaal", totaal)

if totaal >= 76:
    status_ph.success("🎉 76 of meer zetels — meerderheidscoalitie.")
elif totaal > 0:
    status_ph.info("Nog niet boven de 76.")
else:
    status_ph.write("Selecteer partijen om te beginnen.")

if st.session_state.geselecteerd:
    selected_ph.write("Geselecteerd: " + ", ".join(sorted(st.session_state.geselecteerd)))
else:
    selected_ph.empty()
