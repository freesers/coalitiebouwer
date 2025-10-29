st.header("Klik partijen om de coalitie te vormen")

# CSS voor grotere, touch-vriendelijke knoppen
st.markdown("""
<style>
.big-button button {
    padding: 14px 20px !important;
    border-radius: 10px !important;
    font-size: 18px !important;
    width: 100% !important;
}
.selected {
    box-shadow: 0 0 0 3px #222 inset;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(2)  # 2 per rij → grotere knoppen voor telefoon
for i, (naam, zetels, kleur) in enumerate(partijen):
    kolom = cols[i % 2]
    is_selected = naam in st.session_state.geselecteerd

    button_label = f"{naam} ({zetels})"

    # Template voor gekleurde container
    container_style = f"""
        background-color: {kleur};
        color: white;
        border-radius: 8px;
        padding: 6px;
        text-align: center;
        margin-bottom: 8px;
        {"box-shadow: 0 0 6px 2px #00000066 inset;" if is_selected else ""}
    """

    with kolom:
        st.markdown(f"<div style='{container_style}' class='big-button'>{button_label}</div>", unsafe_allow_html=True)
        st.button("Selecteer / Verwijder", key=naam, on_click=toggle, args=(naam,))
