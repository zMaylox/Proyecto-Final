#!/usr/bin/env python3
import json
import time
from nltk.chat.util import *


while True:
    
    print("\n==============================Aprender las tablas de multiplicar===============================\n")
    print("Seleccione la opcion que desea realizar")
    print("(1). Mostrar las tablas de multiplicar")
    print("(2). ChatBot resuelve dudas de tablas")
    print("(3). Iniciar desafio de tablas de multiplicar")
    print("(4). Salir")

    hola = int(input('Ingresa una opcion: '))

    print()
    if hola== 1:
        print("==============================Tabla del 1===============================")
        for f in range(1,11):
            multiplicacion = 1 * f 
            print(f"1 x {f} = {multiplicacion}")
        print("==============================Tabla del 2===============================")
        for f in range(1,11):
            multiplicacion = 2 * f 
            print(f"2 x {f} = {multiplicacion}")
        print("==============================Tabla del 3===============================")
        for f in range(1,11):
            multiplicacion = 3 * f 
            print(f"3 x {f} = {multiplicacion}")
        print("==============================Tabla del 4===============================")
        for f in range(1,11):
            multiplicacion = 4 * f 
            print(f"4 x {f} = {multiplicacion}")
        print("==============================Tabla del 5===============================")
        for f in range(1,11):
            multiplicacion = 5 * f 
            print(f"5 x {f} = {multiplicacion}")
        print("==============================Tabla del 6===============================")
        for f in range(1,11):
            multiplicacion = 6 * f 
            print(f"6 x {f} = {multiplicacion}")
        print("==============================Tabla del 7===============================")
        for f in range(1,11):
            multiplicacion = 7 * f 
            print(f"7 x {f} = {multiplicacion}")
        print("==============================Tabla del 8===============================")
        for f in range(1,11):
            multiplicacion = 8 * f 
            print(f"8 x {f} = {multiplicacion}")
        print("==============================Tabla del 9===============================")
        for f in range(1,11):
            multiplicacion = 9 * f 
            print(f"9 x {f} = {multiplicacion}")
        print("==============================Tabla del 10===============================")
        for f in range(1,11):
            multiplicacion = 10 * f 
            print(f"10 x {f} = {multiplicacion}")

    elif hola == 2:

        mis_reflexions = {
        "ir": "fui",
        "hola": "hey"
        }

        pares = [
            [
                r"(.*) (1x1|1 x 1|1x 1|1 x1)",
                ["La respuesta es: 1",]
            ],

            [
                r"(.*) (1x2|1 x 2|1x 2|1 x2)",
                ["La respuesta es: 2",]
            ],

            [
                r"(.*) (1x3|1 x 3|1x 3|1 x3)",
                ["La respuesta es: 3",]
            ],

            [
                r"(.*) (1x4|1 x 4|1x 4|1 x4)",
                ["La respuesta es: 4",]
            ],

            [
                r"(.*) (1x5|1 x 5|1x 5|1 x5)",
                ["La respuesta es: 5",]
            ],

            [
                r"(.*) (1x6|1 x 6|1x 6|1 x6)",
                ["La respuesta es: 6",]
            ],

            [
                r"(.*) (1x7|1 x 7|1x 7|1 x7)",
                ["La respuesta es: 7",]
            ],


            [
                r"(.*) (1x8|1 x 8|1x 8|1 x8)",
                ["La respuesta es: 8",]
            ],   

            [
                r"(.*) (1x9|1 x 9|1x 9|1 x9)",
                ["La respuesta es: 9",]
            ],

            [
                r"(.*) (1x10|1 x 10|1x 10|1 x10)",
                ["La respuesta es: 10",]
            ],

            [
                r"(.*) (2x1|2 x 1|2x 1|2 x1)",
                ["La respuesta es: 2",]
            ],    

            [
                r"(.*) (2x2|2 x 2|2x 2|2 x2)",
                ["La respuesta es: 4",]
            ],

            [
                r"(.*) (2x3|2 x 3|2x 3|2 x3)",
                ["La respuesta es: 6",]
            ],

            [
                r"(.*) (2x4|2 x 4|2x 4|2 x4)",
                ["La respuesta es: 8",]
            ],
            [
                r"(.*) (2x5|2 x 5|2x 5|2 x5)",
                ["La respuesta es: 10",]
            ],
            [
                r"(.*) (2x6|2 x 6|2x 6|2 x6)",
                ["La respuesta es: 12",]
            ],
            [
                r"(.*) (2x7|2 x 7|2x 7|2 x7)",
                ["La respuesta es: 14",]
            ],
            [
                r"(.*) (2x8|2 x 8|2x 8|2 x8)",
                ["La respuesta es: 16",]
            ],
            [
                r"(.*) (2x9|2 x 9|2x 9|2 x9)",
                ["La respuesta es: 18",]
            ],
            [
                r"(.*) (2x10|2 x 10|2x 10|2 x10)",
                ["La respuesta es: 20",]
            ],
            [
                r"(.*) (3x1|3 x 1|3x 1|3 x1)",
                ["La respuesta es: 3",]
            ],
            [
                r"(.*) (3x2|3 x 2|3x 2|3 x2)",
                ["La respuesta es: 6",]
            ],
            [
                r"(.*) (3x3|3 x 3|3x 3|3 x3)",
                ["La respuesta es: 9",]
            ],
            [
                r"(.*) (3x4|3 x 4|3x 4|3 x4)",
                ["La respuesta es: 12",]
            ],
            [
                r"(.*) (3x5|3 x 5|3x 5|3 x5)",
                ["La respuesta es: 15",]
            ],
            [
                r"(.*) (3x6|3 x 6|3x 6|3 x6)",
                ["La respuesta es: 18",]
            ],
            [
                r"(.*) (3x7|3 x 7|3x 7|3 x7)",
                ["La respuesta es: 21",]
            ],
            [
                r"(.*) (3x8|3 x 8|3x 8|3 x8)",
                ["La respuesta es: 24",]
            ],
            [
                r"(.*) (3x9|3 x 9|3x 9|3 x9)",
                ["La respuesta es: 27",]
            ],
            [
                r"(.*) (3x10|3 x 10|3x 10|3 x10)",
                ["La respuesta es: 30",]
            ],
            [
                r"(.*) (4x1|4 x 1|4x 1|4 x1)",
                ["La respuesta es: 4",]
            ],
            [
                r"(.*) (4x2|4 x 2|4x 2|4 x2)",
                ["La respuesta es: 8",]
            ],
            [
                r"(.*) (4x3|4 x 3|4x 3|4 x3)",
                ["La respuesta es: 12",]
            ],
            [
                r"(.*) (4x4|4 x 4|4x 4|4 x4)",
                ["La respuesta es: 16",]
            ],
            [
                r"(.*) (4x5|4 x 5|4x 5|4 x5)",
                ["La respuesta es: 20",]
            ],
            [
                r"(.*) (4x6|4 x 6|4x 6|4 x6)",
                ["La respuesta es: 24",]
            ],
            [
                r"(.*) (4x7|4 x 7|4x 7|4 x7)",
                ["La respuesta es: 28",]
            ],
            [
                r"(.*) (4x8|4 x 8|4x 8|4 x8)",
                ["La respuesta es: 32",]
            ],
            [
                r"(.*) (4x9|4 x 9|4x 9|4 x9)",
                ["La respuesta es: 36",]
            ],
            [
                r"(.*) (4x10|4 x 10|4x 10|4 x10)",
                ["La respuesta es: 40",]
            ],
            [
                r"(.*) (5x1|5 x 1|5x 1|5 x1)",
                ["La respuesta es: 5",]
            ],
            [
                r"(.*) (5x2|5 x 2|5x 2|5 x2)",
                ["La respuesta es: 10",]
            ],
            [
                r"(.*) (5x3|5 x 3|5x 3|5 x3)",
                ["La respuesta es: 15",]
            ],
            [
                r"(.*) (5x4|5 x 4|5x 4|5 x4)",
                ["La respuesta es: 20",]
            ],
            [
                r"(.*) (5x5|5 x 5|5x 5|5 x5)",
                ["La respuesta es: 25",]
            ],
            [
                r"(.*) (5x6|5 x 6|5x 6|5 x6)",
                ["La respuesta es: 30",]
            ],
            [
                r"(.*) (5x7|5 x 7|5x 7|5 x7)",
                ["La respuesta es: 35",]
            ],
            [
                r"(.*) (5x8|5 x 8|5x 8|5 x8)",
                ["La respuesta es: 40",]
            ],
            [
                r"(.*) (5x9|5 x 9|5x 9|5 x9)",
                ["La respuesta es: 45",]
            ],
            [
                r"(.*) (5x10|5 x 10|5x 10|5 x10)",
                ["La respuesta es: 50",]
            ],

            [
                r"(.*) (6x1|6 x 1|6x 1|6 x1)",
                ["La respuesta es: 6",]
            ],
            [
                r"(.*) (6x2|6 x 2|6x 2|6 x2)",
                ["La respuesta es: 12",]
            ],
            [
                r"(.*) (6x3|6 x 3|6x 3|6 x3)",
                ["La respuesta es: 18",]
            ],
            [
                r"(.*) (6x4|6 x 4|6x 4|6 x4)",
                ["La respuesta es: 24",]
            ],
            [
                r"(.*) (6x5|6 x 5|6x 5|6 x5)",
                ["La respuesta es: 30",]
            ],
            [
                r"(.*) (6x6|6 x 6|6x 6|6 x6)",
                ["La respuesta es: 36",]
            ],
            [
                r"(.*) (6x7|6 x 7|6x 7|6 x7)",
                ["La respuesta es: 42",]
            ],
            [
                r"(.*) (6x8|6 x 8|6x 8|6 x8)",
                ["La respuesta es: 48",]
            ],
            [
                r"(.*) (6x9|6 x 9|6x 9|6 x9)",
                ["La respuesta es: 54",]
            ],
            [
                r"(.*) (6x10|6 x 10|6x 10|6 x10)",
                ["La respuesta es: 60",]
            ],
            [
                r"(.*) (7x1|7 x 1|7x 1|7 x1)",
                ["La respuesta es: 7",]
            ],
            [
                r"(.*) (7x2|7 x 2|7x 2|7 x2)",
                ["La respuesta es: 14",]
            ],
            [
                r"(.*) (7x3|7 x 3|7x 3|7 x3)",
                ["La respuesta es: 21",]
            ],
            [
                r"(.*) (7x4|7 x 4|7x 4|7 x4)",
                ["La respuesta es: 28",]
            ],
            [
                r"(.*) (7x5|7 x 5|7x 5|7 x5)",
                ["La respuesta es: 35",]
            ],
            [
                r"(.*) (7x6|7 x 6|7x 6|7 x6)",
                ["La respuesta es: 42",]
            ],
            [
                r"(.*) (7x7|7 x 7|7x 7|7 x7)",
                ["La respuesta es: 49",]
            ],
            [
                r"(.*) (7x8|7 x 8|7x 8|7 x8)",
                ["La respuesta es: 56",]
            ],
            [
                r"(.*) (7x9|7 x 9|7x 9|7 x9)",
                ["La respuesta es: 63",]
            ],
            [
                r"(.*) (7x10|7 x 10|7x 10|7 x10)",
                ["La respuesta es: 70",]
            ],
            [
                r"(.*) (8x1|8 x 1|8x 1|8 x1)",
                ["La respuesta es: 8",]
            ],

            [
                r"(.*) (8x2|8 x 2|8x 2|8 x2)",
                ["La respuesta es: 16",]
            ],
            [
                r"(.*) (8x3|8 x 3|8x 3|8 x3)",
                ["La respuesta es: 24",]
            ],
            [
                r"(.*) (8x4|8 x 4|8x 4|8 x4)",
                ["La respuesta es: 32",]
            ],
            [
                r"(.*) (8x5|8 x 5|8x 5|8 x5)",
                ["La respuesta es: 40",]
            ],
            [
                r"(.*) (8x6|8 x 6|8x 6|8 x6)",
                ["La respuesta es: 48",]
            ],
            [
                r"(.*) (8x7|8 x 7|8x 7|8 x7)",
                ["La respuesta es: 56",]
            ],
            [
                r"(.*) (8x8|8 x 8|8x 8|8 x8)",
                ["La respuesta es: 64",]
            ],
            [
                r"(.*) (8x9|8 x 9|8x 9|8 x9)",
                ["La respuesta es: 72",]
            ],
            [
                r"(.*) (8x10|8 x 10|8x 10|8 x10)",
                ["La respuesta es: 80",]
            ],

            [
                r"(.*) (9x1|9 x 1|9x 1|9 x1)",
                ["La respuesta es: 9",]
            ],

            [
                r"(.*) (9x2|9 x 2|9x 2|9 x2)",
                ["La respuesta es: 18",]
            ],
            [
                r"(.*) (9x3|9 x 3|9x 3|9 x3)",
                ["La respuesta es: 27",]
            ],
            [
                r"(.*) (9x4|9 x 4|9x 4|9 x4)",
                ["La respuesta es: 36",]
            ],
            [
                r"(.*) (9x5|9 x 5|9x 5|9 x5)",
                ["La respuesta es: 45",]
            ],
            [
                r"(.*) (9x6|9 x 6|9x 6|9 x6)",
                ["La respuesta es: 54",]
            ],
            [
                r"(.*) (9x7|9 x 7|9x 7|9 x7)",
                ["La respuesta es: 63",]
            ],
            [
                r"(.*) (9x8|9 x 8|9x 8|9 x8)",
                ["La respuesta es: 72",]
            ],
            [
                r"(.*) (9x9|9 x 9|9x 9|9 x9)",
                ["La respuesta es: 81",]
            ],
            [
                r"(.*) (9x10|9 x 10|9x 10|9 x10)",
                ["La respuesta es: 90",]
            ],

            [
                r"(.*) (10x1|10 x 1|10x 1|10 x1)",
                ["La respuesta es: 10",]
            ],

            [
                r"(.*) (10x2|10 x 2|10x 2|10 x2)",
                ["La respuesta es: 20",]
            ],
            [
                r"(.*) (10x3|10 x 3|10x 3|10 x3)",
                ["La respuesta es: 30",]
            ],
            [
                r"(.*) (10x4|10 x 4|10x 4|10 x4)",
                ["La respuesta es: 40",]
            ],
            [
                r"(.*) (10x5|10 x 5|10x 5|10 x5)",
                ["La respuesta es: 50",]
            ],
            [
                r"(.*) (10x6|10 x 6|10x 6|10 x6)",
                ["La respuesta es: 60",]
            ],
            [
                r"(.*) (10x7|10 x 7|10x 7|10 x7)",
                ["La respuesta es: 70",]
            ],
            [
                r"(.*) (10x8|10 x 8|10x 8|10 x8)",
                ["La respuesta es: 80",]
            ],
            [
                r"(.*) (10x9|10 x 9|10x 9|10 x9)",
                ["La respuesta es: 90",]
            ],
            [
                r"(.*) (10x10|10 x 10|10x 10|10 x10)",
                ["La respuesta es: 100",]
            ],
            [
                r"(.*) (estas|estas?)",
                ["Estoy muy bien alumno",]
            ],
            [
                r"(disculta|perdon) (.*)",
                ["No pasa nada",]
            ],
            [
                r"hola|hey|buenas",
                ["Hola", "Que tal",]
            ],
            [
                r"que (.*) quieres ?",
                ["Nada gracias",]
        
            ],
            [
                r"(.*) creado|creado?",
                ["Fui creado el dia 23 de Enero del 2021",]
            ],
            [
                r"adios|finalizar|terminar",
                ["Adios","Fue bueno hablar contigo"]
        ],

        ]
        def chatear():
            print("Soy el señor doctor profesor Patricio para usted, puedes preguntarme las tablas de multiplicar del 1 al 10, pero antes que nada hola mucho gusto.") #mensaje por defecto
            chat = Chat(pares, mis_reflexions)
            chat.converse()
        if __name__ == "__main__":
            chatear()

        chatear()

        break

        #----------------------------Cuestionario---------------------------------
    elif hola== 3:
  
        TOPICS_LIST = ['facil', 'medio', 'dificil'] 
        # this list has to in sync with the JSON filename and the Menu prompt inside test() method

        def ask_one_question(question):
            print("\n" + question)
            choice = input("Ingresa una opcion [a/b/c/d]: ")
            while(True):
                if choice.lower() in ['a', 'b', 'c', 'd']:
                    return choice
                else:
                    print("Opcion invalida, ingresa una opcion valida")
                    choice = input("Ingresa una opcion [a/b/c/d]: ")

        def score_one_result(key, meta):
            actual = meta["answer"]
            if meta["user_response"].lower() == actual.lower():
                print("P.{0} Muy bien!\n".format(key))
                return 2
            else:
                print("P.{0} Respuesta incorrecta".format(key))
                print("La respuesta correcta es ({0})".format(actual))
                print ("Respuesta: " + meta["more_info"] + "\n")
                return -1


        def test(questions):
            score = 0
            print("Instrucciones Generales:\n1. Ingresa unicamente la letra que contenga la opcion correspondiente, puedes darle click al boton que contenga la letra o tambien escribirla.\n2. Cada respuesta contestada correctamente ganas 2 puntos. \n3. Cada respuesta incorrecta pierdes 1 punto, si obtienes los suficientes puntos podras pasar al siguiente nivel y asi hasta completar todas las tablas de multiplicar.\nEn breve iniciaremos. Mucha suerte y que la fuerza los acompañe!\n")
            time.sleep(15)
            for key, meta in questions.items():
                questions[key]["user_response"] = ask_one_question(meta["question"])
            print("\n==============================RESULTADO===============================\n")
            for key, meta in questions.items():
                score += score_one_result(key, meta)
            print("Tu puntaje obtenido:", score, "/", (2 * len(questions)))

        def load_question(filename):
            """
            loads the questions from the JSON file into a Python dictionary and returns it
            """
            questions = None
            with open(filename, "r") as read_file:
                questions = json.load(read_file)
            return (questions)


        def play_quiz():
            flag = False
            try:
                choice = int(input("Bienvenido al desafio!\nSelecciona el nivel de dificultad de las preguntas:\n(1). Facil\n(2). Medio\n(3). Dificil\n\nIngresa tu respuesta [1/2/3]: "))
                if choice > len(TOPICS_LIST) or choice < 1:
                    print("Opcion invalida, ingresa una opcion valida")
                    flag = True # raising flag
            except ValueError as e:
                print("Opcion invalida, ingresa una opcion valida")
                flag = True # raising a flag

            if not flag:
                questions = load_question('niveles/'+TOPICS_LIST[choice-1]+'.json')
                test(questions)
            else:
                play_quiz() # replay if flag was raised

        def user_begin_prompt():
            print("Desea realizar la prueba de tablas de multiplicar?\nA. Si\nB. No")
            play = input()
            if play.lower() == 'a' or play.lower() ==  'y':
                play_quiz()
            elif play.lower() == 'b':
                print("Vuelva pronto!")
            else:
                print("Ponga una opcion valida.\nPresiona A para jugar, o B para salir.")
                user_begin_prompt()
        
        def execute():
            user_begin_prompt()

        if __name__ == '__main__':
            execute()

    elif hola== 4:
        print("Vuelva pronto")
        break

    else:
        print("No selecciono una opcion valida")
