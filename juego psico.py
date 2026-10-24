
import streamlit as st
import random

st.set_page_config(
    page_title="Retos de la adultez",
    page_icon="🎮",
    layout="centered"
)

# PREGUNTAS EN EL ORDEN ORIGINAL
BANCO = [
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "1. ¿Qué caracteriza el desarrollo social durante la adultez?",
        "opciones": [
            "La pérdida total de relaciones sociales.",
            "La consolidación de vínculos familiares, laborales y comunitarios.",
            "La dependencia absoluta de otras personas.",
            "El abandono de responsabilidades."
        ],
        "correcta": "La consolidación de vínculos familiares, laborales y comunitarios.",
        "explicacion": "En la adultez se pueden consolidar vínculos familiares, laborales y comunitarios."
    },
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "2. La generatividad hace referencia a:",
        "opciones": [
            "El aislamiento social.",
            "La preocupación por contribuir al bienestar de las futuras generaciones.",
            "El deterioro cognitivo.",
            "La búsqueda de independencia económica."
        ],
        "correcta": "La preocupación por contribuir al bienestar de las futuras generaciones.",
        "explicacion": "La generatividad consiste en contribuir al bienestar de otras personas y de las generaciones futuras."
    },
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "3. ¿Cuál es un ejemplo de generatividad en la adultez?",
        "opciones": [
            "Evitar la participación comunitaria.",
            "Ignorar las necesidades de los demás.",
            "Compartir conocimientos y experiencias con personas más jóvenes.",
            "Reducir el contacto social."
        ],
        "correcta": "Compartir conocimientos y experiencias con personas más jóvenes.",
        "explicacion": "Compartir conocimientos ayuda a orientar y apoyar a las nuevas generaciones."
    },
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "4. El trabajo durante la adultez cumple una función social porque:",
        "opciones": [
            "Solo proporciona ingresos.",
            "Favorece la identidad, las relaciones sociales y la participación en la sociedad.",
            "Elimina las responsabilidades familiares.",
            "Impide el desarrollo personal."
        ],
        "correcta": "Favorece la identidad, las relaciones sociales y la participación en la sociedad.",
        "explicacion": "El trabajo también puede aportar identidad, relaciones y participación social."
    },
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "5. La cultura influye en la adultez porque:",
        "opciones": [
            "No afecta el comportamiento humano.",
            "Determina normas, valores y expectativas sociales.",
            "Solo influye en la infancia.",
            "Solo afecta a las personas mayores."
        ],
        "correcta": "Determina normas, valores y expectativas sociales.",
        "explicacion": "La cultura influye en los valores, las costumbres y las expectativas sociales."
    },
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "6. Una característica del envejecimiento activo es:",
        "opciones": [
            "El aislamiento.",
            "La participación continua en actividades sociales y culturales.",
            "El abandono de la comunidad.",
            "La dependencia permanente."
        ],
        "correcta": "La participación continua en actividades sociales y culturales.",
        "explicacion": "El envejecimiento activo favorece la participación y el bienestar."
    },
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "7. ¿Qué factor favorece el bienestar social en la adultez?",
        "opciones": [
            "La soledad.",
            "Las redes de apoyo familiar y comunitario.",
            "El aislamiento voluntario.",
            "El rechazo de las relaciones sociales."
        ],
        "correcta": "Las redes de apoyo familiar y comunitario.",
        "explicacion": "Las redes de apoyo brindan compañía, ayuda y sentido de pertenencia."
    },
    {
        "tipo": "abcd",
        "seccion": "🧠 Conocimientos",
        "pregunta": "8. Durante la adultez media es común que las personas:",
        "opciones": [
            "Carezcan de responsabilidades.",
            "Asuman múltiples roles familiares, laborales y sociales.",
            "Pierdan interés por los demás.",
            "Dejen de aprender."
        ],
        "correcta": "Asuman múltiples roles familiares, laborales y sociales.",
        "explicacion": "Es frecuente combinar responsabilidades familiares, laborales y sociales."
    },
    {
        "tipo": "vf",
        "seccion": "✅ Verdadero o Falso",
        "pregunta": "9. Las personas mayores pueden seguir contribuyendo activamente a la sociedad.",
        "opciones": ["Verdadero", "Falso"],
        "correcta": "Verdadero",
        "explicacion": "Las personas mayores pueden contribuir con su experiencia y participación."
    },
    {
        "tipo": "vf",
        "seccion": "✅ Verdadero o Falso",
        "pregunta": "10. La vejez implica necesariamente dependencia y pasividad.",
        "opciones": ["Verdadero", "Falso"],
        "correcta": "Falso",
        "explicacion": "La vejez no implica necesariamente dependencia o pasividad."
    },
    {
        "tipo": "vf",
        "seccion": "✅ Verdadero o Falso",
        "pregunta": "11. La participación en actividades culturales favorece la integración social.",
        "opciones": ["Verdadero", "Falso"],
        "correcta": "Verdadero",
        "explicacion": "Las actividades culturales favorecen el encuentro y la colaboración."
    },
    {
        "tipo": "vf",
        "seccion": "✅ Verdadero o Falso",
        "pregunta": "12. La generatividad solo ocurre cuando una persona tiene hijos.",
        "opciones": ["Verdadero", "Falso"],
        "correcta": "Falso",
        "explicacion": "La generatividad también se expresa enseñando, orientando y ayudando a la comunidad."
    },
    {
        "tipo": "abcd",
        "seccion": "🌍 Casos de la vida real",
        "pregunta": "13. Ana tiene 55 años y en su barrio organiza talleres para jóvenes que quieren emprender. ¿Qué está mostrando?",
        "opciones": ["Aislamiento.", "Generatividad.", "Dependencia.", "Desinterés."],
        "correcta": "Generatividad.",
        "explicacion": "Ana comparte conocimientos y ayuda a jóvenes: esto es generatividad."
    },
    {
        "tipo": "abcd",
        "seccion": "🌍 Casos de la vida real",
        "pregunta": "14. Don Pedro tiene 68 años, va al taller de pintura, sale con sus amigos y participa en la junta del barrio. ¿Qué representa esta situación?",
        "opciones": ["Que lo excluyeron.", "Envejecimiento activo.", "Aislamiento.", "Que está estancado."],
        "correcta": "Envejecimiento activo.",
        "explicacion": "Don Pedro mantiene relaciones y participa en actividades culturales y comunitarias."
    },
    {
        "tipo": "abcd",
        "seccion": "🌍 Casos de la vida real",
        "pregunta": "15. María debe cuidar a su papá mayor y, al mismo tiempo, ayudar a sus hijos que están en la universidad. ¿Qué vive María?",
        "opciones": [
            "Que no tiene nada que hacer.",
            "Que cumple muchos roles a la vez.",
            "Que depende de otros.",
            "Que está sola."
        ],
        "correcta": "Que cumple muchos roles a la vez.",
        "explicacion": "María combina diferentes responsabilidades familiares y de cuidado."
    },
    {
        "tipo": "abcd",
        "seccion": "🌍 Casos de la vida real",
        "pregunta": "16. ¿Cómo definirías mejor el desarrollo social en la adultez?",
        "opciones": [
            "Un proceso centrado exclusivamente en pérdidas y deterioro propios del envejecimiento.",
            "Una etapa de estabilidad donde no se presentan cambios sociales significativos.",
            "Un proceso de adaptación continua en el que la persona participa activamente en diversos contextos familiares, laborales, sociales y culturales.",
            "Una etapa caracterizada únicamente por los cambios físicos y biológicos del envejecimiento."
        ],
        "correcta": "Un proceso de adaptación continua en el que la persona participa activamente en diversos contextos familiares, laborales, sociales y culturales.",
        "explicacion": "El desarrollo social continúa durante la adultez e incluye adaptación y participación en distintos contextos."
    }
]


