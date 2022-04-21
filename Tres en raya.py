tablero = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]

jugador_actual = "X"
ganador = None
seguir_jugando = True


#Funcion para mostrar el tablero en la consola#
def print_tablero(tab):
    for i in range(len(tab)):
        if (i + 1) % 3 == 0 and i != 0 and i != 8:
            print(tab[i])
            print("----------")
        
        elif (i + 1) == 9:
            print(tab[i])
            
        else:
            print(str(tab[i]) + " | ", end="")
            

#Funcion para recibir input del jugador#
def jugada_usuario(tab):
    jugada = int(input("Elija un numero entre 1 y 9: "))
    if jugada >= 1 and jugada <= 9 and tab[jugada - 1] == "-":
        tab[jugada - 1] = jugador_actual
    
    else:
        print("Posicion no valida")
        

#Funciones para comprobar si se ha ganado o empatado#
def comprobar_horizontal(tab):
    global ganador
    if tab[0] == tab[1] == tab[2] and tab[1] != "-":
        ganador = tab[0]
        return True
    elif tab[3] == tab[4] == tab[5] and tab[4] != "-":
         ganador = tab[3]
         return True   
    elif tab[6] == tab[7] == tab[8] and tab[7] != "-":
          ganador = tab[6]
          return True      

def comprobar_vertical(tab):
    global ganador
    if tab[0] == tab[3] == tab[6] and tab[3] != "-":
        ganador = tab[0]
        return True
    elif tab[1] == tab[4] == tab[7] and tab[4] != "-":
         ganador = tab[1]
         return True   
    elif tab[2] == tab[5] == tab[8] and tab[5] != "-":
          ganador = tab[2]
          return True
      
def comprobar_diagonal(tab):
    global ganador
    if tab[0] == tab[4] == tab[8] and tab[4] != "-":
        ganador = tab[0]
        return True
    elif tab[2] == tab[4] == tab[6] and tab[4] != "-":
         ganador = tab[2]
         return True

def comprobar_empate(tab):
    global seguir_jugando
    if "-" not in tab:
        print_tablero(tab)
        print("Empate")
        seguir_jugando = False

def comprobar_victoria():
    global seguir_jugando
    if comprobar_horizontal(tablero) or comprobar_vertical(tablero) or comprobar_diagonal(tablero):
        print_tablero(tablero)
        print(f"El ganador es {ganador}")
        seguir_jugando = False


#Funcion para cambiar de jugador#
def cambiar_jugador():
    global jugador_actual
    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"


#Bucle para que el juego fucione#
while seguir_jugando:
    print_tablero(tablero)
    jugada_usuario(tablero)
    comprobar_victoria()
    comprobar_empate(tablero)
    cambiar_jugador()
    
    