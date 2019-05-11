
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
#Método que devuelve la informacion completa de un producto especificado
def getZapato(codigo):
    if codigo in Codigos.values():
        clave = list(Codigos.values()).index(codigo)
        descr = Descripcion.get(clave)
        tal = Talla.get(clave)
        prec = Precio.get(clave)
        cant = Cantidad.get(clave)
    return "\n El modelo seleccionado es: Zapato {modelo=" + descr +", talla="+ str(tal) +", precio="+ str(prec) +"}\n Del modelo " + codigo + " existen: "+ str(cant) + "\n"
    
#Método que elimina un registro entero de producto
def popZapato(codigo):
    if codigo in Codigos.values():
        llave = list(Codigos.values()).index(codigo)
        Codigos.pop(llave)
        Descripcion.pop(llave)
        Talla.pop(llave)
        Precio.pop(llave)
        Cantidad.pop(llave)
        return True
    else:
        return False


#Método que permite realizar entregas
def entregar():

    codigo = input("ingrese el código del zapato: ")  
    if codigo in Codigos.values():
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

    else:
        print("\n El código introducido no se encuentra registrado.")

        
#Método que permite agregar unidades del producto al inventario
def fabricar():

    codigo = input("ingrese el código del zapato: ")
    if codigo in Codigos.values():
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

    else:
        print("\n El código introducido no se encuentra registrado.")
    
#Método que muestra las existencias de un modelo particular
def verificarExistencia():

    codigo = input("ingrese el código del zapato: ")
    if codigo in Codigos.values():
        clave = list(Codigos.values()).index(codigo)
        descr = Descripcion.get(clave)
        tal = Talla.get(clave)
        prec = Precio.get(clave)
        cant = Cantidad.get(clave)
        print("\n El modelo seleccionado es: Zapato {modelo=" + descr +", talla="+ str(tal) +", precio="+ str(prec) +"}\n Del modelo " + codigo + " existen: "+ str(cant) + "\n")
    else:
        print("\n El código introducido no se encuentra registrado.")


#Método que muestra todo el inventario
def verExistencia():
    print("Modelo  | Descripción         | Talla | Precio  | Cantidad \n")
    for i in Codigos:
        print(Codigos[i]+" | "+Descripcion[i]+"   | "+str(Talla[i])+"    | "+str(Precio[i])+"   | "+str(Cantidad[i]))

#Método que permite modificar las caracteristicas de un producto ya registrado
def updateZapato():

    codigo = input("Ingrese el código del zapato: ")
    if codigo in Codigos.values():
        clave = list(Codigos.values()).index(codigo)
        descr = Descripcion.get(clave)
        tal = Talla.get(clave)
        prec = Precio.get(clave)
        cant = Cantidad.get(clave)
        print("\n El modelo seleccionado es: Zapato {modelo=" + descr +", talla="+ str(tal) +", precio="+ str(prec) +"}\n Del modelo " + codigo + " existen: "+ str(cant) + "\n")
        print("\n1. Descripción\n2. Talla\n3. Precio\n4. Cantidad")
        opcion = int(input("\n Seleccione la característica que desea cambiar: "))
        if opcion == 1:
            campo = input("\n Introduzca la nueva descripción: ")
            Descripcion.update({clave: campo})
            print("\n La información se ha actualizado de manera satisfactoria")
            print(getZapato(codigo))
        elif opcion == 2:
            try:
                campo = input("\n Introduzca la nueva talla: ")
                Talla.update({clave: campo})
                print("\n La información se ha actualizado de manera satisfactoria")
                print(getZapato(codigo))
            except ValueError:
                print("\nEl valor debe ser numerico")
        elif opcion == 3:
            try:
                campo = input("\n Introduzca el nuevo precio: ")
                Precio.update({clave: campo})
                print("\n La información se ha actualizado de manera satisfactoria")
                print(getZapato(codigo))
            except ValueError:
                print("\nEl valor debe ser numerico")
        elif opcion == 4:
            try:
                campo = input("\n Introduzca la nueva cantidad: ")
                Cantidad.update({clave: campo})
                print("\n La información se ha actualizado de manera satisfactoria")
                print(getZapato(codigo))
            except ValueError:
                print("\nEl valor debe ser numerico")
        elif opcion > 5 or opcion < 1:
            print("\n La opción introducida no es correcta.")

    else:
        print("\n El código introducido no se encuentra registrado.")


#Método que permite eliminar el registro de un producto
def deleteZapato():
 codigo = input("Ingrese el código del zapato que desea eliminar: ")
 print("\n El registro a eliminar es:")
 print(getZapato(codigo))
 op = input("\n¿Está seguro que desea eliminar el registro?(y/n): ")
 if op == "y":
    if popZapato(codigo) == True:
        print("\n El registro se ha eliminado satisfactoriamente")
        print("\n A continuacion se muestra el inventario para confirmación: \n")
        verExistencia()
       


#Método que permite agregar un registro de un producto
def postZapato():
 print ()

switch = {
    1: entregar,
    2: fabricar,
    3: verificarExistencia,
    4: verExistencia,
    5: updateZapato,
    6: deleteZapato
}

def main():
    a = True
    while (a):
        print ( "\n1. Entregar\n2. Fabricar\n3. Verificar Existencia\n4. Ver Inventario\n5. Modificar registro\n6. Eliminar registro\n7. Agregar producto\n8. Salir")
        try:
            op = int(input("Ingrese una opción: "))
            if op > 8 or op < 1:
                print("Opción invalida")
            else:
                if op != 8:
                    switch[op]()
                elif op == 8:
                    print("\nGracias por usar el sistema, regrese pronto\n")
                    a = False
        except ValueError:
                print("\nEl valor debe ser numerico")

#metodos

if __name__ == "__main__":
    main()
