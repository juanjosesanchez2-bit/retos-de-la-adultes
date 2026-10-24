
import streamlit as st
import random

st.set_page_config(
    page_title="Retos de la adultez",
    page_icon="🌱",
    layout="centered"
)

# BANCO DE LAS 16 PREGUNTAS
BANCO = [
    ("Conocimientos",
     "¿Qué caracteriza el desarrollo social durante la adultez?",
     ["La pérdida total de relaciones sociales.",
      "La consolidación de vínculos familiares, laborales y comunitarios.",
      "La dependencia absoluta de otras personas.",
      "El abandono de responsabilidades."],
     1,
     "En la adultez se pueden consolidar vínculos familiares, laborales y comunitarios."),

    ("Conocimientos",
     "La generatividad hace referencia a:",
     ["El aislamiento social.",
      "La preocupación por contribuir al bienestar de las futuras generaciones.",
      "El deterioro cognitivo.",
      "La búsqueda de independencia económica."],
     1,
     "La generatividad consiste en contribuir al bienestar de otras personas y generaciones futuras."),

    ("Conocimientos",
     "¿Cuál es un ejemplo de generatividad en la adultez?",
     ["Evitar la participación comunitaria.",
      "Ignorar las necesidades de los demás.",
      "Compartir conocimientos y experiencias con personas más jóvenes.",
      "Reducir el contacto social."],
     2,
     "Compartir experiencias permite orientar a otras personas y transmitir conocimientos."),

    ("Conocimientos",
     "El trabajo durante la adultez cumple una función social porque:",
     ["Solo proporciona ingresos.",
      "Favorece la identidad, las relaciones sociales y la participación en la sociedad.",
      "Elimina las responsabilidades familiares.",
      "Impide el desarrollo personal."],
     1,
     "El trabajo puede aportar identidad, relaciones sociales y participación en la sociedad."),

    ("Conocimientos",
     "La cultura influye en la adultez porque:",
     ["No afecta el comportamiento humano.",
      "Determina normas, valores y expectativas sociales.",
      "Solo influye en la infancia.",
      "Solo afecta a las personas mayores."],
     1,
     "La cultura influye en las costumbres, valores y expectativas sociales."),

    ("Conocimientos",
     "Una característica del envejecimiento activo es:",
     ["El aislamiento.",
      "La participación continua en actividades sociales y culturales.",
      "El abandono de la comunidad.",
      "La dependencia permanente."],
     1,
     "El envejecimiento activo promueve la participación, la salud y el bienestar."),

    ("Conocimientos",
     "¿Qué factor favorece el bienestar social en la adultez?",
     ["La soledad.",
      "Las redes de apoyo familiar y comunitario.",
      "El aislamiento voluntario.",
      "El rechazo de las relaciones sociales."],
     1,
     "Las redes de apoyo ofrecen compañía, ayuda y sentido de pertenencia."),

    ("Conocimientos",
     "Durante la adultez media es común que las personas:",
     ["Carezcan de responsabilidades.",
      "Asuman múltiples roles familiares, laborales y sociales.",
      "Pierdan interés por los demás.",
      "Dejen de aprender."],
     1,
     "Es frecuente combinar diferentes responsabilidades familiares, laborales y sociales."),

    ("Verdadero o falso",
     "Las personas mayores pueden seguir contribuyendo activamente a la sociedad.",
     ["Verdadero", "Falso"],
     0,
     "Las personas mayores pueden contribuir con su experiencia, conocimientos y participación."),

    ("Verdadero o falso",
     "La vejez implica necesariamente dependencia y pasividad.",
     ["Verdadero", "Falso"],
     1,
     "La vejez no significa necesariamente dependencia. Cada persona tiene experiencias y capacidades diferentes."),

    ("Verdadero o falso",
     "La participación en actividades culturales favorece la integración social.",
     ["Verdadero", "Falso"],
     0,
     "Las actividades culturales crean oportunidades de encuentro y colaboración."),

    ("Verdadero o falso",
     "La generatividad solo ocurre cuando una persona tiene hijos.",
     ["Verdadero", "Falso"],
     1,
     "La generatividad también se manifiesta enseñando, orientando y ayudando a la comunidad."),

    ("Casos reales",
     "Ana tiene 55 años y en su barrio organiza talleres para jóvenes que quieren emprender. ¿Qué está mostrando?",
     ["Aislamiento.", "Generatividad.", "Dependencia.", "Desinterés."],
     1,
     "Ana comparte conocimientos y ayuda a las nuevas generaciones. Esto es generatividad."),

    ("Casos reales",
     "Don Pedro tiene 68 años, va al taller de pintura, sale con sus amigos y participa en la junta del barrio. ¿Qué representa?",
     ["Que lo excluyeron.", "Envejecimiento activo.", "Aislamiento.", "Que está estancado."],
     1,
     "Don Pedro mantiene relaciones, participa en actividades y se integra en su comunidad."),

    ("Casos reales",
     "María cuida a su papá mayor y también ayuda a sus hijos que están en la universidad. ¿Qué vive María?",
     ["Que no tiene nada que hacer.",
      "Que cumple muchos roles a la vez.",
      "Que depende de otros.",
      "Que está sola."],
     1,
     "María combina diferentes responsabilidades familiares y de cuidado."),

    ("Casos reales",
     "¿Cómo definirías mejor el desarrollo social en la adultez?",
     ["Un proceso centrado exclusivamente en pérdidas y deterioro.",
      "Una etapa estable sin cambios sociales significativos.",
      "Un proceso de adaptación continua en contextos familiares, laborales, sociales y culturales.",
      "Una etapa caracterizada únicamente por cambios físicos y biológicos."],
     2,
     "El desarrollo social continúa durante la adultez mediante la adaptación y participación en distintos contextos.")
]


