import random


def menu():
    """
    Este es el menu del juego. Aqui se accede a todas las opciones.
    """
    print('\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
    print('+ Bienvenido al menu del juego!             +')
    print('+ 1. Jugar                                  +')
    print('+ 2. Informacion sobre solar punk           +')
    print('+ 3. Informacion sobre pueblos originarios  +')
    print('+ 4. Informacion sobre el conflicto         +')
    print('+    en Cabagra, Costa Rica                 +')
    print('+ 5. Referencias                            +')
    print('+ 6. Reglas del Juego                       +')
    print('+ 7. Salir                                  +')
    print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')
    selection = obtener_seleccion()  # llama a la opcion seleccionada en el menu
    if selection == 1:
        inicio_juego()
    elif selection == 2:
        informacion_solar()
    elif selection == 3:
        informacion_originarios()
    elif selection == 4:
        informacion_conflicto()
    elif selection == 5:
        referencias()
    elif selection == 6:
        informacion_juego()
    elif selection == 7:
        salir_del_juego()

    else:
        print('\nSelecciona una opcion valida')
        menu()


def informacion_solar():
    print(r"""El solarpunk es un movimiento que propone un futuro utópico basado en la energía renovable, 
la sostenibilidad y la armonía con la naturaleza. En contraste con el cyberpunk, que se centra en un futuro 
distópico dominado por la tecnología y las megacorporaciones, el solarpunk imagina un mundo donde la tecnología se 
utiliza para promover la vida en equilibrio con el medio ambiente. Toma en cuenta la tecnología pero la aplica de 
manera sostenible.

En un futuro solarpunk, las ciudades estarían llenas de jardines verticales, techos verdes y paneles solares integrados 
en la arquitectura. La energía sería generada de manera descentralizada, utilizando tecnologías como la energía solar, 
eólica e hidroeléctrica. Los vehículos serían eléctricos o alimentados por energía renovable, y se promovería el 
transporte público, la bicicleta y el caminar para reducir la huella de carbono.

La producción de alimentos se basaría en granjas urbanas, agricultura vertical y sistemas de permacultura, minimizando 
el uso de pesticidas y promoviendo la biodiversidad. La economía estaría orientada hacia la producción local y 
el comercio justo, fomentando la comunidad y la colaboración en lugar de la competencia desenfrenada y del inestable 
crecimiento del capitalismo.La vestimenta solarpunk se caracterizaría por el uso de tejidos sostenibles, reciclados y 
de comercio justo, con un enfoque en la creatividad, la expresión personal y la artesanía. La cultura solarpunk 
valoraría la diversidad, la inclusión y el respeto por todas las formas de vida.
    """)


def informacion_originarios():
    print(r"""
En Costa Rica, residen más de 104 mil personas indígenas, pertenecientes a 8 pueblos, de los cuales 36 mil habitan en 
24 territorios. Los pueblos indígenas en Costa Rica incluyen a los Bribris, Cabcares, Malekus, Chorotegas, Huetares, 
Ngabes, Bruncas y Terrabas. La Organización de las Naciones Unidas reconoce la importancia y las contribuciones 
fundamentales que realizan los pueblos indígenas a Costa Rica en relación con sus aportes a la economía, la cultura, 
el desarrollo social y la protección del ambiente. Cada uno de estos pueblos contribuye a la diversidad y riqueza de la 
civilización y cultura de Costa Rica.

Según el último censo nacional de población, al menos 104,143 personas se identifican como aborígenes o sus 
descendientes, lo que representa poco más del 2% de la población. Su influencia cultural logra encontrarse en diversas 
capas de la sociedad costarricense en aspectos, ya sea esto en aspectos culinarios, culturales, folclóricos e 
idiomáticos. El porcentaje de la población indígena que vive bajo el nivel de pobreza alcanza cifras alarmantes. Por 
ejemplo, el 94.3% de la población Cabcar vive bajo el nivel de pobreza, y este porcentaje también es alto para otros 
pueblos indígenas como los Ngbe, Brran, Bribri, Brunka, Maleku, Chorotega y Huetar.

En cuanto a los derechos de los pueblos indígenas en Costa Rica, a pesar de que el país ha adoptado la Declaración de 
Naciones Unidas sobre los Derechos de los Pueblos Indígenas y ha ratificado la Convención 169 de la OIT, los derechos 
al territorio y a la autodeterminación siguen sin estar plenamente reconocidos. Sin embargo, ha habido avances 
importantes, como la aplicación del mecanismo de consulta, y el reconocimiento de derechos de uso ancestral del 
territorio.""")


def informacion_conflicto():
    print(r"""
La situación en Cabagra es de alta sensibilidad, ya que se han registrado hechos violentos en el territorio 
indígena. Esta área ha sido escenario de tensiones y conflictos relacionados con la recuperación de tierras por parte de
la comunidad indígena Bribri. Estos incidentes han resultado en agresiones y personas heridas, lo que ha llevado al 
gobierno a llamar a un cese de la violencia en el territorio.

La recuperación de tierras en territorio indígena es un tema complicado que ha generado confrontaciones y desacuerdos 
entre las comunidades indígenas y otros involucrados. En el caso de Cabagra, la disputa por la tierra ha desencadenado 
situaciones de violencia que han llegado a afectar a las personas que habitan la zona.

Es fundamental entender que la disputa por la tierra va más allá de un conflicto territorial; se trata de un tema que 
involucra aspectos culturales, históricos y de identidad para la comunidad indígena. La tierra no solo representa un 
espacio físico, sino también un lugar con significado espiritual para estas comunidades. Ante esta situación, es 
necesario buscar vías de diálogo y negociación que permitan abordar de manera pacífica y respetuosa las diferencias en 
torno a la tenencia de la tierra. El respeto a los derechos de las comunidades indígenas, así como la protección de su 
integridad física y cultural, son aspectos fundamentales que deben ser considerados en la búsqueda de 
soluciones a estos conflictos.""")


def referencias():
    print(r"""  Solarpunk: La guía definitiva de la literatura eco-optimista. (n.d.). Recuperado 5 de junio, 2024, de 
    https://www.solarpedia.info/solarpunk/amp/

    Solarpunk: Características. (2023, March 26). Recuperado 5 de junio, 2024, de https://espejohumeanterevista.
    wordpress.com/2023/03/26/solarpunk-caracteristicas/

    Investigación pregunta a indígenas cómo les gustaría que sean las viviendas sociales. (s.f.). Recuperado 5 de junio,
     2024, de https://pubmed.ncbi.nlm.nih.gov/12556237/

    El Mundo Indígena: Costa Rica. (s.f.). Recuperado 5 de junio, 2024, de https://iwgia.org/es/costa-rica/4785-mi-2022
    -costa-rica.html

    Comunidades indígenas de Ujarrás, Salitre y Cabagra se suman a la ciencia ciudadana para proteger la biodiversidad.
     (s.f.). Recuperado 5 de junio, 2024, de https://www.telediario.cr/en-alerta/gobierno-llama-cese-violencia-
     territorio-indigena-cabagra

    Soy indígena en Costa Rica y - esta es mi historia. (s.f.). Recuperado 5 de junio, 2024, de 
    https://www.puravidauniversity.eu/territorios-indigenas-costa-rica/

    El Mundo Indígena 2024: Costa Rica. (s.f.). Recuperado 5 de junio, 2024, de https://www.telediario.cr/en-alerta/
    gobierno-llama-cese-violencia-territorio-indigena-cabagra

    Conflictos en territorios indígenas salen de Salitre y llegan también a Cabagra. (s.f.). Recuperado 5 de junio, 
    2024, de https://delfino.cr/2021/11/recuperacion-de-tierra-en-territorio-indigena-bribri-deja-agresiones-y-
    personas-heridas

    Indígenas reclaman al Gobierno falta de soluciones efectivas. (s.f.). Recuperado 5 de junio, 2024, de 
    https://semanariouniversidad.com/pais/territorios-indigenas-china-kicha-y-cabagra-registraron-hechos-
    violentos-durante-fin-de-ano/""")


def salir_del_juego():
    print('\nGracias por jugar!')
    exit(0)


def informacion_juego():
    print('El territorio de Cabagra esta en peligro!\n'
          'En este juego deberas luchar contra presiones externas que quieren crear mineras, areas agricolas, \n'
          'establecer rutas de narcotrafico y mas dentro de zonas infigenas autonomas\n'
          'Durante el dia, podras ayudar a la comunidad a realizar proyectos de desarrollo para el fortalecimiento \n'
          'de su autonomia y para conservar su cultura. En la noche, actores externos estaran interesados en \n'
          'usurpar espacios sobre el territorio, demoliendo proyectos')
    selec = input('Deseas saber mas informacion sobre las mecanicas del juego? (y): ')
    if selec == 'y':
        print('Tablero:\nEl tablero del juego se maneja en indices de 0 hasta 8 (maximo 9x9)\n\n'
              'Fin del Juego:\nEl juego termina cuando se crea una fila o una columna de proyectos consolidados\n'
              'o si el territorio se parte en dos por territorios usurpados\n\n'
              'Plantear una iniciativa:\nPuedes plantear una iniciativa por turno, sera un proyecto al siguiente dia,\n'
              'una iniciativa no puede ser destruida por fuerzas externas\n\n'
              'Difundir cultura:\nAl difundir cultura se exparse de manera horizontal o vertical, recuperando terreno\n'
              'usurpado, hasta llegar a un proyecto consolidado. Si se intenta destruir una de estas casillas, \n'
              'solamente se suprime\n\n'
              'Proyectos consolidados:\nLas casillas con proyectos son las unicas casillas '
              'que se toman en cuenta para ganar, pueden ser usurpadas directamente\n\n'
              'Casillas usurpadas:\nEn estos espacios no sera posible plantear iniciativas ni establecer proyectos '
              'consolidados')
        menu()
    else:
        menu()


def obtener_seleccion():
    """
    Función para selecciones con números
    """
    selection = input('Introduce tu selección: ')
    if selection.isdigit():
        return int(selection)
    else:
        print('\nIntroduce un número válido')
        return obtener_seleccion()


tablero = [' ']


def win(persona):
    """
    Verifica si el jugador ha ganado.
    """
    # Verifica filas
    for fila in persona:
        if all(celda == 'P' for celda in fila):
            print("¡Has ganado!")
            return menu()

    # Verifica columnas
    for col in range(len(persona[0])):
        if all(fila[col] == 'P' for fila in persona):
            print("¡Has ganado!")
            print("""⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣄⢘⣒⣀⣀⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣛⠛⢛⣿⣿⡿⠟⠂⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⡀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⡆⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠜⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⠿⠿⣿⣿⡿⢿⣿⣿⠈⣿⣿⣿⡏⣠⡴⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣿⣿⣿⡿⢁⣴⣶⣄⠀⠀⠉⠉⠉⠀⢻⣿⡿⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⠟⠋⠀⠈⠛⣿⣿⠀⠀⠀⠀⠀⠀⠸⣿⡇⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⠀⠀⠀⠀⠀⠘⠿⠆⠀⠀⠀⠀⠀⠀⣿⡇⠀⠿⠇⠀""")
            return menu()

    # Si no se ha encontrado una fila o columna completa de 'P', el juego continúa.
    print("El juego continúa.")


def lose(signalis):
    """
    Verifica si el jugador ha perdido.
    """
    # Verifica filas
    for fila in signalis:
        if all(celda == 'X' for celda in fila):
            print("¡Has perdido! Los usurpadores separaron la ciudad.")
            return menu()

    # Verifica columnas
    for col in range(len(signalis[0])):
        if all(fila[col] == 'X' for fila in signalis):
            print("¡Has perdido! Los usurpadores separaron la ciudad.")
            return menu()


flag = False


def pipipi(pi):
    global flag
    while flag:
        for i in range(len(pi)):
            for j in range(len(pi[i])):
                if pi[i][j] == 'I':
                    pi[i][j] = 'P'
        flag = False
        dia(pi)


def inicio_juego():
    """
    Inicia el juego
    """
    # Se definen columnas
    print('Escribe la cantidad de columnas de tu tablero')
    num = obtener_seleccion()

    while not (3 <= num <= 9):
        print('Debe ser un número entre 3 y 9')
        num = obtener_seleccion()

    columnas = [' '] * num  # Inicializa una fila con el número correcto de columnas

    # Se añaden las filas a la cuadrícula
    print('Escribe la cantidad de filas de tu tablero')
    num = obtener_seleccion()

    while not (3 <= num <= 9):
        print('Debe ser un número entre 3 y 9')
        num = obtener_seleccion()
    filas = [columnas[:] for _ in range(num)]  # Crea una matriz de filas y columnas

    return dia(filas)


def dia(ciudad):
    global tablero
    tablero = ciudad
    pipipi(tablero)
    print(r"""
    _.-.-=-.                  .-=.'"=.-=.
  (       .'    \  :  /      '._.-=._.=-'
   '-"-=="    `. .-=-. .'  
----------------'     '--------------------""")
    for fila in tablero:
        print(("[{0}]".format(', '.join(map(str, fila)))))
    win(tablero)
    print('Que deseas hacer?\n'
          '1. Proyecto\n'
          '2. Iniciativa\n'
          '3. Cultura\n')
    seleccion = obtener_seleccion()
    if seleccion == 1:
        proyecto(tablero)
    elif seleccion == 2:
        iniciativa(tablero)
    elif seleccion == 3:
        cultura(tablero)
    else:
        print('Seleccion invalida')
        dia(tablero)


def iniciativa(ciudad):
    global tablero, flag
    tablero = ciudad
    print('¿Dónde deseas realizar una iniciativa?')
    print('Fila: ', end='')
    y = obtener_seleccion()
    print('Columna: ', end='')
    x = obtener_seleccion()

    # Validación de índices
    if not 0 <= x < len(ciudad[0]):
        print('Debe ser un valor dentro de los parámetros de la matriz.')
        iniciativa(tablero)
    elif not 0 <= y <= len(ciudad):
        print('Debe ser un valor dentro de los parámetros de la matriz.')
        iniciativa(tablero)
    elif ciudad[y][x] == 'X':
        print('Esta casilla ha sido usurpada')
        iniciativa(tablero)
    else:
        # Modifica solo el valor específico
        tablero[y][x] = 'I'  # Usamos y para las filas y x para las columnas
        flag = True
    return noche(tablero)


def proyecto(ciudad):
    global tablero, flag
    tablero = ciudad
    print('¿Dónde deseas realizar un proyecto?')
    print('Fila: ', end='')
    y = obtener_seleccion()
    print('Columna: ', end='')
    x = obtener_seleccion()

    # Validación de índices
    if not 0 <= x < len(ciudad[0]):
        print('Debe ser un valor dentro de los parámetros de la matriz.')
        iniciativa(tablero)
    elif not 0 <= y <= len(ciudad):
        print('Debe ser un valor dentro de los parámetros de la matriz.')
        iniciativa(tablero)
    elif ciudad[y][x] == 'X':
        print('Esta casilla ha sido usurpada')
        iniciativa(tablero)
    else:
        # Modifica solo el valor específico
        tablero[y][x] = 'P'  # Usamos y para las filas y x para las columnas
    return noche(tablero)


def cultura(ciudad):
    selec = input('Difundir cultura en una fila o una columna (f/c): ')
    if selec == 'f':
        print("Seleccione el índice de la fila:")
        fila_index = obtener_seleccion()
        if 0 <= fila_index < len(tablero):
            convertir_fila(tablero, fila_index)
        else:
            print("Índice de fila fuera de rango.")
            cultura(tablero)
    elif selec == 'c':
        columna = obtener_seleccion()
        if not 0 <= columna < len(ciudad[0]):
            print('Debe ser un valor dentro de los parámetros de la matriz.')
            cultura(tablero)
        else:
            convertir_columna(tablero, columna)
    else:
        print('selecciona fila (f) o columna (c)')
        cultura(tablero)


def convertir_fila(matriz, fila_index):
    """
    Convierte una fila a 'C' hasta encontrar una 'X' o una 'P'.
    """
    for i in range(len(matriz[fila_index])):
        if matriz[fila_index][i] == 'P':
            break
        matriz[fila_index][i] = 'C'
    noche(tablero)


def convertir_columna(matriz, ind):
    """
    Convierte una columna a 'C' hasta encontrar una 'X' o una 'P'.
    """
    for i in range(len(matriz)):
        if matriz[i][ind] == 'P':
            break
        matriz[i][ind] = 'C'
    noche(tablero)


def noche(ciudad):
    global tablero
    print('Empieza la noche')
    print(r"""
                  ,-,
    _.-.-=-.     /.(        .-=.'"=.-=.
  (       .'     \ {       '._.-=._.=-'
   '-"-=="        `-`
-------------------------------------------""")
    for fila in tablero:
        print(("[{0}]".format(', '.join(map(str, fila)))))
    for i in range(len(ciudad)):
        for j in range(len(ciudad[i])):
            x = random.random()
            if x < 0.1:  # 10% de probabilidad de ser usurpado
                if ciudad[i][j] == 'I':
                    ciudad[i][j] = 'I'
                elif ciudad[i][j] == 'C':
                    ciudad[i][j] = ' '
                else:
                    ciudad[i][j] = 'X'
    print('Los usurpadores hacen su movimiento')
    tablero = ciudad
    for fila in tablero:
        print(("[{0}]".format(', '.join(map(str, fila)))))
    print('La noche ha pasado')
    lose(tablero)

    return dia(tablero)


def main():
    """
    La funcion principal llama al menu para iniciar
    """
    while True:
        menu()


if __name__ == "__main__":
    main()
