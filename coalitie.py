import streamlit as st

st.set_page_config(page_title="Coalitiebouwer", layout="wide")
st.title("Coalitiebouwer")

partijen = [
    ("PVV", 26),
    ("GL/PvdA", 24),
    ("D66", 23),
    ("CDA", 20),
    ("VVD", 17),
    ("JA21", 10),
    ("FvD", 5),
    ("SP", 4),
    ("BBB", 4),
    ("Denk", 3),
    ("PvdD", 3),
    ("SGP", 3),
    ("CU", 3),
    ("50PLUS", 2),
    ("Volt", 2),
    ("NSC", 1),
]

# ---- Lees coalitie uit de URL ----
param = st.query_params.get("coalitie", "")
geselecteerd = set(param.split(",")) if param else set()

# ---- Bovenste UI ----
totaal = sum(z for n, z in partijen if n in geselecteerd)
st.metric("Totaal", totaal)

if totaal >= 76:
    st.success("🎉 Meerderheid")
elif totaal > 0:
    st.info("Nog onder de 76")
else:
    st.write("Selecteer partijen om te beginnen")

if geselecteerd:
    st.write("Geselecteerd:", ", ".join(sorted(geselecteerd)))

st.markdown("---")

# ---- Partijselectie ----
cols = st.columns(3)

for i, (naam, zetels) in enumerate(partijen):
    col = cols[i % 3]
    checked = naam in geselecteerd

    new_set = set(geselecteerd)
    if checked:
        new_set.remove(naam)
    else:
        new_set.add(naam)

    # nieuwe URL-parameter
    new_param = ",".join(sorted(new_set)) if new_set else ""

    label = f"{naam} ({zetels})"
    # Knop die enkel de URL wijzigt → geen cookies nodig
    col.button(label, on_click=lambda v=new_param: st.query_params.update(coalitie=v))
