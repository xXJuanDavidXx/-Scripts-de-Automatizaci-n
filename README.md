# Scripts de Automatización

Este repositorio contiene scripts de automatización creados para optimizar mi flujo de trabajo según las necesidades que vayan surgiendo.

## Scripts disponibles

### 📂 `ordenar.py`
Este script organiza automáticamente los archivos de imagen y PDF dentro del directorio en el que se ejecuta.

🔹 **Futuras mejoras:**
- Añadir interacción para permitir al usuario seleccionar los tipos de archivos a organizar, el directorio de origen y el de destino.

### 🖼️ `compresor_imagenes.py`
Este script comprime imágenes en formato **WebP** con compresión **lossy**. Puede procesar una imagen individual o todas las imágenes de una carpeta.

🔹 **Uso:**
Ejecuta el siguiente comando en la terminal para ver el uso:
```sh
python compresor_de_imagenes.py
```

### Subnetting Script

#### Descripción

Este script está diseñado para facilitar la tarea de subnetting. Recibe como entrada una máscara de red y una dirección IP de destino, y proporciona información detallada sobre la subred, como la notación CIDR, el rango de direcciones IP asignables, y más.


#### Uso

Para ejecutar el script, necesitas proporcionar la máscara de red y la dirección IP de destino como argumentos. Aquí tienes un ejemplo de cómo hacerlo desde la línea de comandos:

```sh
python script.py --netmask 255.255.255.0 --ip 192.168.1.1
```

#### Ejemplo de Salida

Aquí tienes un ejemplo de la salida que genera el script:

```
╔═════════════════════════════╗
║      Información de Red     ║
╚═════════════════════════════╝
╔═════════════════════════════╗
║ Parámetro                   ║ Valor                         ║
╠═════════════════════════════╣═══════════════════════════════╣
║ Máscara de red (decimal)    ║ 255.255.255.0                 ║
║ Máscara de red (binario)    ║ 11111111.11111111.11111111.00000000 ║
║ CIDR de la red              ║ /24                           ║
║ CIDR para hosts             ║ /8                            ║
║ Capacidad total de la red   ║ 254                           ║
║ Red identificada (decimal)  ║ 192.168.1.0                   ║
║ Red identificada (binario)  ║ 11000000, 10101000, 00000001, 00000000 ║
║ Rango de IP asignables      ║ 192.168.1.1 - 192.168.1.254   ║
╚═════════════════════════════╝
```


### Script de Búsqueda y Copia de Archivos

#### Descripción

Este script está diseñado para buscar archivos en un directorio específico y copiarlos a una carpeta de salida indicada. Recibe como entrada una lista de archivos a buscar, el directorio donde se realizará la búsqueda y el directorio de salida donde se copiarán los archivos encontrados.


#### Uso

Para ejecutar el script, necesitas proporcionar la lista de archivos, el directorio donde buscar y el directorio de salida como argumentos. Aquí tienes un ejemplo de cómo hacerlo desde la línea de comandos:

```sh
python script.py --lista /ruta/a/lista.txt --directorio /ruta/del/directorio --directorio_salida /ruta/del/directorio_salida
```


