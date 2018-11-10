1. 首先有一个概念：回溯
　　回溯法(探索与回溯法)是一种选优搜索法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。

- 深度优先算法：
（1）访问初始顶点v并标记顶点v已访问。
（2）查找顶点v的第一个邻接顶点w。
（3）若顶点v的邻接顶点w存在，则继续执行；否则回溯到v，再找v的另外一个未访问过的邻接点。
（4）若顶点w尚未被访问，则访问顶点w并标记顶点w为已访问。
（5）继续查找顶点w的下一个邻接顶点wi，如果v取值wi转到步骤（3）。直到连通图中所有顶点全部访问过为止。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-dafc576a99ef461a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/6634703-843365c7be3d2bf6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 广度优先算法：
（1）顶点v入队列。
（2）当队列非空时则继续执行，否则算法结束。
（3）出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。
（4）查找顶点v的第一个邻接顶点col。
（5）若v的邻接顶点col未被访问过的，则col入队列。
（6）继续查找顶点v的另一个新的邻接顶点col，转到步骤（5）。
         直到顶点v的所有未被访问过的邻接点处理完。转到步骤（2）。
![image.png](https://upload-images.jianshu.io/upload_images/6634703-90a06eb985b7914d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
####代码实现
- 图结构
```
class Graph:
    class Vertex:
        __slots__='_element'
        def __init__(self,x):
            self._element = x
        def element(self):
            return self._element
        def __hash__(self):
            return hash(id(self))
    class Edge:
        __slots__='_origin','_destination','_element'
        def __init__(self,u,v,x):
            self._origin =u
            self._destination=v
            self._element=x
        def endpoints(self): # 返回元组（u,v）
            return (self._origin,self._destination)
        def opposite(self,v):
            return self._destination if v is self._origin else self._origin
        def element(self):
            return self._element
        def __hash__(self):
            return hash(self._origin,self._destination)
            
    def __init__(self,directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing # 只有在有向图的时候激活
    def is_directed(self):
        return self._incoming is not self._outgoing
    def vertex_count(self):
        return len(self._outgoing)
    def vertices(self):
        return self._outgoing.keys()
    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total//2 # 有向图边是无向图的两倍
    def edges(self):
        result =set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values) # The A.update(B) adds elements from the set B to A.
        return result
    def get_edge(self,u,v):
        return self._outgoing[u].get(v)
    def degree(self,v,outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    def incident_edges(self,v,outgoing=True):
        adj=self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    def insert_vertex(self,x=None):
        v=self.Vertex(x)
        self._outgoing[v]={}
        if self.is_directed():
            self._incoming[v]={}
        return v
    def insert_edge(self,u,v,x=None):
        e = self.Edge(u,v,x)
        self._outgoing[u][v]=e
        self._incoming[v][u]=e
```
- 深度遍历与广度遍历
```
# 深度遍历
def DFS(g,u,discovered):
    for e in g.incident_edges(): # for every outgoing edge from u
        v= e.opposite(u)
        if v not in discovered:
            discovered[v]=e
            DFS(g,v,discovered)
# 广度遍历
def BFS(g,s,discovered):
    level=[s]
    while len(level)>0:
        next_level=[]
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v]=e
                    next_level.append(v)
        level=next_level
```
