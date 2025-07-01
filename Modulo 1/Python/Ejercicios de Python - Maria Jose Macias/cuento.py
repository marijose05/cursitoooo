# el examen
print("Buenos dias, Hoy es el dia de un examen importante.")
print("Te despiertas tarde y solo tienes 20 minutos para llegar.")
print("Miras por la ventana y ves que esta lloviendo mucho.")

opciones = ["SALIR aun esta lloviendo", "BUSCAR un paraguas", "LLAMAR a un amigo"]
print("\nOpciones:")
for op in opciones:
    print(f"- {op}")
opcion = input("¿Qué haces? (Escribe una opción en MAYÚSCULAS): ").upper()

if opcion == "SALIR":
    print("\nSales corriendo bajo la lluvia. Llegas a la parada del autobus completamente empapado.")
    print("El autobus esta a punto de llegar, pero ves que hay un gran charco entre tu y la puerta.")
    
    opciones = ["SALTAR", "ESPERAR"]
    print("\nOpciones:")
    for op in opciones:
        print(f"- {op}")
    opcion = input("¿Qué haces? (Escribe una opción en MAYÚSCULAS): ").upper()
    
    if opcion == "SALTAR":
        print("\nIntentas saltar, pero resbalas y caes en el charco. El conductor del autobus se rie y se va sin dejarte subir.")
        print("Llegas tarde al examen y repruebas.")
        print("FIN (Mal final)")
    elif opcion == "ESPERAR":
        print("\nEl autobus se detiene justo frente a ti y logras subir sin problemas.")
        print("Llegas justo a tiempo para el examen.")
        print("FIN (Buen final)")
    else:
        print("\n vuelve a intentar.")

elif opcion == "BUSCAR":
    print("\nBuscas por toda la casa y finalmente encuentras un paraguas roto.")
    print("Decides usarlo igual, pero apenas te cubre. Al salir, ves que el autobus ya paso y el siguiente llegara en 30 minutos.")
    
    opciones = ["CAMINAR", "PEDIR"]
    print("\nOpciones:")
    for op in opciones:
        print(f"- {op}")
    opcion = input("¿Qué haces? (Escribe una opción en MAYÚSCULAS): ").upper()
    
    if opcion == "CAMINAR":
        print("\nLlegas empapado y con frio, pero justo a tiempo para el examen.")
        print("Sin embargo, estas tan mojado que no puedes concentrarte y repruebas.")
        print("FIN (Mal final)")
    elif opcion == "PEDIR":
        print("\nEl taxi llega rapido y llegas justo a tiempo, seco y listo para el examen.")
        print("Sacas una buena nota.")
        print("FIN (Buen final)")
    else:
        print("\nNo tomaste una decision a tiempo. Llegaste tarde al examen.")

elif opcion == "LLAMAR":
    print("\nLlamas a tu amigo Carlos, quien acepta llevarte.")
    print("Sin embargo, mientras esperas, revisas tus notas y te das cuenta de que olvidaste estudiar un tema importante.")
    
    opciones = ["REPASAR y esperar que te salga lo estudiado", "REZAR y esperar un milagro"]
    print("\nOpciones:")
    for op in opciones:
        print(f"- {op}")
    opcion = input("¿Qué haces? (Escribe una opción en MAYÚSCULAS): ").upper()
    
    if opcion == "REPASAR":
        print("\nLogras entender lo basico justo a tiempo. En el examen, sale esa pregunta y la respondes bien.")
        print("Pasas el examen con buena nota.")
        print("FIN")
    elif opcion == "REZAR":
        print("\nEl tema que no estudiaste es justo el que mas preguntas tiene en el examen.")
        print("Repruebas.")
        print("FIN")
    else:
        print("\nNo hiciste nada al respecto. El tema aparecio en el examen y no supiste que responder.")

else:
    print("\nNo elegiste ninguna opcion valida. Te quedaste paralizado y perdiste el examen.")