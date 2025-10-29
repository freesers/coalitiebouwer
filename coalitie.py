import streamlit as st

st.set_page_config(page_title="Coalitiebouwer", layout="wide")
st.title("Coalitiebouwer")

partijen = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

# 1) Lees selectie uit URL
param = st.query_params.get("coalitie", "")
geselecteerd = set(param.split(",")) if param else set()

# 2) Toon UI bovenaan
totaal = sum(z for n, z in partijen if n in geselecteerd)
st.metric("Totaal", totaal)

if totaal >= 76:
    st.success("🎉 Meerderheid!")
elif totaal > 0:
    st.info("Nog onder de 76")
else:
    st.write("Selecteer partijen om te beginnen")

if geselecteerd:
    st.write("Geselecteerd:", ", ".join(sorted(geselecteerd)))

st.markdown("---")

# 3) Toon checkboxes → verzamel nieuwe selectie
cols = st.columns(3)
nieuwe = set()

for i, (naam, zetels) in enumerate(partijen):
    col = cols[i % 3]
    checked = col.checkbox(f"{naam} ({zetels})", value=(naam in geselecteerd), key=f"cb_{naam}")
    if checked:
        nieuwe.add(naam)

# 4) Pas **na** checkboxes pas URL aan
if nieuwe != geselecteerd:
    if nieuwe:
        st.query_params.update(coalitie=",".join(sorted(nieuwe)))
    else:
        st.query_params.pop("coalitie", None)
