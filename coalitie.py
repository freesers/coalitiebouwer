import streamlit as st

st.set_page_config(page_title="Coalitiebouwer", layout="wide")
st.title("Coalitiebouwer")

# ---- Partijen en zetels ----
partijen = [
    ("PVV", 26), ("GL/PvdA", 24), ("D66", 23), ("CDA", 20),
    ("VVD", 17), ("JA21", 10), ("FvD", 5), ("SP", 4),
    ("BBB", 4), ("Denk", 3), ("PvdD", 3), ("SGP", 3),
    ("CU", 3), ("50PLUS", 2), ("Volt", 2), ("NSC", 1),
]

# ---- Lees huidige selectie uit de URL (stateless) ----
param = st.query_params.get("coalitie", "")
geselecteerd = set(filter(None, param.split(","))) if param else set()

# ---- Totaal bovenaan ----
totaal = sum(z for n, z in partijen if n in geselecteerd)
st.metric("Totaal", totaal)
if totaal >= 76:
    st.success("🎉 Meerderheid!")
elif totaal > 0:
    st.info("Nog onder de 76.")
else:
    st.write("Selecteer partijen hieronder en klik op **Update**.")

if geselecteerd:
    st.write("Geselecteerd:", ", ".join(sorted(geselecteerd)))

st.markdown("---")

# ---- Formulier: checkboxes + één submit (voorkomt mobiele render-loops) ----
with st.form("coalitie_form", clear_on_submit=False):
    cols = st.columns(3)
    # toon checkboxes met huidige URL-selectie als default
    for i, (naam, zetels) in enumerate(partijen):
        col = cols[i % 3]
        col.checkbox(
            f"{naam} ({zetels})",
            value=(naam in geselecteerd),
            key=f"cb_{naam}"
        )

    submitted = st.form_submit_button("Update")

# ---- Na submit: schrijf selectie één keer naar de URL (triggert rerun automatisch) ----
if submitted:
    nieuwe = sorted(
        n for (n, _) in [(p[0], p[1]) for p in partijen]
        if st.session_state.get(f"cb_{n}", False)
    )
    if nieuwe:
        st.query_params.update(coalitie=",".join(nieuwe))
    else:
        # leeg maken = coalitie-param verwijderen
        st.query_params.pop("coalitie", None)
