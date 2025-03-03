#Este es un script de automatización para ordenar tods los archivos de imagen y pdf en una carpeta
#version 1.0.0
#En la proxima actualización se planea agregar soporte para mas tipos de archivo y multimedias.
# Autor: xXJuanDavidXx
import os
import shutil

def ordenar():
    """Función que ordena todos los archivos img y pdf de una carptea en sus carpetas correspondientes."""    
    #Creo las carpetas y verifico que existan.
    pdf_carpeta = "Pdf"
    imagen_carpeta = "Imagen"

    if not os.path.exists(pdf_carpeta):
        os.mkdir(pdf_carpeta)
    if not os.path.exists(imagen_carpeta):
        os.mkdir(imagen_carpeta)

    # Obtenemos la lista de archivos y directorios
    lista = os.listdir()
    # Recorremos la lista
    for elemento in lista:
        # Si es un archivo
        if os.path.isfile(elemento):
            try: 
            # Obtenemos la extensión
                if elemento.lower().endswith(('pdf')):
                    shutil.move(elemento, pdf_carpeta)

                elif elemento.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                    shutil.move(elemento, imagen_carpeta)
            except:
                print("No se pudo mover el archivo: ", elemento)







if __name__ == "__main__":
    ordenar()
    print("Archivos ordenados correctamente.")

            
            
