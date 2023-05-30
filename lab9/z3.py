import networkx as nx
import matplotlib.pyplot as plt

def budowa_grafu():
    rodzaj_g = int(input("Podaj typ grafu:\n 1 - skierowany\n 2 - nieskierowany): "))
    wierzcholki = int(input("Podaj liczbę wierzchołków: "))
    polaczenia = int(input("Podaj liczbę połączeń: "))

    graf = nx.DiGraph() if rodzaj_g == 1 else nx.Graph()

    for i in range(wierzcholki): graf.add_node(i) #dodawanie wierzchołków do grafu

    for x in range(polaczenia):
        od_wierzch = int(input("Podaj wierzchołek początkowy: "))
        do_wierzch = int(input("Podaj wierzchołek końcowy: "))
        waga = float(input("Podaj wagę połączenia: "))

        graf.add_edge(od_wierzch, do_wierzch, weight=waga)

    macierz_sasiedztwa = nx.adjacency_matrix(graf).todense()
    lista_sasiedztwa = dict(graf.adjacency())

    print("Macierz sąsiedztwa:")
    print(macierz_sasiedztwa)

    print("Lista sąsiedztwa:")
    print(lista_sasiedztwa)

    nx.draw(graf, with_labels=True, node_color="lightblue", node_size=800, edge_color="gray")
    plt.show()

budowa_grafu()