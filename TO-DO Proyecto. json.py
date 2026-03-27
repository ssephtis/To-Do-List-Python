#Proyecto TO-DO

import json
import os

ARCHIVO = "tareas.json"

def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return []

def guardar_tareas(tareas):
    with open(ARCHIVO, "w") as f:
        json.dump(tareas, f, indent=4)

def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return
    for i, tarea in enumerate(tareas):
        estado = "✔" if tarea["completada"] else "✘"
        print(f"{i+1}. {tarea['titulo']} [{estado}]")

def agregar_tarea(tareas):
    titulo = input("Nueva tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    guardar_tareas(tareas)

def completar_tarea(tareas):
    mostrar_tareas(tareas)
    num = int(input("Número de tarea a completar: ")) - 1
    if 0 <= num < len(tareas):
        tareas[num]["completada"] = True
        guardar_tareas(tareas)

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    num = int(input("Número de tarea a eliminar: ")) - 1
    if 0 <= num < len(tareas):
        tareas.pop(num)
        guardar_tareas(tareas)

def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- TO DO LIST ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            break
        else:
            print("Opción inválida")

menu()