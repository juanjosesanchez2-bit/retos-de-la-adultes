
import streamlit as st
import random

st.set_page_config(
    page_title="Retos de la adultez",
    page_icon="🎮"
)

PREGUNTAS = [
    {
        "p": "¿Qué puede cambiar en las relaciones sociales durante la adultez?",
        "o": [
            "Las relaciones nunca cambian",
            "Se fortalecen vínculos importantes y cambian prioridades",
            "Todas las amistades desaparecen",
            "La familia deja de importar"
        ],
        "c": 1,
        "e": "Las personas pueden reorganizar su tiempo y fortalecer sus vínculos."
    },
    {
        "p": "¿Qué significa desarrollo cultural en la adultez?",
        "o": [
            "Dejar de aprender",
            "Aceptar solo las costumbres propias",
            "Construir y adaptar valores e identidad durante la vida",
            "Cambiar de país obligatoriamente"
        ],
        "c": 2,
        "e": "La identidad cultural evoluciona con las experiencias y el aprendizaje."
    },
    {
        "p": "Participar en actividades del barrio favorece:",
        "o": [
            "La participación comunitaria",
            "El aislamiento",
            "El desinterés",
            "La incomunicación"
        ],
        "c": 0,
        "e": "La participación comunitaria fortalece la cooperación y la pertenencia."
    },
    {
        "p": "¿Cómo se logra un equilibrio entre trabajo y vida personal?",
        "o": [
            "Trabajando todo el día",
            "Ignorando las responsabilidades",
            "Organizando el tiempo para trabajo, descanso y relaciones",
            "Evitando todo compromiso"
        ],
        "c": 2,
        "e": "La organización permite atender diferentes responsabilidades."
    },
    {
        "p": "¿Cómo puede influir la cultura en la adultez?",
        "o": [
            "No influye nunca",
            "Influye en costumbres, celebraciones y relaciones",
            "Determina totalmente la personalidad",
            "Impide aprender"
        ],
        "c": 1,
        "e": "La cultura influye en hábitos y valores, pero cada persona tiene sus propias experiencias."
    },
    {
        "p": "Respetar una tradición diferente demuestra:",
        "o": [
            "Intolerancia",
            "Falta de identidad",
            "Respeto por la diversidad cultural",
            "Desinterés"
        ],
        "c": 2,
        "e": "Respetar la diversidad significa reconocer distintas costumbres y formas de vida."
    },
    {
        "p": "¿Qué ayuda a mantener buenas relaciones sociales?",
        "o": [
            "Comunicarse y respetar límites",
            "Exigir que todos piensen igual",
            "Evitar hablar",
            "Alejarse de todos"
        ],
        "c": 0,
        "e": "La comunicación y el respeto ayudan a cuidar las relaciones."
    },
    {
        "p": "¿Se puede seguir aprendiendo durante la adultez?",
        "o": [
            "No, después de los 30 años es imposible",
            "Solo se aprende durante la infancia",
            "Sí, durante toda la vida",
            "Solo en la universidad"
        ],
        "c": 2,
        "e": "El aprendizaje puede continuar en cualquier etapa de la vida."
    },
    {
        "p": "Las redes de apoyo familiar y social pueden:",
        "o": [
            "Impedir tomar decisiones",
            "Contribuir al bienestar y ayudar ante dificultades",
            "Eliminar todas las responsabilidades",
            "Ser siempre innecesarias"
        ],
        "c": 1,
        "e": "Las redes de apoyo pueden ayudar a afrontar responsabilidades y cambios."
    },
    {
        "p": "El desarrollo en la adultez depende de:",
        "o": [
            "La edad solamente",
            "Tener un trabajo específico",
            "Factores personales, sociales, económicos y culturales",
            "Vivir siempre en el mismo lugar"
        ],
        "c": 2,
        "e": "Cada persona vive la adultez de forma diferente según su contexto y experiencias."
    }
]

def iniciar():
    st.session_state.preguntas = random.sample(PREGUNTAS, len(PREGUNTAS))
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.respuesta = None
    st.session_state.terminado = False
    st.session_state.iniciado = True

if "iniciado" not in st.session_state:
    st.session_state.iniciado = False

st.title("🎮 Retos de la adultez")
st.subheader("Desarrollo social y cultural")
st.write("¡Demuestra lo que sabes y aprende jugando!")

if not st.session_state.iniciado:
    st.write("Responde 10 preguntas sobre familia, trabajo, relaciones y cultura.")
    st.text_input("Nombre del jugador (opcional)", key="nombre")
    if st.button("🚀 Empezar juego", type="primary"):
        iniciar()
        st.rerun()

elif not st.session_state.terminado:
    i = st.session_state.indice
    pregunta = st.session_state.preguntas[i]

    st.progress((i + 1) / len(st.session_state.preguntas))
    st.caption(f"Pregunta {i + 1} de 10 | Puntaje: {st.session_state.puntos}/100")
    st.subheader(pregunta["p"])

    if st.session_state.respuesta is None:
        eleccion = st.radio(
            "Selecciona una respuesta:",
            pregunta["o"],
            index=None,
            key=f"opcion_{i}"
        )

        if st.button("Comprobar respuesta", type="primary"):
            if eleccion is None:
                st.warning("Selecciona una respuesta primero.")
            else:
                st.session_state.respuesta = eleccion
                if eleccion == pregunta["o"][pregunta["c"]]:
                    st.session_state.puntos += 10
                st.rerun()
    else:
        correcta = pregunta["o"][pregunta["c"]]

        if st.session_state.respuesta == correcta:
            st.success("¡Correcto! Ganaste 10 puntos.")
        else:
            st.error("Respuesta incorrecta.")

        st.write("**Respuesta correcta:**", correcta)
        st.info(pregunta["e"])

        if st.button("Siguiente pregunta ➡️", type="primary"):
            if i == 9:
                st.session_state.terminado = True
            else:
                st.session_state.indice += 1
                st.session_state.respuesta = None
            st.rerun()

else:
    puntos = st.session_state.puntos
    nombre = st.session_state.get("nombre", "").strip()

    st.balloons()
    st.header("🏆 ¡Juego terminado!")
    if nombre:
        st.write(f"Jugador: **{nombre}**")
    st.metric("Puntaje final", f"{puntos}/100")

    if puntos >= 80:
        st.success("¡Excelente! Comprendes muy bien el tema.")
    elif puntos >= 50:
        st.info("¡Buen trabajo! Sigue reforzando tus conocimientos.")
    else:
        st.warning("¡Sigue aprendiendo! Puedes intentarlo otra vez.")

    st.write(
        "La adultez es una etapa en la que las relaciones, "
        "la participación social y la identidad cultural "
        "pueden seguir evolucionando."
    )

    if st.button("🔄 Jugar de nuevo"):
        iniciar()
        st.rerun()

st.divider()
st.caption("Proyecto educativo sobre el desarrollo social y cultural en la adultez.")
