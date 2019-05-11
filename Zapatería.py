
#variables
def __init__():
    print("nada")
Codigos = {
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

#Método que permite realizar entregas
def entregar():
    codigo = input("ingrese el código del zapato: ")
    clave = list(Codigos.values()).index(codigo)
    descr = Descripcion.get(clave)
    tal = Talla.get(clave)
    prec = Precio.get(clave)
    cant = Cantidad.get(clave)
   
    print("\n El modelo seleccionado es: Zapato {modelo=" + descr +", talla="+ str(tal) +", precio="+ str(prec) +"}\n Del modelo " + codigo + " existen: "+ str(cant) + "\n")
   
    while (True):
        despacho = input("\n Indique la cantidad a despachar:")
        total = cant - int(despacho)
        if total > 0:
            Cantidad.update({clave: total})
            print("\n Despachadas "+ despacho + " unidades del modelo " + codigo)
            cant = Cantidad.get(clave)                          
            print("\n Existencia del modelo "+ codigo + ": "+ str(cant) + "\n")
            break
        else:
            print("\n La cantidad introducida es mayor que las existencias del producto")
            op = input("\n Desea introducir otra cantidad?(y/n): ")
            if (op == "n"):
                break
        
#Método que permite agregar unidades del producto al inventario
def fabricar():
    codigo = input("ingrese el código del zapato: ")
    clave = list(Codigos.values()).index(codigo)
    descr = Descripcion.get(clave)
    tal = Talla.get(clave)
    prec = Precio.get(clave)
    cant = Cantidad.get(clave)
    print("\n El modelo seleccionado es: Zapato {modelo=" + descr +", talla="+ str(tal) +", precio="+ str(prec) +"}\n Del modelo " + codigo + " existen: "+ str(cant) + "\n")
    fabricados = input("\n Indique la cantidad a fabricar:")
    total = cant + int(fabricados)
    Cantidad.update({clave: total})
    print("\n Agregadas "+ fabricados + " unidades del modelo " + codigo)
    cant = Cantidad.get(clave)                          
    print("\n Existencia del modelo "+ codigo + ": "+ str(cant) + "\n")
    

def verificarExistencia():
    codigo = input("ingrese el código del zapato: ")
    clave = list(Codigos.values()).index(codigo)
    descr = Descripcion.get(clave)
    tal = Talla.get(clave)
    prec = Precio.get(clave)
    cant = Cantidad.get(clave)
    print("\n El modelo seleccionado es: Zapato {modelo=" + descr +", talla="+ str(tal) +", precio="+ str(prec) +"}\n Del modelo " + codigo + " existen: "+ str(cant) + "\n")


def verExistencia():
    print("Modelo  | Descripción         | Talla | Precio  | Cantidad \n")
    for i in Codigos:
        print(Codigos[i]+" | "+Descripcion[i]+"   | "+str(Talla[i])+"    | "+str(Precio[i])+"   | "+str(Cantidad[i]))


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
                switch[op]()
            elif op == 5:
                print("\nGracias por usar el sistema, regrese pronto\n")
                a = False

#metodos

if __name__ == "__main__":
    main()
