try:
    import pandas as pd
    import streamlit as st

    df = pd.read_excel('verbos ingles.xlsx')

    st.title('Aprender Verbos en Ingles')

    # 1. Control de palabra actual
    if "guardar" not in st.session_state:
        st.session_state["guardar"] = df.sample()

    # 2. Control de versión (IMPORTANTE para resetear inputs)
    if "version" not in st.session_state:
        st.session_state["version"] = 0

    fila_aleatoria = st.session_state["guardar"]

    palabra = fila_aleatoria["infinitivo"].iloc[0]
    st.write(f"Verbo: {palabra}")

    # 3. Inputs (con key dinámico para evitar errores)
    respuesta_usuario = st.text_input(
        "Significado - Meaning",
        key=f"input_significado_{st.session_state['version']}"
    ).strip().lower()

    respuesta_pasado = st.text_input(
        "Pasado simple en ingles",
        key=f"input_pasado_{st.session_state['version']}"
    ).strip().lower()

    # 4. Validaciones
    correcto_significado = False
    correcto_pasado = False

    if respuesta_usuario:
        correcto_significado = respuesta_usuario == fila_aleatoria["español"].iloc[0]

        if correcto_significado:
            st.success("✔ significado correcto")
        else:
            st.error("❌ significado incorrecto")

    if respuesta_pasado:
        correcto_pasado = respuesta_pasado == fila_aleatoria["pasado"].iloc[0]

        if correcto_pasado:
            st.success("✔ pasado correcto")
        else:
            st.error("❌ pasado incorrecto")

    # 5. Resultado final
    if correcto_significado and correcto_pasado:
        st.success("🎉 ¡Todo correcto!")
        st.info(f"🗣 Pronunciación en padado simple: {fila_aleatoria['pronunciacion'].iloc[0]}")

    # 6. BOTÓN (abajo)
    if st.button("Siguiente palabra"):
        st.session_state["guardar"] = df.sample()
        st.session_state["version"] += 1
        st.rerun()
    
    #7. Boton Resultado:
    if st.button("Respuesta"):
        st.info("📘 Respuestas correctas:")

        st.write(f"Significado: {fila_aleatoria['español'].iloc[0]}")
        st.write(f"Pasado: {fila_aleatoria['pasado'].iloc[0]}")
        st.write(f"Pronunciación: {fila_aleatoria['pronunciacion'].iloc[0]}")
        
        
        

except Exception as error:
    print(error)