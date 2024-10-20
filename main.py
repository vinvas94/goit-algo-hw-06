from metro_graph import create_metro_graph
from search_algorithms import dfs, bfs
from dijkstra_algorithm import dijkstra
from visualization import visualize_and_save, visualize_weighted_graph
import networkx as nx

def print_analysis(metro_graph):
    """Prints basic analysis of the graph."""
    degree_centrality = nx.degree_centrality(metro_graph)
    print(f"Number of stations (nodes): {metro_graph.number_of_nodes()}")
    print(f"Number of connections (edges): {metro_graph.number_of_edges()}")
    print("Degree of each vertex:")
    for node, degree in degree_centrality.items():
        print(f"{node}: {degree:.2f}")
    

def print_paths(start_station, stations, paths, method):
    """Prints the paths found by the specified algorithm."""
    print(f"\n{method} Paths:")
    for station in stations:
        if station in paths:
            print(f"{start_station} -> {station}: {paths[station]}")

def user_interface(metro_graph, stations):
    """User interface for selecting an algorithm and a station."""
    print("Welcome to the metro route search system.")
    
    # Convert stations to lowercase for case-insensitive comparison
    lowercased_stations = {station.lower(): station for station in stations}
    
    while True:
        print("\nOptions:")
        print("1. Run BFS")
        print("2. Run DFS")
        print("3. Run Dijkstra")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "4":
            print("Exiting the program.")
            break

        start_station = input("Enter the starting station: ").lower()  

        if start_station not in lowercased_stations:
            print(f"Error: The station '{start_station}' does not exist in the graph.")
            continue
        
        # Get the original station name using the case-insensitive map
        start_station_original = lowercased_stations[start_station]

        if choice == "1":
            bfs_paths = bfs(metro_graph, start_station_original)
            print_paths(start_station_original, stations, bfs_paths, "BFS")
        elif choice == "2":
            dfs_paths = dfs(metro_graph, start_station_original)
            print_paths(start_station_original, stations, dfs_paths, "DFS")
        elif choice == "3":
            all_distances = {}
            all_paths = {}
            for station in stations:
                distances, paths = dijkstra(metro_graph, station)
                all_distances[station] = distances
                all_paths[station] = paths
            
            # Display shortest paths from the chosen start station
            print(f"\nShortest paths from {start_station_original}:")
            for station in stations:
                if station != start_station_original:
                    path = all_paths[start_station_original][station] + [station]
                    print(f"{start_station_original} -> {station}: {path}, Distance: {all_distances[start_station_original][station]}")
        else:
            print("Invalid option. Please choose a valid option.")

def main():
    # Create metro graph
    metro_graph, stations = create_metro_graph()

    # Visualize the graph
    visualize_and_save(metro_graph)

    # Analyze the graph
    print_analysis(metro_graph)

    # Run the user interface
    user_interface(metro_graph, stations)

    # Visualize the weighted graph
    visualize_weighted_graph(metro_graph)

if __name__ == "__main__":
    main()

