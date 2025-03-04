#Script para comprimir imagenes a Lossy en formato webp
#1.0.0
#De momento no se planea añadir nada mas al script
# Autor: xXJuanDavidXx


from PIL import Image
import os
import argparse

class Comprimir:
    def __init__(self, ruta):
        self.ruta = ruta  
        self._crear_ruta()  # En caso de que no exista, creamos la ruta.

    def _crear_ruta(self):
        """En caso de que la ruta no exista, prueba crear la ruta."""
        try:
            if not os.path.exists(self.ruta):
                os.makedirs(self.ruta)
        except Exception as e:
            print(f"Error creando la ruta: {e}")

    def comprimir(self, imagen, calidad):
        """
        Comprime una imagen.
        
        Args:
        imagen : str : La ruta de la imagen a comprimir.
        calidad : int : La calidad de compresión (1-100).
        """
        try:
            image = Image.open(imagen).convert('RGB')  # Convertimos la imagen a RGB para que sea compatible con WEBP.
            
            tamano_inicial = os.path.getsize(imagen) / (1024 * 1024)  # Obtenemos el tamaño inicial de la imagen en MB

            nombre_archivo, _ = os.path.splitext(os.path.basename(imagen))  # Quitamos cualquier extensión que pueda tener (jpg, png, webp)
            ruta_salida = os.path.join(self.ruta, f'cp_{nombre_archivo}.jpg')  # Agregamos la extensión jpg

            image.save(ruta_salida, 'JPEG', quality=calidad)  # Guardamos la imagen en la ruta dada.
            
            tamano_final = os.path.getsize(ruta_salida) / (1024 * 1024)  # Obtenemos el tamaño final de la imagen en MB
            
            print(f"[+] Peso inicial: {tamano_inicial:.2f} MB  --  Peso final: {tamano_final:.2f} MB\n\n")  # Comparamos los tamaños en MB
        except Exception as e:
            print(f"Error comprimiendo la imagen {imagen}: {e}")

    def comprimir_imagenes(self, imagenes, calidad):
        """Comprime todas las imágenes de una carpeta."""
        self.dir_path = imagenes
        
        for archivo in os.listdir(self.dir_path):
            archivo_path = os.path.join(self.dir_path, archivo)
            if any(archivo.endswith(ext) for ext in ['jpg', 'png', 'webp']):
                print(f"[*] Comprimiendo {archivo}")
                self.comprimir(archivo_path, calidad)
            else:
                continue

def main(ruta, imagen, calidad):
    compresor = Comprimir(ruta)
    if os.path.isdir(imagen):
        compresor.comprimir_imagenes(imagen, calidad)
    else:
        compresor.comprimir(imagen, calidad)
    
    print(f"[+] Compresión terminada. Imágenes guardadas en {ruta}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Esta herramienta permite comprimir imágenes a formato lossy y las convierte a webp.")
    parser.add_argument("-r", "--ruta", type=str, required=True, help="La ruta donde se va a guardar la imagen comprimida. ej: -r /home/user/images")
    parser.add_argument("-m", "--img", type=str, required=True, help="La ruta de la imagen o carpeta a comprimir. ej: --img /images/img_to_compress")
    parser.add_argument("-q", "--quality", type=int, required=True, help="La calidad de compresión que se va a usar, ej: -q 75")

    args = parser.parse_args()
    
    main(args.ruta, args.img, args.quality)