def comenzar():
    partida = []

    for pregunta in BANCO:
        copia = pregunta.copy()
        copia["opciones"] = pregunta["opciones"].copy()

        # Mezclar las opciones ABCD, no las preguntas.
        if copia["tipo"] == "abcd":
            random.shuffle(copia["opciones"])

        partida.append(copia)

    st.session_state.partida = partida
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.respuestas = {}
    st.session_state.jugando = True
    st.session_state.finalizado = False
    st.session_state.ronda = st.session_state.get("ronda", 0) + 1


if "jugando" not in st.session_state:
    st.session_state.jugando = False


# DISEÑO COLORIDO
st.markdown("""
<style>
.stApp {
    background: linear-gradient(140deg, #fff7ed, #fce7f3, #ede9fe);
}
.block-container {
    max-width: 850px;
    padding-top: 1.3rem;
}
.hero {
    background: linear-gradient(125deg, #7c3aed, #db2777, #f97316);
    padding: 30px 18px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0 12px 30px #7c3aed30;
    margin-bottom: 22px;
}
.hero h1 {
    color: white;
    font-size: 2.35rem;
}
.hero p {
    color: white;
    font-size: 1.05rem;
}
.card {
    background: white;
    border: 2px solid #f5d0fe;
    border-radius: 22px;
    padding: 22px;
    margin: 15px 0;
    box-shadow: 0 7px 22px #9d174d12;
}
div.stButton > button {
    border-radius: 14px;
    min-height: 48px;
    font-weight: 800;
}
div[data-testid="stRadio"] label {
    background: white;
    border: 1px solid #e9d5ff;
    border-radius: 13px;
    padding: 9px 12px;
    margin-bottom: 6px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <div>🎮 ¡APRENDE, JUEGA Y SUPERA EL RETO!</div>
    <h1>🌟 RETOS DE LA ADULTEZ 🌟</h1>
    <p>Desarrollo social y cultural · ¡Tú puedes lograrlo!</p>
</div>
""", unsafe_allow_html=True)


