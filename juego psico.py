import tkinter as tk
from tkinter import messagebox
import random

# Juego educativo: Desarrollo social y cultural en la adultez

PREGUNTAS = [
    {
        "pregunta": "¿Qué puede cambiar en las relaciones sociales durante la adultez?",
        "opciones": [
            "Las relaciones nunca cambian",
            "Se pueden fortalecer vínculos importantes y cambiar las prioridades",
            "Todas las amistades desaparecen",
            "La familia deja de ser importante para todos"
        ],
        "correcta": 1,
        "explicacion": "En la adultez, las personas suelen reorganizar su tiempo y fortalecer los vínculos que consideran significativos."
    },
    {
        "pregunta": "¿Qué significa desarrollo cultural en la adultez?",
        "opciones": [
            "Dejar de aprender sobre otras culturas",
            "Aceptar únicamente las costumbres propias",
            "Construir y adaptar valores, costumbres e identidad a lo largo de la vida",
            "Cambiar obligatoriamente de país"
        ],
        "correcta": 2,
        "explicacion": "La identidad cultural puede mantenerse y también enriquecerse mediante nuevas experiencias y el contacto con otras personas."
    },
    {
        "pregunta": "Una persona adulta empieza a participar en actividades de su barrio. ¿Qué aspecto desarrolla?",
        "opciones": [
            "Participación comunitaria",
            "Aislamiento social",
            "Desinterés cultural",
            "Dependencia tecnológica"
        ],
        "correcta": 0,
        "explicacion": "Participar en actividades comunitarias puede favorecer el sentido de pertenencia y la cooperación."
    },
    {
        "pregunta": "¿Cuál es un ejemplo de equilibrio entre trabajo y vida personal?",
        "opciones": [
            "Trabajar todo el tiempo y abandonar los vínculos personales",
            "Ignorar las responsabilidades laborales",
            "Organizar el tiempo para atender responsabilidades, descanso y relaciones",
            "Evitar cualquier compromiso"
        ],
        "correcta": 2,
        "explicacion": "Organizar el tiempo ayuda a atender distintas responsabilidades y cuidar el bienestar personal."
    },
    {
        "pregunta": "¿Cómo puede influir la cultura en la vida adulta?",
        "opciones": [
            "No influye en ninguna decisión",
            "Puede influir en las costumbres familiares, celebraciones y formas de relacionarse",
            "Determina exactamente la personalidad de cada persona",
            "Impide que las personas aprendan cosas nuevas"
        ],
        "correcta": 1,
        "explicacion": "La cultura influye en hábitos y valores, aunque cada persona también interpreta y adapta esas influencias."
    },
    {
        "pregunta": "Una persona adulta escucha con respeto una tradición diferente a la suya. ¿Qué demuestra?",
        "opciones": [
            "Intolerancia",
            "Falta de identidad",
            "Respeto por la diversidad cultural",
            "Desinterés por la sociedad"
        ],
        "correcta": 2,
        "explicacion": "Respetar la diversidad implica reconocer que existen distintas costumbres, creencias y formas de vida."
    },
    {
        "pregunta": "¿Cuál es una forma saludable de mantener las relaciones sociales en la adultez?",
        "opciones": [
            "Comunicarse, compartir tiempo y respetar límites",
            "Evitar expresar opiniones",
            "Exigir que los demás piensen igual",
            "Dejar de conocer personas nuevas"
        ],
        "correcta": 0,
        "explicacion": "La comunicación, el respeto y el tiempo compartido ayudan a cuidar las relaciones."
    },
    {
        "pregunta": "¿Qué papel puede tener el aprendizaje durante la adultez?",
        "opciones": [
            "Ya no se puede aprender después de los 30 años",
            "Solo sirve durante la infancia",
            "Puede apoyar el crecimiento personal, laboral y social durante toda la vida",
            "No tiene relación con la cultura"
        ],
        "correcta": 2,
        "explicacion": "Las personas pueden adquirir conocimientos y habilidades en cualquier etapa de la adultez."
    },
    {
        "pregunta": "Una persona adulta cuida a familiares y también busca apoyo cuando lo necesita. ¿Qué refleja esto?",
        "opciones": [
            "Que no puede tomar decisiones",
            "La importancia de las redes de apoyo y los vínculos familiares",
            "Que debe resolver todo sin ayuda",
            "Que las relaciones sociales son innecesarias"
        ],
        "correcta": 1,
        "explicacion": "Las redes de apoyo pueden contribuir al bienestar y ayudar a afrontar responsabilidades y cambios."
    },
    {
        "pregunta": "¿Cuál afirmación sobre la adultez es más adecuada?",
        "opciones": [
            "Todas las personas adultas viven las mismas experiencias",
            "El desarrollo se detiene al terminar los estudios",
            "La experiencia adulta depende de factores personales, sociales, económicos y culturales",
            "La edad determina por completo los intereses de una persona"
        ],
        "correcta": 2,
        "explicacion": "El desarrollo adulto es diverso y está influido por las experiencias y el contexto de cada persona."
    }
]

