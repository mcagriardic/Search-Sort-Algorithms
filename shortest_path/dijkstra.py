# Dijkstra's Algorithm (shortest path) Implementation

def print_city_instances(lst_city_instances):
    for city in lst_city_instances:
        print(city.name)

def print_dict(dict_):
    for k,v in dict_.items():
        print("%s: %s" %(k.name, v))

def print_results(queue, shortest_path, visited, current_vertex):
    print("QUEUE ELEMENTS...")
    print_city_instances(queue)
    print("\n")
    
    print("SHORTEST PATH ELEMENTS...")
    print_dict(shortest_path)
    print("\n")
    
    print("VISITED ELEMENTS...")
    print_city_instances(visited)
    print("\n")
    
    print("CURRENT VERTEX")
    print(current_vertex.name)


class City(object):
    
    def __init__(self, name):
        self.name = name
        self.route = {}
        
    def add_route(self, to, distance):
        self.route[to] = distance
    
    @property
    def adjacent(self):
        # returns the list of adjacent vertices sorted in ascending order
        # according to its value
        return sorted(self.route, key=self.route.get)
        
    def __str__(self):
        return " --- ".join(["%s: %s" %(k.name, v) for k,v in self.route.items()])
    
    
class FlightNetwork(object):
    
    def find_cheapest_flights_from(self, starting_vertex):
        current_vertex = starting_vertex
        visited = []
        shortest_path = {}
        queue = [starting_vertex]
        
        # index = 0
        while queue:
            # index += 1
#             if index == 5:
#                 return queue, shortest_path, visited, current_vertex
            if current_vertex not in visited:
                for adjacent in current_vertex.adjacent:
                    if adjacent in shortest_path:
                        alternative_route = shortest_path[current_vertex] + current_vertex.route[adjacent]
                        if alternative_route < shortest_path[adjacent]:
                            shortest_path[adjacent] = alternative_route
                    else:
                        try:
                            shortest_path[adjacent] = shortest_path[current_vertex] + current_vertex.route[adjacent]
                        except KeyError:
                            shortest_path[adjacent] = current_vertex.route[adjacent]

                    if adjacent not in visited and adjacent not in queue:
                        queue.append(adjacent)
                
                visited.append(queue.pop(0))
                if queue:
                    current_vertex = queue[0]
                else:
                    print_dict(shortest_path)
                    return shortest_path


atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)

boston.add_route(chicago, 120)
boston.add_route(denver, 180)

chicago.add_route(el_paso, 80)

denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)

el_paso.add_route(boston, 100)

flights = FlightNetwork()

shortest_path = flights.find_cheapest_flights_from(atlanta)

# queue, shortest_path, visited, current_vertex = flights.find_cheapest_flights_from(atlanta)
# print_results(queue, shortest_path, visited, current_vertex)