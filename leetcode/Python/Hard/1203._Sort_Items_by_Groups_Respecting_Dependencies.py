from collections import deque


class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:

        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m+=1

        groups = {i: [] for i in range(m)}
        for i in range(n):
            groups[group[i]].append(i)


        adj = {i:[] for i in range(n)}
        indegree = {i:0 for i in range(n)}
        group_adj = {i: [] for i in range(m)}
        group_indegree = {i: 0 for i in range(m)}

        for i in range(n):
            for j in beforeItems[i]:
                adj[j].append(i)
                indegree[i]+=1
                if group[j] != group[i]:
                    group_adj[group[j]].append(group[i])
                    group_indegree[group[i]]+=1


        def kahns(d, adj, indegree):
            order = []
            while d:
                v = d.popleft()
                order.append(v)
                for i in adj[v]:
                    indegree[i]-=1
                    if indegree[i] == 0:
                        d.append(i)
            return order if len(order) == len(adj) else []

        item_order = kahns(deque(i for i in indegree if indegree[i] == 0), adj, indegree)

        group_order = kahns(deque(i for i in group_indegree if group_indegree[i] == 0), group_adj, group_indegree)

        if not item_order or not group_order:
            return []

        ans = []

        o = {i: [] for i in range(m)}

        for i in item_order:
            o[group[i]].append(i)

        # return group_order, o
        for i in group_order:
            ans.extend(o[i])
        return ans



s = Solution()
print(s.sortItems(n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]))