class JuegoAdultez:
    def __init__(self, root):
        self.root = root
        self.root.title("Retos de la adultez")
        self.root.geometry("760x540")
        self.root.configure(bg="#f1f5f9")
        self.root.resizable(False, False)

        self.preguntas = random.sample(PREGUNTAS, len(PREGUNTAS))
        self.indice = 0
        self.puntos = 0
        self.respondida = False

        tk.Label(
            root, text="RETOS DE LA ADULTEZ",
            font=("Arial", 22, "bold"), bg="#f1f5f9", fg="#17324d"
        ).pack(pady=(18, 4))

        tk.Label(
            root, text="Desarrollo social y cultural • Aprende jugando",
            font=("Arial", 11), bg="#f1f5f9", fg="#475569"
        ).pack(pady=(0, 12))

        self.progreso = tk.Label(root, text="", font=("Arial", 11, "bold"),
                                 bg="#f1f5f9", fg="#0f766e")
        self.progreso.pack()

        self.pregunta_label = tk.Label(
            root, text="", font=("Arial", 14, "bold"),
            wraplength=660, justify="left", bg="#f1f5f9", fg="#172554"
        )
        self.pregunta_label.pack(anchor="w", padx=42, pady=(18, 14))

        self.botones = []
        for i in range(4):
            boton = tk.Button(
                root, text="", font=("Arial", 11), wraplength=620,
                justify="left", anchor="w", padx=12, pady=9,
                bg="white", fg="#1e293b", activebackground="#dbeafe",
                relief="groove", bd=1, cursor="hand2",
                command=lambda opcion=i: self.responder(opcion)
            )
            boton.pack(fill="x", padx=42, pady=4)
            self.botones.append(boton)

        self.explicacion = tk.Label(
            root, text="", font=("Arial", 10), wraplength=660,
            justify="left", bg="#f1f5f9", fg="#334155"
        )
        self.explicacion.pack(anchor="w", padx=42, pady=(10, 4))

        self.siguiente = tk.Button(
            root, text="Siguiente pregunta →", font=("Arial", 11, "bold"),
            bg="#0f766e", fg="white", activebackground="#115e59",
            activeforeground="white", padx=16, pady=8,
            command=self.avanzar, state="disabled", cursor="hand2"
        )
        self.siguiente.pack(pady=8)

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        self.respondida = False
        actual = self.preguntas[self.indice]
        self.progreso.config(
            text=f"Pregunta {self.indice + 1} de {len(self.preguntas)}     |     Puntos: {self.puntos}"
        )
        self.pregunta_label.config(text=actual["pregunta"])
        opciones = list(enumerate(actual["opciones"]))
        random.shuffle(opciones)
        self.opciones_mostradas = opciones
        for i, (_, texto) in enumerate(opciones):
            self.botones[i].config(text=f"{'ABCD'[i]}.  {texto}",
                                   state="normal", bg="white", fg="#1e293b")
        self.explicacion.config(text="")
        self.siguiente.config(state="disabled",
                              text="Siguiente pregunta →")

    def responder(self, opcion_visual):
        if self.respondida:
            return
        self.respondida = True
        actual = self.preguntas[self.indice]
        respuesta_original = self.opciones_mostradas[opcion_visual][0]
        correcta = actual["correcta"]

        for boton in self.botones:
            boton.config(state="disabled")

        if respuesta_original == correcta:
            self.puntos += 10
            self.botones[opcion_visual].config(bg="#bbf7d0", fg="#14532d")
            prefijo = "¡Correcto! +10 puntos. "
        else:
            self.botones[opcion_visual].config(bg="#fecaca", fg="#7f1d1d")
            for i, (original, _) in enumerate(self.opciones_mostradas):
                if original == correcta:
                    self.botones[i].config(bg="#bbf7d0", fg="#14532d")
            prefijo = "No es esa. "
        self.progreso.config(
            text=f"Pregunta {self.indice + 1} de {len(self.preguntas)}     |     Puntos: {self.puntos}"
        )
        self.explicacion.config(text=prefijo + actual["explicacion"])
        self.siguiente.config(state="normal")
        if self.indice == len(self.preguntas) - 1:
            self.siguiente.config(text="Ver resultado final")

    def avanzar(self):
        if self.indice < len(self.preguntas) - 1:
            self.indice += 1
            self.mostrar_pregunta()
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        porcentaje = self.puntos
        if porcentaje >= 80:
            mensaje = "¡Excelente! Tienes una gran comprensión del tema."
        elif porcentaje >= 50:
            mensaje = "¡Buen trabajo! Repasa las explicaciones para reforzar lo aprendido."
        else:
            mensaje = "¡Sigue aprendiendo! Cada pregunta es una oportunidad para mejorar."

        tk.Label(self.root, text="¡Juego terminado!",
                 font=("Arial", 24, "bold"), bg="#f1f5f9",
                 fg="#17324d").pack(pady=(65, 20))
        tk.Label(self.root, text=f"Tu puntaje: {self.puntos} / 100",
                 font=("Arial", 20, "bold"), bg="#f1f5f9",
                 fg="#0f766e").pack(pady=10)
        tk.Label(self.root, text=mensaje, font=("Arial", 13),
                 wraplength=600, bg="#f1f5f9", fg="#334155").pack(pady=12)
        tk.Label(
            self.root,
            text="Recuerda: la adultez es una etapa diversa en la que las relaciones,\n"
                 "la participación social y la identidad cultural pueden seguir evolucionando.",
            font=("Arial", 11), justify="center",
            bg="#f1f5f9", fg="#475569"
        ).pack(pady=18)

        tk.Button(
            self.root, text="Jugar de nuevo", font=("Arial", 12, "bold"),
            bg="#0f766e", fg="white", padx=20, pady=10,
            command=self.reiniciar, cursor="hand2"
        ).pack(pady=12)

    def reiniciar(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)


if __name__ == "__main__":
    ventana = tk.Tk()
    juego = JuegoAdultez(ventana)
    ventana.mainloop()
