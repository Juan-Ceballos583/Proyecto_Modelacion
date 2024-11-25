import networkx as nx
class Ciudad:
    #def __init__(self):
    #    self.adjacency_list = {}
    
    #def add_edge(self, start, end, weight):
    #    if start not in self.adjacency_list:
    #        self.adjacency_list[start] = []
    #    if end not in self.adjacency_list:
    #        self.adjacency_list[end] = []
        
    #    self.adjacency_list[start].append((end, weight))
    #    self.adjacency_list[end].append((start, weight))
    
    #def get_neighbors(self, node):
     #   return self.adjacency_list.get(node, [])

    def __init__(self): 
        self.grafo = nx.Graph() 
        self.agregar_nodos_y_aristas() 
        
    def agregar_nodos_y_aristas(self): 
        tiempos_javier = {'normal': 4, 'malo': 6, 'comercial': 8} 
        tiempos_andreina = {'normal': 6, 'malo': 8, 'comercial': 10} 
        
        for calle in range(50, 56): 
            for carrera in range(10, 16): 
                self.grafo.add_node((calle, carrera)) 
        
        for calle in range(50, 56): 
            for carrera in range(10, 15): 
                if carrera in [12, 13, 14]: 
                    tiempo = tiempos_javier['malo'] 
                elif calle == 51: 
                    tiempo = tiempos_javier['comercial'] 
                else: tiempo = tiempos_javier['normal'] 
                self.grafo.add_edge((calle, carrera), (calle, carrera + 1), weight=tiempo, andreina=tiempo + 2) 
                
        for calle in range(50, 55): 
            for carrera in range(10, 16): 
                if carrera in [12, 13, 14]: 
                    tiempo = tiempos_javier['malo'] 
                elif calle == 51: 
                    tiempo = tiempos_javier['comercial'] 
                else: 
                    tiempo = tiempos_javier['normal'] 
                self.grafo.add_edge((calle, carrera), (calle + 1, carrera), weight=tiempo, andreina=tiempo + 2) 
                
    def obtener_grafo(self):
        return self.grafo