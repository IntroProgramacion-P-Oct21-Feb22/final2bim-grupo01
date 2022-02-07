"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""


def main():
    """
    Este seria el procediiento principal desde el cual se va ha presentar un menu de opciones sobre que tipo de
    cuentas crear hasta que el usuario lo decida, ademas de que para ello este procedimiento se ecargara de
    llamar a los difrenetes procedimientos o funciones segun sea el caso. Una vez que se termine de ingresar cuentas
    se llamara a una funcion que me duvuelve un mensaje en segun el numero de cuentas creadas y los presentara.
    """
    bandera = True
    contador = 0
    while bandera:
        num = int(input("Menu de Opciones\n-Ingrese el 1 para crear cuenta de Facebook\n-Ingrese el 2 para crear "
                        "cuenta de twitter\n-Ingrese el 3 para crear cuenta de Whatsapp\n-Ingrese el 4 para crear "
                        "cuenta de Telegram\n-Ingrese el 5 para crear cuenta de Signal\n-Ingrese el 6 para crear "
                        "cuenta de Instagram\n-Ingrese el 7 para crear cuenta de Flickr\n"))
        if num == 1:
            print(crear_facebook())
        else:
            if num == 2:
                crear_twitter()
            else:
                if num == 3:
                    print(crear_whatsapp())
                else:
                    if num == 4:
                        crear_telegram()
                    else:
                        if num == 5:
                            print(crear_signal())
                        else:
                            if num == 6:
                                crear_instagram()
                            else:
                                if num == 7:
                                    print(crear_flickr())
                                else:
                                    print("Valor fuera del rango")
        if 1 <= num <= 7:
            contador = contador + 1
        salida = input("Ingrese no para dejar de Ingresar cuentas o si para continuar --> ")
        if salida == "no":
            bandera = False
    cadena = "\nNumero de cuentas creadas: %d --> %s\n" % (contador, obtener_mensaje(contador))
    print(cadena)


def crear_facebook():
    """
    La función crear_facebook va a pedir todos los datos nesesarios para la creacion de la cuenta y va a retornar
    todos estos datos en una sola cadena.
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    edad = int(input("Ingrese su edad --> "))
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    correo_electronico = input("Ingrese su correo electronico --> ")
    cadena = "%s\nNombre de Usuario: %s\nEdad: %d\nCiudad: %s\nPaís: %s\nCorreo Electronico: %s\n" % \
             ("\nCreando cuenta de Facebook", nombre_usuario, edad, ciudad, pais, correo_electronico)
    return cadena


def crear_twitter():
    """
    El procedimiento crear_twitter va a pedir todos los datos nesesarios para la creacion de la cuenta y va
    a presentar todos los datos pedidos.
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    nombre = input("Ingrese sus Nombres --> ")
    apellido = input("Ingrese sus Apellidos --> ")
    edad = int(input("Ingrese su edad --> "))
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    idioma = input("Igrese su Idioma --> ")
    correo_electronico = input("Ingrese su correo Electronico --> ")
    cadena = "%s\nNombre de Usuario: %s\nNombres: %s\nApellido: %s\nEdad: %d\nCiudad: %s\nPaís: %s\nIdioma: %s" \
             "\nCorreo Electronico: %s\n" % ("\nCreando cuenta de Twitter", nombre_usuario, nombre,
                                             apellido, edad, ciudad, pais, idioma, correo_electronico)
    print(cadena)


def crear_whatsapp():
    """
    La función crear_whatsapp va a pedir todos los datos nesesarios para la creacion de la cuenta y va a retornar
    todos estos datos en una sola cadena.
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    num_telefono = input("Ingrese su numero de Telefono --> ")
    edad = int(input("Ingrese su edad --> "))
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    cadena = "%s\nNombre de Usuario: %s\nTelefono: %s\nEdad: %d\nCiudad: %s\nPaís: %s\n" % \
             ("\nCreando cuenta de Whatsapp", nombre_usuario, num_telefono, edad, ciudad, pais)
    return cadena


def crear_telegram():
    """
    El procedimiento crear_telegram va a pedir todos los datos nesesarios para la creacion de la cuenta y va
    a presentar todos los datos pedidos.
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    num_telefono = input("Ingrese su numero de Telefono --> ")
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    area_interes = input("Ingrese su Area de Interes --> ")
    cadena = "%s\nNombre de Usuario: %s\nTelefono: %s\nCiudad: %s\nPaís: %s\nArea de Interes: %s\n" % \
             ("\nCreando cuenta de Telegram", nombre_usuario, num_telefono, ciudad, pais, area_interes)
    print(cadena)


def crear_signal():
    """
    La función crear_signal va a pedir todos los datos nesesarios para la creacion de la cuenta y va a retornar
    todos estos datos en una sola cadena.
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    num_telefono = input("Ingrese su numero de Telefono --> ")
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    hobby_principal = input("Ingrese su hobby Principal --> ")
    cadena = "%s\nNombre de Usuario: %s\nTelefono: %s\nCiudad: %s\nPaís: %s\nHobby Principal: %s\n" % \
             ("\nCreando cuenta de Signal\n", nombre_usuario, num_telefono, ciudad, pais, hobby_principal)
    return cadena


def crear_instagram():
    """
    El procedimiento crear_instagram va a pedir todos los datos nesesarios para la creacion de la cuenta y va
    a presentar todos los datos pedidos.
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    ciudad = input("Ingrese su Ciudad --> ")
    edad = int(input("Ingrese su edad --> "))
    correo_electronico = input("Ingrese su correo electronico --> ")
    cadena = "%s\nNombre de Usuario: %s\nCiudad: %s\nEdad: %d\nCorreo Electronico: %s\n" % \
             ("\nCreando cuenta de Instagram", nombre_usuario, ciudad, edad, correo_electronico)
    print(cadena)


def crear_flickr():
    """
    La función crear_flickr va a pedir todos los datos nesesarios para la creacion de la cuenta y va a retornar
    todos estos datos en una sola cadena.
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    correo_electronico = input("Ingrese su correo electronico --> ")
    cadena = "%s\nNombre de Usuario: %s\nCorreo Electronico: %s\n" % \
             ("\nCreando cuenta de Flickr", nombre_usuario, correo_electronico)
    return cadena


def obtener_mensaje(a):
    """
    La función obtener_mensaje va a revisar un valor entero y va realizar el proceso para determinar
    en que rango se encuentra la campaña y devolver un mensaje.
    """
    mensaje_final = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if 1 <= a <= 5:
        return mensaje_final[0]
    else:
        if 6 <= a <= 15:
            return mensaje_final[1]
        else:
            if a > 16:
                return mensaje_final[2]
            else:
                return "Ninguna cuenta Creada"


if __name__ == "__main__":
    """"
    Aquí empieza el proceso cuando se ejecuta por consola
    el archivo python run.py
    """
    main()
