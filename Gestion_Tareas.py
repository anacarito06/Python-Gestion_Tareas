class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = 'pendiente'

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}\n"


def agregar_tarea(lista_tareas):
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    nueva_tarea = Tarea(titulo, descripcion)
    lista_tareas.append(nueva_tarea)
    print("Tarea agregada exitosamente.")


def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas para mostrar.")
    else:
        for tarea in lista_tareas:
            print(tarea)


def buscar_tarea(lista_tareas):
    titulo = input("Ingrese el título de la tarea que desea buscar: ")
    for tarea in lista_tareas:
        if tarea.titulo == titulo:
            print(tarea)
            return
    print("Tarea no encontrada.")


def actualizar_estado(lista_tareas):
    titulo = input("Ingrese el título de la tarea que desea marcar como completada: ")
    for tarea in lista_tareas:
        if tarea.titulo == titulo:
            tarea.estado = 'completada'
            print("Estado de la tarea actualizado a 'completada'.")
            return
    print("Tarea no encontrada.")


def eliminar_tarea(lista_tareas):
    titulo = input("Ingrese el título de la tarea que desea eliminar: ")
    for tarea in lista_tareas:
        if tarea.titulo == titulo:
            lista_tareas.remove(tarea)
            print("Tarea eliminada.")
            return
    print("Tarea no encontrada.")


def menu():
    lista_tareas = []
    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar nueva tarea")
        print("2. Mostrar todas las tareas")
        print("3. Buscar una tarea por título")
        print("4. Actualizar el estado de una tarea")
        print("5. Eliminar una tarea por título")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                agregar_tarea(lista_tareas)
            elif opcion == 2:
                mostrar_tareas(lista_tareas)
            elif opcion == 3:
                buscar_tarea(lista_tareas)
            elif opcion == 4:
                actualizar_estado(lista_tareas)
            elif opcion == 5:
                eliminar_tarea(lista_tareas)
            elif opcion == 6:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


menu()
