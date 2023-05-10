from collections import Counter
from typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        # Inicializamos los acumuladores
        total_temperatura = 0
        total_humedad = 0
        total_presion = 0
        total_velocidad_viento = 0
        total_medidas = 0
        direcciones_viento = []

        with open(self.nombre_archivo, 'r') as f:
            bloque_datos = []
            for linea in f:
                if linea.strip():  # Si la línea no está vacía
                    bloque_datos.append(linea)
                else:  # Si la línea está vacía, se ha terminado un bloque de datos
                    total_temperatura += float(bloque_datos[5].split(": ")[1])
                    total_humedad += float(bloque_datos[6].split(": ")[1])
                    total_presion += float(bloque_datos[7].split(": ")[1])
                    viento = bloque_datos[8].split(": ")[1].split(',')
                    total_velocidad_viento += float(viento[0])
                    direcciones_viento.append(viento[1].strip())
                    total_medidas += 1
                    bloque_datos = []  # Reiniciar bloque de datos para la próxima estación

        # Si quedó un bloque de datos sin procesar (última estación)
        if bloque_datos:
            total_temperatura += float(bloque_datos[5].split(": ")[1])
            total_humedad += float(bloque_datos[6].split(": ")[1])
            total_presion += float(bloque_datos[7].split(": ")[1])
            viento = bloque_datos[8].split(": ")[1].split(',')
            total_velocidad_viento += float(viento[0])
            direcciones_viento.append(viento[1].strip())
            total_medidas += 1

        # Calculamos los promedios
        promedio_temperatura = total_temperatura / total_medidas
        promedio_humedad = total_humedad / total_medidas
        promedio_presion = total_presion / total_medidas
        promedio_velocidad_viento = total_velocidad_viento / total_medidas

        # Calculamos la dirección predominante del viento
        conteo_direcciones = Counter(direcciones_viento)
        direccion_predominante = conteo_direcciones.most_common(1)[0][0]

        return (f"La temperatura promedio: {promedio_temperatura}\nPromedio humedad: {promedio_humedad}\npromedio presion: {promedio_presion}\n {promedio_velocidad_viento}\n {direccion_predominante}\n")
    
    def ver_archivo(self):
        info_total = ""
        with open('prueba.txt', 'r') as mi_archivo:
            lineas = mi_archivo.readlines()
            for i in lineas:
                info_total+=(i.replace('\n', ''))
                info_total+= "\n"
                info_total+=("------------------------------------")
                info_total+= "\n"
            return info_total

abrir_archivo = DatosMeteorologicos("prueba.txt")
print(abrir_archivo.ver_archivo())
print(abrir_archivo.procesar_datos())