# PANTALLA INICIAL
if not st.session_state.jugando:
    st.markdown("## 🎉 ¡Bienvenido/a al desafío!")

    st.write(
        "Pon a prueba tus conocimientos sobre el desarrollo social "
        "y cultural durante la adultez."
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("📝 Preguntas", "16")
    c2.metric("⭐ Cada acierto", "10 puntos")
    c3.metric("🏆 Máximo", "160 puntos")

    st.markdown("""
    <div class="card">
      <h3>📚 ¿Cómo se juega?</h3>
      <p>🔤 <b>Preguntas de selección múltiple:</b> elige A, B, C o D.</p>
      <p>✅ <b>Verdadero o Falso:</b> decide si la afirmación es verdadera o falsa.</p>
      <p>🌍 <b>Casos de la vida real:</b> aplica lo aprendido a situaciones cotidianas.</p>
      <p>💡 Lee la explicación después de cada respuesta.</p>
    </div>
    """, unsafe_allow_html=True)

    st.text_input(
        "✍️ Tu nombre (opcional)",
        key="nombre_inicio",
        placeholder="Escribe tu nombre"
    )

    st.info(
        "✨ Las preguntas mantienen el orden del 1 al 16. "
        "Las opciones A, B, C y D se mezclan en cada partida."
    )

    if st.button("🚀 ¡EMPEZAR A JUGAR!", type="primary", use_container_width=True):
        st.session_state.nombre = st.session_state.get("nombre_inicio", "").strip()
        comenzar()
        st.rerun()


# PANTALLA DE PREGUNTAS
elif not st.session_state.finalizado:
    i = st.session_state.indice
    p = st.session_state.partida[i]
    total = len(st.session_state.partida)
    nombre = st.session_state.get("nombre", "") or "Jugador"

    col1, col2 = st.columns(2)
    col1.markdown(f"**👤 {nombre}**")
    col2.markdown(f"**⭐ {st.session_state.puntos} puntos**")

    st.progress(i / total, text=f"🚩 Pregunta {i + 1} de {total}")

    st.markdown(
        f'<div class="card">'
        f'<div style="color:#9333ea;font-weight:800;">{p["seccion"]}</div>'
        f'<h3 style="color:#3b0764;">{p["pregunta"]}</h3>'
        f'</div>',
        unsafe_allow_html=True
    )

    if p["tipo"] == "abcd":
        st.markdown("### 🔤 Elige tu respuesta: A, B, C o D")
        letras = ["A", "B", "C", "D"]
        opciones_visibles = [
            f"{letras[n]}) {opcion}"
            for n, opcion in enumerate(p["opciones"])
        ]
    else:
        st.markdown("### ✅ Elige: Verdadero o Falso")
        opciones_visibles = p["opciones"]

    ya_respondio = i in st.session_state.respuestas

    if not ya_respondio:
        eleccion = st.radio(
            "Opciones",
            opciones_visibles,
            index=None,
            key=f"respuesta_{st.session_state.ronda}_{i}",
            label_visibility="collapsed"
        )

        if st.button("💥 ¡COMPROBAR RESPUESTA!", type="primary", use_container_width=True):
            if eleccion is None:
                st.warning("👀 ¡Selecciona una opción antes de continuar!")
            else:
                texto = (
                    eleccion.split(") ", 1)[1]
                    if p["tipo"] == "abcd"
                    else eleccion
                )

                correcta = texto == p["correcta"]

                st.session_state.respuestas[i] = {
                    "eleccion": texto,
                    "correcta": correcta
                }

                if correcta:
                    st.session_state.puntos += 10

                st.rerun()

    else:
        resultado = st.session_state.respuestas[i]

        if resultado["correcta"]:
            st.success("🎉 ¡BRAVO! ¡Respuesta correcta! +10 puntos.")
        else:
            st.error("💪 ¡No te rindas! Aprende y sigue adelante.")

        st.markdown(f'**🎯 Respuesta correcta:** {p["correcta"]}')
        st.info(f'💡 **Aprende algo nuevo:** {p["explicacion"]}')

        if i < total - 1:
            if st.button("➡️ ¡VAMOS CON LA SIGUIENTE!", type="primary", use_container_width=True):
                st.session_state.indice += 1
                st.rerun()
        else:
            if st.button("🏆 ¡VER MI RESULTADO FINAL!", type="primary", use_container_width=True):
                st.session_state.finalizado = True
                st.rerun()


# PANTALLA FINAL
else:
    total = len(st.session_state.partida)
    puntos = st.session_state.puntos
    nombre = st.session_state.get("nombre", "").strip()

    correctas = sum(
        1 for r in st.session_state.respuestas.values()
        if r["correcta"]
    )
    porcentaje = round(correctas / total * 100)

    st.balloons()
    st.markdown("## 🏆🎊 ¡RETO COMPLETADO! 🎊🏆")

    if nombre:
        st.markdown(f"### ¡Excelente esfuerzo, {nombre}!")

    st.markdown(
        f'<div class="hero">'
        f'<h1>{puntos} / 160 puntos</h1>'
        f'<p>Respuestas correctas: {correctas} de {total} · {porcentaje}%</p>'
        f'</div>',
        unsafe_allow_html=True
    )

    if porcentaje >= 85:
        st.success("🌟 ¡INCREÍBLE! Dominas muy bien el tema.")
    elif porcentaje >= 60:
        st.info("👏 ¡MUY BIEN! Sigue reforzando tus conocimientos.")
    else:
        st.warning("💜 ¡TÚ PUEDES! Cada intento es una oportunidad para aprender.")

    with st.expander("📖 Revisar mis respuestas"):
        for n, p in enumerate(st.session_state.partida):
            r = st.session_state.respuestas.get(n, {})
            icono = "✅" if r.get("correcta") else "❌"

            st.markdown(f'**{icono} {p["pregunta"]}**')
            st.write(f'Tu respuesta: {r.get("eleccion", "Sin respuesta")}')
            st.write(f'Respuesta correcta: {p["correcta"]}')
            st.caption(p["explicacion"])
            st.divider()

    if st.button("🔁 ¡JUGAR OTRA VEZ!", type="primary", use_container_width=True):
        comenzar()
        st.rerun()

st.divider()
st.caption("💜 Proyecto educativo · Desarrollo social y cultural en la adultez")
