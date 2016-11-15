#coding=utf-8
from  collections import  deque
class photo():
    def __init__(self):
        self.node_n={}

    def add_nodelist(self,nodelist):
        for i in nodelist:
            self.add_nodes(i)
    def add_node(self,node):
        if not node in self.nodes():
            self.node_n=[]
    def add_edge(self,edge):
        u,v=edge
        if (v not in self.node_n[u] and u not  in self.node_np[v]):
            self.node_n[u].append(v)
            if u!=v:
                self.node_n[v].append(u)
    def nodes(self):
        return  self.node_n.keys()

    def deep(self,root=None):
        self.visited={}
        order=[]
        def dfs(node):
            self.visited[node]=True
            order.append(node)
            for i in self.node_n[node]:
                if not i in self.visited:
                    dfs(i)
        if root:
            dfs(root)
        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        print("order",order)
        return  order
    def wide(self,root=None):
        self.visited={}
        d=deque([])
        order=[]
        def bfs():
            while len(d)>0:
                node=d.popleft()
                self.visited[node]=True
                for i in self.node_n[node]:
                    if not i in d and not i in self.visited:
                        bfs()
                        if root:
                            d.append(root)
                            order.append(root)
                            bfs()
                        for i in self.nodes():
                            if i not in self.visited:
                                d.append(i)
                                order.append(i)
                                bfs()
                                print(order)
                                return order
if __name__=="_main_":
    p=photo()
    i=0
    p.add_nodes([i+1 for i in range(9)])
    print(p)
    p.add_edge((1,2))
    p.add_edge((1,3))
    p.add_edge((2,4))
    p.add_edge((2,5))
    p.add_edge((4,8))
    p.add_edge((5,8))
    p.add_edge((3,6))
    p.add_edge((3,7))
    p.add_edge((6,7))
    print (p.nodes())
    p.wide(1)
