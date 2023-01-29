class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(graph, node, cur, res):
            if node == len(graph)-1:
                res.append(cur)
                return

            nextNodes = graph[node]
            for nextNode in nextNodes:
                cur.append(nextNode)
                dfs(graph, nextNode, cur.copy(), res)
                cur = cur[:-1]
        
        dfs(graph, 0, [0], res)
        return res
