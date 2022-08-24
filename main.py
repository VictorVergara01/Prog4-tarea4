import redis

r = redis.Redis(
    host = "localhost",
    port = 6379) 

def principal():
    menu="""
a) Agregar nueva palabra
b) Editar palabra existente
c) Eliminar palabra existente
d) Ver listado de palabras
e) Buscar significado de palabra
f) Salir
Elige: """
    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            palabra = input("Ingresa la palabra: ")
            # Comprobar si no existe
            posible_significado = r.hexists("diccionario", palabra)
            if posible_significado:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("Ingresa el significado: ")
                agregar_palabra(palabra, significado)
                print("Palabra agregada")

        if eleccion == "b":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            r.hset("diccionario", palabra, nuevo_significado)
            print("Palabra actualizada")

        if eleccion == "c":
            palabra = input("Ingresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
            print("Palabra eliminada")

        if eleccion == "d":
            palabras = r.hkeys("diccionario")
            print("=== Lista de palabras ===")
            print(palabras)

        if eleccion == "e":
            palabra = input(
                "Ingresa la palabra de la cual quieres saber el significado: ") 
            significado = r.hget("diccionario", palabra)
            if significado:
                    print(significado)
            else:
                print("Palabra no encontrada")            


def agregar_palabra(palabra, significado):
    r.hset("diccionario", palabra, significado)

#def existe_palabra(palabra):
#    r.hexists("diccionario", palabra)

#def buscar_significado(palabra):
#    r.hget("diccionario", palabra)    

def eliminar_palabra(palabra):
    r.hdel("diccionario", palabra)

#def obtener_palabras():
#    r.hkeys("diccionario")

if __name__ == '__main__':
  principal()










#for x in range(3):
#    palabra= input("Ingrese palabra:")
#    significado= input("Ingrese significado:")

#    r.hset("diccionario", palabra, significado)

#else:
#    print(r.hgetall("diccionario"))