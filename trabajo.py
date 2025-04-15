import networkx as nx
import matplotlib.pyplot as plt

# Crear una red social como un grafo no dirigido
def crear_red_social():
    G = nx.Graph()
    G.add_edges_from([
        (0, 1), (1, 2), (2, 3), (1, 4),
        (4, 5), (0, 6), (6, 7), (7, 8),
        (8, 9), (5, 9)
    ])
    return G

# Aplicar Floyd-Warshall para obtener caminos más cortos
def obtener_caminos_mas_cortos(G):
    return dict(nx.floyd_warshall(G))

# Simulación de propagación desde un nodo origen
def simular_propagacion(caminos, origen):
    tiempo_llegada = {}
    for nodo in caminos[origen]:
        tiempo_llegada[nodo] = int(caminos[origen][nodo])  # tiempo = distancia
    return tiempo_llegada

# Visualizar el grafo y tiempos de llegada
def visualizar_propagacion(G, tiempos, origen):
    pos = nx.spring_layout(G)
    colores = [tiempos[n] for n in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=colores, cmap=plt.cm.plasma, node_size=800)
    etiquetas = {n: f"{n}\n{tiempos[n]}s" for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=etiquetas, font_color='white')
    plt.title(f"Propagación desde nodo {origen}")
    plt.colorbar(plt.cm.ScalarMappable(cmap=plt.cm.plasma), label="Tiempo de llegada")
    plt.show()

# Función principal
def main():
    G = crear_red_social()
    caminos = obtener_caminos_mas_cortos(G)
    nodo_origen = 0
    tiempos = simular_propagacion(caminos, nodo_origen)
    visualizar_propagacion(G, tiempos, nodo_origen)

if __name__ == "__main__":
    main()
