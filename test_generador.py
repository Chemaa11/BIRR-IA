from generador import GeneradorCreativo

generador = GeneradorCreativo()

opciones = {
    "1": "codigo",
    "2": "script",
    "3": "musica",
    "4": "historia",
    "5": "guion",
    "6": "ideas"
}

print("====================================")
print("     BIRR-IA GENERADOR CREATIVO")
print("====================================")

while True:

    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Generar código")
    print("2. Generar scripts")
    print("3. Generar música")
    print("4. Generar historias")
    print("5. Generar guiones")
    print("6. Generar ideas creativas")
    print("7. Mejorar último contenido")
    print("8. Guardar contenido")
    print("9. Salir")

    opcion = input(
        "\nSelecciona una opción: "
    ).strip()

    if opcion == "9":
        print("\nGracias por utilizar BIRR-IA.")
        break

    try:

        if opcion in opciones:

            tipo = opciones[opcion]

            descripcion = input(
                "\nDescribe lo que deseas generar: "
            )

            estilo = input(
                "Estilo (Enter para Profesional): "
            ).strip() or "Profesional"

            extension = input(
                "Extensión (Corta, Media o Larga): "
            ).strip() or "Media"

            print("\nGenerando contenido con Gemini...")
            print("Por favor, espera unos momentos.")

            resultado = generador.generar(
                tipo,
                descripcion,
                estilo,
                extension
            )

            print("\n--- CONTENIDO GENERADO ---\n")
            print(resultado)

        elif opcion == "7":

            instrucciones = input(
                "\n¿Qué deseas mejorar? "
            )

            print("\nMejorando contenido...")

            resultado = generador.mejorar(
                instrucciones
            )

            print("\n--- CONTENIDO MEJORADO ---\n")
            print(resultado)

        elif opcion == "8":

            ruta = generador.guardar()

            print("\nContenido guardado correctamente.")
            print(f"Ubicación: {ruta}")

        else:

            print("\nOpción no válida.")

    except Exception as error:

        print(f"\nOcurrió un error: {error}")