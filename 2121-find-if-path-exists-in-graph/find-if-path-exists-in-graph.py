class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        book={}
        if source == destination:
                return True
        for a,b in edges:
            if a in book:
                book[a].append(b)
            else:
                book[a]=[b]

            if b in book:
                book[b].append(a)
            else:
                book[b]=[a]

        visited = set()
        def explore(room):
            
            if room in visited:
                return
            else:
                visited.add(room)
                for nb in book[room]:
                    explore(nb)
                
        explore(source)
        return destination in visited
                

            