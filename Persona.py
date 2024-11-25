import networkx as nx

class Persona:
    def __init__(self, name, base_time, position):
        """
        name: Nombre de la persona
        base_time: Tiempo base para recorrer una cuadra
        position: Posición inicial (calle, carrera)
        """
        self.name = name
        self.base_time = base_time
        self.position = position

    def calcular_ruta_mas_corta(self, ciudad, destino): 
        grafo = ciudad.obtener_grafo() 
        return nx.dijkstra_path(grafo, self.position, destino, weight=self.base_time)
    
    def calcular_tiempo_ruta(self, ciudad, ruta): 
        tiempo_total = 0 
        grafo = ciudad.obtener_grafo() 
        for i in range(len(ruta) - 1): 
            tiempo_total += grafo[ruta[i]][ruta[i + 1]][self.base_time] 
        return tiempo_total