#!/bin/bash
#
# Autor : xXJuanDavidXx

# Verificamos si se han proporcionado los argumentos necesarios
if [ -z "$1" ]; then
  echo "Uso: $0 <ruta_del_directorio> <nombre_del_archivo> <ruta_destino>"
  exit 1
fi

if [ -z "$2" ]; then
  echo "Uso: $0 <ruta_del_directorio> <nombre_del_archivo> <ruta_destino>"
  exit 1
fi

if [ -z "$3" ]; then
  echo "Uso: $0 <ruta_del_directorio> <nombre_del_archivo> <ruta_destino>"
  exit 1
fi

ruta="$1"
nombre="$2"
destino="$3"

# Ejecutamos el comando find y guardamos la ruta completa del archivo encontrado
archivo=$(find "$ruta" -type f -name "$nombre")

# Verificamos si se encontró el archivo
if [ -z "$archivo" ]; then
  echo "Archivo no encontrado"
  exit 1
fi

# Copiamos el archivo al destino
while IFS= read -r file; do
  cp "$file" "$destino"
  if [ $? -eq 0 ]; then
    echo "Archivo copiado exitosamente a $destino"
  else
    echo "Error al copiar el archivo: $file"
    exit 1
  fi
done <<< "$archivo"
