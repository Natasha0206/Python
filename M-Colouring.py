def graphColoring(graph, k, V):
    color=[0]*V
    def mcolor(vertex,graph,k,V):
        if vertex==V:
            return True
        
        for i in range(1,k+1):
            flag=1
            for j in range(V):
                if graph[vertex][j]==1 and color[j]==i:
                    flag=0
                    break
                
            if flag==1:
                    color[vertex]=i
                    if mcolor(vertex+1,graph,k,V):
                        return True
                    
                    color[vertex]=0
        return False
        
    return mcolor(0,graph,k,V)