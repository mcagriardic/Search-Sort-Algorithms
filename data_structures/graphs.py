# example of a graph data structure

class Person(object):
    
    def __init__(self, name, friends=[]):
        self.name = name
        self.friends = friends[:]

    def add_friend(self, friend):
        if isinstance(friend, list):
            self.friends = self.friends + friend
        else:
            self.friends.append(friend)


class SocialNetwork(object):
    
    def traverse(self, starting_vertex):
        visited = []
        queue = [starting_vertex]
        
        while queue:
            if queue[0] not in visited:
                print(queue[0].name)
                visited.append(queue[0])
            deque = queue.pop(0)
            queue = queue + [adjacent_friend for adjacent_friend in deque.friends if adjacent_friend not in visited]


helen = Person("Helen")
fred = Person("Fred")
bob = Person("Bob")
candy = Person("Candy")
irena = Person("Irena")
gina = Person("Gina")
elaine = Person("Elaine")
alice = Person("Alice")
derek = Person("Derek")

fred.add_friend([helen, alice])
bob.add_friend(fred)
gina.add_friend(irena)
derek.add_friend(gina)
alice.add_friend([fred, bob, candy, derek, elaine])

social_network = SocialNetwork()

# Traverse the graph - BFS

social_network.traverse(alice)