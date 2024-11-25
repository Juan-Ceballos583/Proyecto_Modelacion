import networkx as nx

class RutaOptima:
    def __init__(self, javier, andreina, ciudad): 
        self.javier = javier 
        self.andreina = andreina 
        self.ciudad = ciudad

    def calcular_rutas_y_tiempos(self, destino): 
        ruta_javier = self.javier.calcular_ruta_mas_corta(self.ciudad, destino) 
        ruta_andreina = self.andreina.calcular_ruta_mas_corta(self.ciudad, destino)

        tiempo_javier = self.javier.calcular_tiempo_ruta(self.ciudad, ruta_javier) 
        tiempo_andreina = self.andreina.calcular_tiempo_ruta(self.ciudad, ruta_andreina)

        if tiempo_javier > tiempo_andreina: 
            diferencia = tiempo_javier - tiempo_andreina 
            return ruta_javier, ruta_andreina, f"Andreína debe salir {diferencia} minutos antes." 
        elif tiempo_javier < tiempo_andreina: 
            diferencia = tiempo_andreina - tiempo_javier 
            return ruta_javier, ruta_andreina, f"Javier debe salir {diferencia} minutos antes." 
        else: 
            return ruta_javier, ruta_andreina, "Ambos deben salir al mismo tiempo."