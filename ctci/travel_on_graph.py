"""
Return all the possible paths from a vertex to another.
"""

graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "C", "D"],
    "C": ["A", "B"],
    "D": ["A", "B"]
}

def travel(from_, to, path=[]):
    path = path + [from_]
    
    if from_ == to:
        return [path]

    paths=[]
    for dest in graph[from_]:
        if dest not in path:
            ep = f(dest, to, path=path)
            
            for p in ep:
                if p not in paths:
                    paths.append(p)
    return paths

travel(from_="C", to="D")


"""
>> [['C', 'A', 'B', 'D'], ['C', 'A', 'D'], ['C', 'B', 'A', 'D'], ['C', 'B', 'D']]
"""