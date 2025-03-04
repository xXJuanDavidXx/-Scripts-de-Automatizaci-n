import subprocess 
import os
import argparse



def buscar_en_lista(lista, directorio, directorio_salida):
    """
    Función dedicada a ejecutar el script bash para buscar archivos y copiarlos a una carpeta indicada

    args:
        lista: str : La ruta de la lista de archivos a buscar.
        directorio: str : La ruta del directorio donde buscar los archivos.
        directorio_salida: str : La ruta de la carpeta donde se van a copiar los archivos encontrados.
    """
    if "~" in directorio:
        directorio = os.path.expanduser(directorio)

    if "~" in directorio_salida:
        directorio_salida = os.path.expanduser(directorio_salida)



    with open(lista, "r") as f:
        archivos = f.read().splitlines()

        for archivo in archivos:
            
            args = [directorio, archivo, directorio_salida]
            
            result = subprocess.run(["bash", script] + args, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"[+] Archivo {archivo} encontrado en {directorio}")
                print("Salida:", result.stdout) 
            else:
                print(f"[-] Archivo {archivo} no encontrado en {directorio}")
                print("Errores:", result.stderr)



if __name__ == "__main__":

    script = "Buscar_archivo.sh"

    parser = argparse.ArgumentParser(description="Buscar archivos en un directorio y copiarlos a una carpeta.")
    parser.add_argument("-l", "--lista", type=str, required=True, help="La ruta de la lista de archivos a buscar.")
    parser.add_argument("-d", "--directorio", type=str, required=True, help="La ruta del directorio donde buscar los archivos.")
    parser.add_argument("-ds", "--directorio_salida", type=str, required=True, help="La ruta de la carpeta donde se van a copiar los archivos encontrados.")

    args = parser.parse_args()

    buscar_en_lista(args.lista, args.directorio, args.directorio_salida)






