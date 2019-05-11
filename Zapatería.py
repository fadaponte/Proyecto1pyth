from Proyecto1 import Zapato

#variables

codigos = {
    0:'zapTAN37',
    1:'zapTAN38',
    2:'zapTAN39',
    3:'zapTAM37',
    4:'zapTAM38',
    5:'zapTAM39',
    6:'zapTMN37',
    7:'zapTMN38',
    8:'zapTMN39',
    9:'zapTMM37',
    10:'zapTMM38',
    11:'zapTMM39'
}

Descripcion = {
    0:'Tacón alto negro',
    1:'Tacón alto negro',
    2:'Tacón alto negro',
    3:'Tacón alto marrón',
    4:'Tacón alto marrón',
    5:'Tacón alto marrón',
    6:'Tacón medio negro',
    7:'Tacón medio negro',
    8:'Tacón medio negro',
    9:'Tacón medio marrón',
    10:'Tacón medio marrón',
    11:'Tacón medio marrón',
}

Talla = {
    0:37,
    1:38,
    2:39,
    3:37,
    4:38,
    5:39,
    6:37,
    7:38,
    8:39,
    9:37,
    10:38,
    11:39
}

Precio = {
    0:95000,
    1:95000,
    2:95000,
    3:92500,
    4:92500,
    5:92500,
    6:85000,
    7:85000,
    8:85000,
    9:83500,
    10:83500,
    11:83500
}

Cantidad = {
    0:10,
    1:10,
    2:10,
    3:7,
    4:7,
    5:7,
    6:12,
    7:12,
    8:12,
    9:8,
    10:8,
    11:8
}

#variables

#metodos

def entregar():
    codigo = input("ingrese el código del zapato: ")
    
    print("El modelo seleccionado es: Zapato {modelo=" + descr +", talla="+tal+", precio="+prec+"}\n"
           "Del modelo" + codigo + "existen: "+ cant + "\n")
    return "por implementar entregar\n"

def fabricar():
    return "por implementar fabricar\n"

def verificarExistencia():
    return "por implementar verificarExistencia\n"

def verExistencia():
    return "por implementar verExistencia\n"

switch = {
    1: entregar,
    2: fabricar,
    3: verificarExistencia,
    4: verExistencia
}

def main():
    a = True
    while (a):
        print ( "1. entregar\n2. fabricar\n3. verificarExistencia\n4. verExistencia\n5. salir\n")
        op = int(input("ingrese una opción: "))
        if op > 5 or op < 1:
            print("Opción invalida")
        else:
            if op != 5:
                print(switch[op]())
            elif op == 5:
                print("\nGracias por usar el sistema, regrese pronto\n")
                a = False

#metodos

if __name__ == "__main__":
    main()
