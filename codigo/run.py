"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""
def main():
    bandera =True
    contador = 0
    while bandera :
        num=int(input("Ingrese el 1 para crear cuenta de Facebook , 2 para crear cuenta de twitter, 3 para crear\n"
                      "cuenta de Whatsapp,4  para crear cuenta de Telegram, 5 para crear cuenta de Signal, 6 para\n"
                      "crear cuenta de Instagram o 7 para crear cuenta de Flickr\n"))
        if num == 1:
            print(crearFacebook())
        else:
            if num == 2:
                crearTwitter()
            else:
                if num == 3:
                    print(crearWhatsapp())
                else:
                    if num == 4:
                        crearTelegram()
                    else:
                        if num == 5:
                            print(crearSignal())
                        else:
                            if num == 6:
                                crearInstagram()
                            else:
                                if num == 7:
                                    print(crearFlickr())
                                else:
                                    print("Valor fuera del rango")
        contador = contador + 1
        salida=input("Ingrese no para dejar de Ingresar cuentas o  si para continuar --> ")
        if salida == "no":
            bandera = False
    cadena = "\nNumero de cuentas creadas: %d --> %s\n" % (contador, obtenerMensaje(contador))
    print(cadena)
def crearFacebook():
    """
        explicación de método
    """
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    edad = int(input("Ingrese su edad --> "))
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    correo_electronico = input("Ingrese su correo electronico --> ")
    cadena = "%s\nNombre de Usuario: %s\nEdad: %d\nCiudad: %s\nPaís: %s\nCorreo Electronico: %s\n" % \
             ("\nCreando cuenta de Facebook", nombre_usuario, edad, ciudad, pais, correo_electronico)
    return cadena

def crearTwitter():
    """
        explicación de método
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
             "\nCorreo Electronico: %s\n" % ("\nCreando cuenta de Twitter",nombre_usuario,nombre,
                                             apellido,edad, ciudad, pais, idioma,correo_electronico)
    print(cadena)
def crearWhatsapp():
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    num_telefono = input("Ingrese su numero de Telefono --> ")
    edad = int(input("Ingrese su edad --> "))
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    cadena = "%s\nNombre de Usuario: %s\nTelefono: %s\nEdad: %d\nCiudad: %s\nPaís: %s\n" % \
             ("\nCreando cuenta de Whatsapp",nombre_usuario,num_telefono,edad,ciudad,pais)
    return cadena
def crearTelegram():
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    num_telefono = input("Ingrese su numero de Telefono --> ")
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    area_interes = input("Ingrese su Area de Interes --> ")
    cadena = "%s\nNombre de Usuario: %s\nTelefono: %s\nCiudad: %s\nPaís: %s\nArea de Interes: %s\n" % \
             ("\nCreando cuenta de Telegram",nombre_usuario,num_telefono,ciudad,pais,area_interes)
    print(cadena)
def crearSignal():
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    num_telefono = input("Ingrese su numero de Telefono --> ")
    ciudad = input("Ingrese su Ciudad --> ")
    pais = input("Ingrese el País --> ")
    hobby_principal = input("Ingrese su hobby Principal --> ")
    cadena = "%s\nNombre de Usuario: %s\nTelefono: %s\nCiudad: %s\nPaís: %s\nHobby Principal: %s\n" % \
             ("\nCreando cuenta de Signal\n", nombre_usuario, num_telefono, ciudad, pais, hobby_principal)
    return  cadena
def crearInstagram():
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    ciudad = input("Ingrese su Ciudad --> ")
    edad = int(input("Ingrese su edad --> "))
    correo_electronico = input("Ingrese su correo electronico --> ")
    cadena = "%s\nNombre de Usuario: %s\nCiudad: %s\nEdad: %d\nCorreo Electronico: %s\n" % \
             ("\nCreando cuenta de Instagram", nombre_usuario,ciudad, edad, correo_electronico)
    print(cadena)
def crearFlickr():
    nombre_usuario = input("Ingrese  su nombre de Usuario --> ")
    correo_electronico = input("Ingrese su correo electronico --> ")
    cadena = "%s\nNombre de Usuario: %s\nCorreo Electronico: %s\n" % \
             ("\nCreando cuenta de Flickr", nombre_usuario, correo_electronico)
    return cadena
def obtenerMensaje(a):
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if 1 <= a <= 5:
        return mensajeFinal[0]
    else:
        if 6 <= a <= 15:
            return mensajeFinal[1]
        else:
            if a > 16:
                return mensajeFinal[2]

# agregar los métodos faltantes

# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
if __name__ == "__main__":
    """
	Leer las indicaciones para que el proceso cumpla
	lo solicitado.	
	"""

    """"
        print("proceso inicial")
        crearFacebook()
        cuenta_twitter = crearTwitter()
        print(cuenta_twitter)
    """
    main()