# PREPARAR UNA PARTIDA NUEVA
def nueva_partida():
    preguntas = []

    for categoria, pregunta, opciones, indice_correcto, explicacion in BANCO:
        opciones_mezcladas = opciones.copy()
        random.shuffle(opciones_mezcladas)

        preguntas.append({
            "categoria": categoria,
            "pregunta": pregunta,
            "opciones": opciones_mezcladas,
            "correcta": opciones[indice_correcto],
            "explicacion": explicacion
        })

    random.shuffle(preguntas)

    st.session_state.partida = preguntas
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.respuestas = {}
    st.session_state.terminado = False
    st.session_state.jugando = True
    st.session_state.numero_partida = (
        st.session_state.get("numero_partida", 0) + 1
    )


# ESTILOS DE LA INTERFAZ
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f0fdfa, #eef2ff);
}
.block-container {
    max-width: 850px;
    padding-top: 1.5rem;
}
.portada {
    background: linear-gradient(135deg, #123b46, #167d75, #60a99a);
    padding: 32px 20px;
    border-radius: 24px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px #123b4625;
}
.portada h1 {
    color: white;
    font-size: 2.3rem;
}
.portada p {
    color: #e5fffa;
}
.tarjeta {
    background: white;
    border: 1px solid #dce7e8;
    border-radius: 18px;
    padding: 22px;
    margin: 15px 0;
    box-shadow: 0 5px 18px #123b4610;
}
div.stButton > button {
    border-radius: 12px;
    min-height: 45px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# CABECERA
st.markdown("""
<div class="portada">
    <div>🎯 JUEGO EDUCATIVO INTERACTIVO</div>
    <h1>🌱 Retos de la adultez</h1>
    <p>Desarrollo social y cultural · Aprende jugando</p>
</div>
""", unsafe_allow_html=True)


# PANTALLA DE INICIO
if "jugando" not in st.session_state:
    st.session_state.jugando = False

if not st.session_state.jugando:
    st.markdown("## ¡Bienvenido/a!")
    st.write(
        "Resuelve preguntas y casos de la vida real sobre "
        "la familia, el trabajo, la generatividad y la cultura."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Preguntas", "16")
    col2.metric("Por acierto", "10 puntos")
    col3.metric("Puntaje máximo", "160")

    st.text_input(
        "Nombre del jugador (opcional)",
        key="nombre",
        placeholder="Escribe tu nombre"
    )

    st.info(
        "Las preguntas y sus opciones se mezclan en cada partida. "
        "Las respuestas correctas pueden aparecer en A, B, C o D."
    )

    if st.button(
        "🚀 COMENZAR JUEGO",
        type="primary",
        use_container_width=True
    ):
        nueva_partida()
        st.rerun()


# PANTALLA DE JUEGO
elif not st.session_state.terminado:

    i = st.session_state.indice
    pregunta = st.session_state.partida[i]
    total = len(st.session_state.partida)
    nombre = st.session_state.get("nombre", "").strip()

    col1, col2 = st.columns(2)
    col1.caption(f"👤 {nombre if nombre else 'Jugador'}")
    col2.caption(f"⭐ Puntaje: {st.session_state.puntos}")

    st.progress(
        (i + 1) / total,
        text=f"Pregunta {i + 1} de {total}"
    )

    st.markdown(
        f'<div class="tarjeta">'
        f'<small>{pregunta["categoria"].upper()}</small>'
        f'<h3>{pregunta["pregunta"]}</h3>'
        f'</div>',
        unsafe_allow_html=True
    )

    respondidas = st.session_state.respuestas
    ya_respondio = i in respondidas

    # Crear opciones con letras A, B, C y D.
    # En verdadero/falso solo aparecen las dos opciones.
    letras = ["A", "B", "C", "D"]
    opciones = pregunta["opciones"]

    if not ya_respondio:
        opciones_visibles = [
            f"{letras[n]}) {opcion}"
            for n, opcion in enumerate(opciones)
        ]

        clave = (
            f"respuesta_{st.session_state.numero_partida}_{i}"
        )

        eleccion = st.radio(
            "Selecciona tu respuesta:",
            opciones_visibles,
            index=None,
            key=clave
        )

        if st.button(
            "COMPROBAR RESPUESTA",
            type="primary",
            use_container_width=True
        ):
            if eleccion is None:
                st.warning("Primero debes seleccionar una respuesta.")
            else:
                texto_elegido = eleccion.split(") ", 1)[1]
                correcta = texto_elegido == pregunta["correcta"]

                st.session_state.respuestas[i] = {
                    "eleccion": texto_elegido,
                    "correcta": correcta
                }

                if correcta:
                    st.session_state.puntos += 10

                st.rerun()

    else:
        resultado = respondidas[i]

        if resultado["correcta"]:
            st.success("🎉 ¡Respuesta correcta! Ganaste 10 puntos.")
        else:
            st.error("❌ Respuesta incorrecta. ¡Sigue aprendiendo!")

        st.markdown(
            f'**Respuesta correcta:** {pregunta["correcta"]}'
        )
        st.info(pregunta["explicacion"])

        if i < total - 1:
            if st.button(
                "SIGUIENTE PREGUNTA ➜",
                type="primary",
                use_container_width=True
            ):
                st.session_state.indice += 1
                st.rerun()
        else:
            if st.button(
                "🏆 VER RESULTADO FINAL",
                type="primary",
                use_container_width=True
            ):
                st.session_state.terminado = True
                st.rerun()


# RESULTADOS
elif st.session_state.terminado:

    puntos = st.session_state.puntos
    total = len(st.session_state.partida)
    correctas = sum(
        1 for r in st.session_state.respuestas.values()
        if r["correcta"]
    )
    porcentaje = round(correctas / total * 100)
    nombre = st.session_state.get("nombre", "").strip()

    st.balloons()
    st.markdown("## 🏆 ¡Juego terminado!")

    if nombre:
        st.write(f"¡Buen trabajo, **{nombre}**!")

    st.markdown(
        f'<div class="tarjeta" style="text-align:center;">'
        f'<h3>Tu puntaje final</h3>'
        f'<h1 style="color:#167d75;font-size:3.5rem;">'
        f'{puntos}/160</h1>'
        f'<p>{correctas} de {total} respuestas correctas</p>'
        f'<p>Resultado: {porcentaje}%</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    if porcentaje >= 85:
        st.success("🌟 ¡Excelente! Dominas el tema.")
    elif porcentaje >= 60:
        st.info("👏 ¡Buen trabajo! Sigue reforzando tus conocimientos.")
    else:
        st.warning("📚 Sigue practicando y revisa las explicaciones.")

    with st.expander("📋 Revisar respuestas"):
        for n, p in enumerate(st.session_state.partida):
            r = st.session_state.respuestas.get(n, {})
            icono = "✅" if r.get("correcta") else "❌"

            st.markdown(f'{icono} **{n + 1}. {p["pregunta"]}**')
            st.write(f'Tu respuesta: {r.get("eleccion", "Sin respuesta")}')
            st.write(f'Respuesta correcta: {p["correcta"]}')
            st.caption(p["explicacion"])
            st.divider()

    if st.button(
        "🔄 JUGAR NUEVAMENTE",
        type="primary",
        use_container_width=True
    ):
        nueva_partida()
        st.rerun()

st.divider()
st.caption(
    "Proyecto educativo · Desarrollo social y cultural en la adultez"
)
