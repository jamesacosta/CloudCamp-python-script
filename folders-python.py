import os
import datetime

def create_folder():
    # Creamos el folder
    folder_name = "folder-script"

    # Comprobación si el folder existe
    if os.path.exists(folder_name):
        os.rmdir(folder_name)

    # Creamos la carpeta
    os.makedirs(folder_name)

    # Nos movemos al folder creado
    os.chdir(folder_name)

    # Creamos los archivos dentro de la carpeta
    for i in range(10):
        archivo_nombre = f"archivo_{i+1}.txt"
        with open(archivo_nombre, 'w') as file:
            # Escribimos la fecha y hora de creación de cada archivo
            tiempo_creacion = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"La fecha y la hora en que creamos: {tiempo_creacion}")

    print(f"Se ha creado la carpeta '{folder_name}' y se han generado los 10 archivos dentro.")

if __name__ == "__main__":
    create_folder()
