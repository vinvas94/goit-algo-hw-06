import networkx as nx

# Create the metro graph and add stations
def create_metro_graph():
    metro_graph = nx.Graph()

    # List of stations
    stations = [
        "Puerta del Sur", "San Nicasio", "Leganés Central", "Hospital Severo Ochoa", 
        "Casa del Reloj", "Julian Besteiro", "El Carrascal", "El Bercial", 
        "Los Espartales", "El Casar", "Juan de la Cierva", "Getafe Central", 
        "Alonso de Mendoza", "Conservatorio", "Arroyo Culebro", "Parque de los Estados",
        "Fuenlabrada Central", "Parque Europa", "Hospital de Fuenlabrada", "Loranca", 
        "Manuela Malasaña", "Hospital de Móstoles", "Pradillo", "Móstoles Central", 
        "Universidad Rey Juan Carlos", "Parque Oeste", "Alcorcón Central", "Parque Lisboa"
    ]

    # Edges with weights (distances)
    metro_edges = [
        ("Puerta del Sur", "San Nicasio", 2),
        ("San Nicasio", "Leganés Central", 2),
        ("Leganés Central", "Hospital Severo Ochoa", 1),
        ("Hospital Severo Ochoa", "Casa del Reloj", 1),
        ("Casa del Reloj", "Julian Besteiro", 1),
        ("Julian Besteiro", "El Carrascal", 1),
        ("El Carrascal", "El Bercial", 2),
        ("El Bercial", "Los Espartales", 1),
        ("Los Espartales", "El Casar", 1),
        ("El Casar", "Juan de la Cierva", 2),
        ("Juan de la Cierva", "Getafe Central", 2),
        ("Getafe Central", "Alonso de Mendoza", 1),
        ("Alonso de Mendoza", "Conservatorio", 1),
        ("Conservatorio", "Arroyo Culebro", 1),
        ("Arroyo Culebro", "Parque de los Estados", 2),
        ("Parque de los Estados", "Fuenlabrada Central", 1),
        ("Fuenlabrada Central", "Parque Europa", 1),
        ("Parque Europa", "Hospital de Fuenlabrada", 1),
        ("Hospital de Fuenlabrada", "Loranca", 2),
        ("Loranca", "Manuela Malasaña", 1),
        ("Manuela Malasaña", "Hospital de Móstoles", 1),
        ("Hospital de Móstoles", "Pradillo", 1),
        ("Pradillo", "Móstoles Central", 1),
        ("Móstoles Central", "Universidad Rey Juan Carlos", 2),
        ("Universidad Rey Juan Carlos", "Parque Oeste", 1),
        ("Parque Oeste", "Alcorcón Central", 1),
        ("Alcorcón Central", "Parque Lisboa", 1),
        ("Parque Lisboa", "Puerta del Sur", 1)
    ]

    # Add edges with weights
    metro_graph.add_weighted_edges_from(metro_edges)
    return metro_graph, stations
