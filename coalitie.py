import streamlit as st

st.set_page_config(page_title="Coalitiebouwer (Freesers)", layout="wide")
st.title("Coalitiebouwer (Freesers)")

# --- Hard-coded zetels + kleuren ---
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

# --- State ---
if "geselecteerd" not in st.session_state:
    st.session_state.geselecteerd = set()

def toggle(naam: str):
    if naam in st.session_state.geselecteerd:
        st.session_state.geselecteerd.remove(naam)
    else:
        st.session_state.geselecteerd.add(naam)

# --- Afhandelen van klik via query param (stabiele API) ---
if "toggle" in st.query_params:
    toggle(st.query_params["toggle"])
    # param wissen en herstarten voor schone URL
    del st.query_params["toggle"]
    st.rerun()

st.header("Klik op een partij:")

# --- Stijl voor de gekleurde balk-knoppen ---
st.markdown("""
<style>
.party-btn {
  display: block;
  width: 100%;
  padding: 8px 12px;
  border-radius: 8px;
  border: none;
  color: white;
  font-weight: 600;
  font-size: 15px;
  text-align: left;
  cursor: pointer;
  margin-bottom: 8px;
}
.party-selected {
  box-shadow: inset 0 0 8px rgba(0,0,0,0.6);
}
</style>
""", unsafe_allow_html=True)

# --- 3 kolommen (mobiel valt vanzelf terug naar 1) ---
cols = st.columns(3)

for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 3]
    selected = naam in st.session_state.geselecteerd
    extra_cls = " party-selected" if selected else ""
    label = f"{'✅ ' if selected else ''}{naam} ({zetels})"

    # Klik zet ?toggle=<naam> in de URL; Streamlit leest die bovenin uit
    kolom.markdown(
        f"""
<button class="party-btn{extra_cls}" style="background:{kleur};"
        onclick="
          const p = new URLSearchParams(window.location.search);
          p.set('toggle', '{naam}');
          window.location.search = p.toString();
        ">
  {label}
</button>
""",
        unsafe_allow_html=True,
    )

# --- Totaal ---
totaal = sum(z for n, z, _ in partijen if n in st.session_state.geselecteerd)

st.subheader("Totaal aantal zetels")
st.metric("Totaal", totaal)

if totaal >= 76:
    st.success("🎉 76 of meer zetels — meerderheidscoalitie.")
elif totaal > 0:
    st.info("Nog geen meerderheid.")
else:
    st.write("Selecteer partijen om te beginnen.")

if st.session_state.geselecteerd:
    st.write("Geselecteerd:", ", ".join(sorted(st.session_state.geselecteerd)))
