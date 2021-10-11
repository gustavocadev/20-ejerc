"""
19. Realiza un programa que nos diga si hay probabilidad de que nuestra pareja nos está siendo infiel. El programa irá haciendo preguntas que el usuario contestará con verdadero o falso. Cada pregunta contestada como verdadero sumará 3 puntos. Las preguntas contestadas con falso no suman puntos. A continuación, se listan las preguntas del test.
1) Tu pareja parece estar más inquieta de lo normal sin ningún motivo aparente.
2) Ha aumentado sus gastos de vestuario
3) Ha perdido el interés que mostraba anteriormente por tí
4) Ahora se afeita y se asea con más frecuencia(si es hombre) o ahora se arregla el pelo y se asea con más frecuencia(si es mujer)
5) No te deja que mires la agenda de su teléfono móvil
6) A veces tiene llamadas que dice no querer contestar cuando estás tú delante
7) Últimamente se preocupa más en cuidar la línea y/o estar bronceado/a
8) Muchos días viene tarde después de trabajar porque dice tener mucho más trabajo
9) Has notado que últimamente se perfuma más
10) Se confunde y te dice que ha estado en sitios donde no ha ido contigo

A continuación, se muestran los mensajes que deberá dar el programa según la puntuación obtenida.
- Puntuación entre 0 y 10: ¡Enhorabuena! tu pareja parece ser totalmente fiel.
- Puntuación entre 11 y 22: Quizás exista el peligro de otra persona en su vida o en su mente, aunque seguramente será algo sin importancia. No bajes la guardia.
- Puntuación entre 22 y 30: Tu pareja tiene todos los ingredientes para estar viviendo un romance con otra persona. Te aconsejamos que indagues un poco más y averigües que es lo que está pasando por su cabeza.
"""


def imprimir_resultado(resultado):
    if resultado >= 0 and resultado <= 10:
        print("¡Enhorabuena! tu pareja parece ser totalmente fiel.")
    if resultado >= 0 and resultado <= 10:
        print("Quizás exista el peligro de otra persona en su vida o en su mente, aunque seguramente será algo sin importancia. No bajes la guardia.")
    if resultado >= 22 and resultado <= 30:
        print("Tu pareja tiene todos los ingredientes para estar viviendo un romance con otra persona. Te aconsejamos que indagues un poco más y averigües que es lo que está pasando por su cabeza.")


def validar_puntos(respuesta):
    puntos = 0
    if respuesta.lower() == 'v' or respuesta.lower() == "verdadero":
        puntos = 3
    return puntos


def preguntar_y_retornar_punto(pregunta):
    respuesta = input(f'{pregunta}: ')
    # Funcion que validara los puntos
    puntoObtenido = validar_puntos(respuesta)
    # retornamos el punto obtenido por la pregunta
    return puntoObtenido


# Creo un diccionario de las preguntas
preguntas = [
    {
        'pregunta1': "¿Tu pareja parece estar más inquieta de lo normal sin ningún motivo aparente?",
    },
    {
        'pregunta2': "¿Ha aumentado sus gastos de vestuario?",
    },
    {
        'pregunta3': "¿Ha perdido el interés que mostraba anteriormente por tí?",
    },
    {
        'pregunta4': "¿Ahora se afeita y se asea con más frecuencia(si es hombre) o ahora se arregla el pelo y se asea con más frecuencia(si es mujer)?",
    },
    {
        'pregunta5': "¿No te deja que mires la agenda de su teléfono móvil?",
    },
    {
        'pregunta6': "¿A veces tiene llamadas que dice no querer contestar cuando estás tú delante?",
    },
    {
        'pregunta7': "¿Últimamente se preocupa más en cuidar la línea y/o estar bronceado/a?",
    },
    {
        'pregunta8': "¿Muchos días viene tarde después de trabajar porque dice tener mucho más trabajo?",
    },
    {
        'pregunta9': "¿Has notado que últimamente se perfuma más?",
    },
    {
        'pregunta10': "¿Se confunde y te dice que ha estado en sitios donde no ha ido contigo?",
    }

]

i = 1
# variable acumuladora de puntos
puntos_totales = 0

print("Responde con [v] = Verdadero, [f] = Falso")
# Hago un iteración de las preguntas
for pregunta in preguntas:
    # Uso mi funcion que retornará el punto
    punto_obtenido = preguntar_y_retornar_punto(pregunta[f'pregunta{i}'])
    # a mi mi misma variable puntos_totales le sumo el punto que retorne la función
    puntos_totales += punto_obtenido
    i += 1

imprimir_resultado(puntos_totales)
