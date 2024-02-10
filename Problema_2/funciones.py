def obtener_calificaciones():

    while True:

        try:
            texto = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones = [int(calificacion.strip()) for calificacion in texto.split(',')]
            return calificaciones
        
        except ValueError:
            print("Error: Hubo un problema al convertir las calificaciones a números enteros. Por favor, asegúrese de ingresar solo números.")
            continue

        except Exception as e:
            print("Error:", e)
            continue