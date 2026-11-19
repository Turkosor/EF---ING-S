from datetime import date, timedelta

print("=" * 40)
print("BIBLIOTECA - UNIVERSIDAD UPN")
print("=" * 40)

# DATOS DEL ESTUDIANTE
codigoUPN = input("Ingrese su codigo UPN: N00")

while len(codigoUPN) != 6 or not codigoUPN.isdigit():
    print("Error: debe ingresar exactamente 6 digitos.")
    codigoUPN = input("Ingrese nuevamente: ")

codigoUPN = "N00" + codigoUPN

telefono = input("Ingrese su telefono: ")

while len(telefono) != 9 or not telefono.isdigit():
    print("Error: debe ingresar exactamente 9 digitos.")
    telefono = input("Ingrese nuevamente: ")

# CONTROL DEL PRESTAMO
prestamoActivo = False

while True:

    print("\n" + "=" * 45)
    print("MENU PRINCIPAL")
    print("=" * 45)

    print("1. Solicitar prestamo")
    print("2. Renovar prestamo")
    print("3. Devolver libro")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    while not opcion.isdigit() or opcion not in ["1", "2", "3", "4"]:
        print("Error: seleccione una opcion del 1 al 4.")
        opcion = input("Ingrese nuevamente: ")

    opcion = int(opcion)

    match opcion:

        # SOLICITAR PRESTAMO
        case 1:

            if prestamoActivo:
                print("Ya tiene un prestamo activo.")
                continue

            print("\n" + "=" * 40)
            print("CATALOGO DE LIBROS")
            print("=" * 40)

            print("""1. Python basico
2. Algoritmos y estructuras de datos
3. Base de datos
4. HTML y CSS
5. Introduccion a la programacion""")

            libro = input("Seleccione el libro solicitado: ")

            while not libro.isdigit() or int(libro) < 1 or int(libro) > 5:
                print("Libro invalido, intente nuevamente.")
                libro = input("Elegir: ")

            libro = int(libro)

            match libro:

                case 1:
                    nombre = "Python basico"
                    tipoColeccion = "Lectura"
                    diasPrestamo = 7
                    renovacionesPermitidas = 2

                case 2:
                    nombre = "Algoritmos y estructuras de datos"
                    tipoColeccion = "Lectura"
                    diasPrestamo = 7
                    renovacionesPermitidas = 2

                case 3:
                    nombre = "Base de datos"
                    tipoColeccion = "Lectura"
                    diasPrestamo = 7
                    renovacionesPermitidas = 2

                case 4:
                    nombre = "HTML y CSS"
                    tipoColeccion = "Regular"
                    diasPrestamo = 2
                    renovacionesPermitidas = 3

                case 5:
                    nombre = "Introduccion a la programacion"
                    tipoColeccion = "Regular"
                    diasPrestamo = 2
                    renovacionesPermitidas = 3

            diasPrestamoBase = diasPrestamo

            # ACEPTACION DE LAS CONDICIONES
            print("\n" + "=" * 40)
            print("CONDICIONES Y SANCIONES DEL PRESTAMO")
            print("=" * 40)

            print("\n1. RETRASO EN LA DEVOLUCION:")
            print("Por cada dia de retraso, el estudiante no podra")
            print("solicitar prestamos durante esa misma cantidad de dias.")

            print("\n2. DAÑO DEL LIBRO:")
            print("Si el libro presenta algun daño, el estudiante")
            print("debera reemplazarlo por otro ejemplar en buen estado.")

            print("\n3. INCUMPLIMIENTO DEL REEMPLAZO:")
            print("Si el estudiante no reemplaza el libro dañado,")
            print("no podra matricularse en el siguiente ciclo.")

            print("=" * 40)

            deseaPrestar = input(
                "\n¿Acepta las condiciones del prestamo?\n"
                "1. SI\n"
                "2. NO\n"
                "Seleccione una opcion: "
            )

            while deseaPrestar not in ["1", "2"]:
                print("Opcion no valida. Intente nuevamente.")
                deseaPrestar = input("Ingrese nuevamente: ")

            if deseaPrestar == "1":

                prestamoActivo = True
                renovacionesUsadas = 0

                fechaPrestamo = date.today()
                fechaDevolucion = fechaPrestamo + timedelta(days=diasPrestamo)

                print("\nPrestamo registrado.")

                print("\n" + "=" * 40)
                print("TICKET DE SOLICITUD DE PRESTAMO")
                print("=" * 40)

                print(f"Codigo UPN: {codigoUPN}")
                print(f"Telefono: {telefono}")
                print(f"Libro: {nombre}")
                print(f"Coleccion: {tipoColeccion}")
                print(f"Fecha de prestamo: {fechaPrestamo}")
                print(f"Fecha de devolucion: {fechaDevolucion}")
                print(f"Plazo de prestamo: {diasPrestamo} dias")
                print(f"Renovaciones permitidas: {renovacionesPermitidas}")

                print("-" * 45)
                print("ESTADO: PRESTAMO REGISTRADO")
                print("Presente este ticket al personal")
                print("de biblioteca para recoger el libro.")
                print("=" * 45)

            else:
                print("El estudiante no acepta las condiciones.")
                print("No se realiza el prestamo.")

        # RENOVAR PRESTAMO
        case 2:

            if not prestamoActivo:
                print("No tiene ningun prestamo activo.")
                continue

            print("\n" + "=" * 40)
            print("RENOVACION DE PRESTAMO")
            print("=" * 40)

            print(f"Libro: {nombre}")
            print(f"Fecha actual de devolucion: {fechaDevolucion}")
            print(f"Plazo actual: {diasPrestamo} dias")
            print(f"Renovaciones realizadas: {renovacionesUsadas}")
            print(f"Renovaciones permitidas: {renovacionesPermitidas}")

            if renovacionesUsadas < renovacionesPermitidas:

                deseaRenovar = input(
                    "\n¿Desea confirmar la renovacion?\n"
                    "1. SI\n"
                    "2. NO\n"
                    "Seleccione una opcion: "
                )

                while deseaRenovar not in ["1", "2"]:
                    print("Opcion no valida.")
                    deseaRenovar = input("Ingrese nuevamente: ")

                if deseaRenovar == "1":

                    diasPrestamo += diasPrestamoBase
                    fechaDevolucion += timedelta(days=diasPrestamoBase)
                    renovacionesUsadas += 1

                    print("\nRenovacion realizada correctamente.")
                    print(f"Nueva fecha de devolucion: {fechaDevolucion}")
                    print(f"Nuevo plazo: {diasPrestamo} dias")
                    print(f"Renovaciones restantes: {renovacionesPermitidas - renovacionesUsadas}")

                else:
                    print("Renovacion cancelada.")

            else:
                print("Ya alcanzo el limite de renovaciones.")

        # PROCESO DE DEVOLUCION
        case 3:

            if not prestamoActivo:
                print("No tiene ningun prestamo activo.")
                continue

            print("\n" + "=" * 40)
            print("PROCESO DE DEVOLUCION")
            print("=" * 40)

            libroDevuelto = input(
                "\n¿Desea devolver el libro?\n"
                "1. SI\n"
                "2. NO\n"
                "Seleccione una opcion: "
            )

            while libroDevuelto not in ["1", "2"]:
                print("Opcion no valida. Intente nuevamente.")
                libroDevuelto = input("Ingrese nuevamente: ")

            if libroDevuelto == "1":

                diasRetraso = input("Ingrese los dias de retraso: ")

                while not diasRetraso.isdigit() or int(diasRetraso) < 0:
                    print("Error: ingrese solamente numeros y que no sean negativos.")
                    diasRetraso = input("Ingrese nuevamente: ")

                diasRetraso = int(diasRetraso)

                # ESTADO DEL LIBRO
                libroDanado = input(
                    "\n¿El libro presenta daños?\n"
                    "1. SI\n"
                    "2. NO\n"
                    "Seleccione una opcion: "
                )

                while libroDanado not in ["1", "2"]:
                    print("Opcion no valida. Intente nuevamente.")
                    libroDanado = input("Ingrese nuevamente: ")

                # TICKET DE DEVOLUCION
                print("\n" + "=" * 40)
                print("TICKET DE DEVOLUCION DE LIBRO")
                print("=" * 40)

                print(f"Libro devuelto: {nombre}")
                print(f"Dias de retraso: {diasRetraso}")

                if libroDanado == "1":
                    print("Libro dañado: SI")
                else:
                    print("Libro dañado: NO")

                if diasRetraso > 0 or libroDanado == "1":
                    print("Sancion: Aplicada")
                else:
                    print("Sancion: No aplica")

                if diasRetraso >= 100:
                    print("Reporte: Enviado a jefatura.")
                elif diasRetraso > 0:
                    print(f"Suspension: {diasRetraso * 2} dias.")
                else:
                    print("El libro fue devuelto dentro del plazo.")

                if libroDanado == "1":
                    print("Debe reemplazar el libro por otro ejemplar.")

                prestamoActivo = False
                print("\nPrestamo finalizado correctamente.")

            else:
                print("El libro aun no ha sido devuelto.")
                print("El prestamo permanece pendiente.")

        # SALIR
        case 4:

            print("\nGracias por utilizar el sistema.")
            print("Fin del proceso.")
            break