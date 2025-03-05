#Autor: xXJuanDavidXx
# Este script, debe recibir mascara de red y dirección ip de destino
#
#su propósito de calcular y presentar información sobre una subred dada una máscara de red y una dirección IP



from rich.console import Console
from rich.table import Table
import ipaddress
import argparse


def convertir_ip_a_binario(ip):
    """
    Conversor de ip a binario recibe una lista, devuelve una lista.
    """
    return [bin(octeto)[2:].zfill(8) for octeto in ip] #Elimino el 0b y me aseguro de que se represente un byte con .zfill
    

def binario_a_decimal(ip):
    """
    Conversor de ip binaria a decimal, recibe una lista devuelve una lista.
    """
    return [int(octeto, 2) for octeto in ip] #convierte cual quier valor binario a decimal int recibe el valor y la base 2



def operacion_and(netmask, ip):
    """
    Función que identifica a qué red pertenece una dirección IP.
    
    Args:
        netmask : list => Lista de cadenas binarias que representan la máscara de red.
        ip : list => Lista de cadenas binarias que representan la IP.
    
    """
    red = []

    # Realiza la operación AND bit a bit
    for byte1, byte2 in zip(netmask, ip):
        octeto = ""
        for bit1, bit2 in zip(byte1, byte2):
            if bit1 == "1" and bit2 == "1":
                octeto += "1"
            else:
                octeto += "0"
        red.append(octeto)
    
    # Une los octetos con puntos para formar una dirección IP
    return red


def notacion_CIDR(netmask):
    """Recibe la mascara de red en forma de lista y devuelve la notación CIDR de la red y los hosts
    args:
        netmask : list
    """
    prefijo_red = ""
    sufijo_host = ""
    for i in netmask:
        for j in i:
            if j == "1":
                prefijo_red += "1"
            else:
                sufijo_host += "0"
            
    cidr_red = len(prefijo_red)
    cidr_host = len(sufijo_host)
    return cidr_red, cidr_host
    

def rango_direcciones(red, cidr_red):
    """
    recibe la red y su notación CIDR y devuelve la cantidad de direcciones que pueden recibir los hosts
    """
    
    red_addr = ".".join(map(str, red)) + "/" + str(cidr_red)
    obj_red = ipaddress.ip_network(red_addr)

    direccion_red = obj_red.network_address
    direccion_broadcast = obj_red.broadcast_address


    return direccion_red + 1, direccion_broadcast - 1
    
    




def main(netmask, ip):

    # Convertimos los parametros recibidos en listas de numeros.
    
    netmask = list(map(int, netmask.split(".")))
    ip = list(map(int, ip.split(".")))


    # Convertimos ambos parámetros a una lista en binario
    netmask_bin = convertir_ip_a_binario(netmask)
    ip_bin = convertir_ip_a_binario(ip)
    
    # Calculamos la notación CIDR que corresponde a la red y a los hosts
    cidr_red, cidr_host = notacion_CIDR(netmask_bin)
    
    # Calculamos la capacidad de la red y de hosts
    # Nota: La capacidad total de direcciones se determina por los bits de host.
    capacidad_total = 2 ** cidr_host       # Ej. para /24 son 256 direcciones
    capacidad_hosts = capacidad_total - 2    # Restamos red y broadcast

    # Identificamos la red mediante operación AND
    red_bin = operacion_and(netmask_bin, ip_bin)
    red_decimal = binario_a_decimal(red_bin)
    
    # Rango de direcciones que pueden recibir los hosts
    direccion_red, direccion_broadcast = rango_direcciones(red_decimal, cidr_red)
    
    # Usando rich para presentar la información en una tabla
    console = Console()
    table = Table(title="Información de Red")

    # Definimos las columnas
    table.add_column("Parámetro", style="cyan", no_wrap=True)
    table.add_column("Valor", style="magenta")

    # Agregamos las filas
    table.add_row("Máscara de red (decimal)", ".".join(str(net) for net in netmask))
    table.add_row("Máscara de red (binario)", ".".join(netmask_bin))
    table.add_row("CIDR de la red", f"/{cidr_red}")
    table.add_row("CIDR para hosts", f"/{cidr_host}")
    table.add_row("Capacidad total de la red", str(capacidad_total - 2))
    table.add_row("Red identificada (decimal)", ".".join(map(str, red_decimal)))
    table.add_row("Red identificada (binario)", ", ".join(red_bin))
    table.add_row("Rango de IP asignables", f"{direccion_red} - {direccion_broadcast}")

    # Imprimimos la tabla en la consola
    console.print(table)




if __name__=="__main__":

   
    parser = argparse.ArgumentParser(description="Este script nos permite calcular la información de una red.")
    parser.add_argument("-m", "--netmask", type=str, required=True, help="La mascara de red en formato x.x.x.x")
    parser.add_argument("-i", "--ip", type=str, required=True, help="La ip de la red en formato x.x.x.x")  
    
    args = parser.parse_args()
    main(args.netmask, args.ip)

