graph = {
'S.Complex':[('Siwaka',0.73)],
'Siwaka':[('Ph.1A',0.38), ('Ph.1B',0.28)],
'Ph.1A':[('Ph.1B',0.28), ('Mada',0.63)],
'Ph.1B':[('STC',0.213), ('Ph.2',0.21)],
'J1':[('Mada',0.63)],
'Mada':[('Parking Lot',0)],
'Parking Lot':[],
'STC':[('Parking Lot',0)],
'Ph.2':[('STC',0.213),('Ph.3',0.16)],
'Ph.3':[('Parking Lot',0)]
}
def bfs2(start, target, graph, queue=[], visited=[]):
    if start not in visited:
        print(start)
        visited.append(start)
    queue=queue+[x for x in graph[start] if x[0][0] not in visited]
    queue.sort(key=lambda x:x[1])
    if queue[0][0]==target:
        print(queue[0][0])
    else:
        processing=queue[0]
        queue.remove(processing)
        bfs2(processing[0], target, graph, queue, visited)
