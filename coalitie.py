import streamlit as st

st.set_page_config(page_title="Coalitiebouwer", layout="centered")
st.title("Coalitiebouwer (Mobiel)")

# Zetels
partijen = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

# Lees selectie via URL (stateless)
param = st.query_params.get("coalitie", "")
geselecteerd = set(filter(None, param.split(","))) if param else set()

# Totaal bovenaan
totaal = sum(z for n, z in partijen if n in geselecteerd)
st.metric("Totaal zetels", totaal)

if totaal >= 76:
    st.success("✅ Meerderheid!")
elif totaal > 0:
    st.info("Nog onder de 76 zetels")
else:
    st.write("Selecteer partijen hieronder:")

st.markdown("---")

# Link om selectie te wissen
st.markdown("**[🧼 Wis selectie](/)**")

st.markdown("---")

# Gewoon lijst met toggles als links → werkt altijd
for naam, zetels in partijen:
    select = naam in geselecteerd
    nieuwe = set(geselecteerd)
    if select:
        nieuwe.remove(naam)
    else:
        nieuwe.add(naam)
    new_param = ",".join(sorted(nieuwe))
    href = f"?coalitie={new_param}" if new_param else "/"
    label = f"{'☑' if select else '☐'} {naam} ({zetels})"
    st.markdown(f"[{label}]({href})")
