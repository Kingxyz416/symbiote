v,e=map(int,input("enter a number:").split())
adj=[[0]*v for _ in range(v)]
for i in range(e):
    print(f"enter {i} edge (u v) :")
    u,v=map(int,input().split())
    adj[u][v]=1
    adj[v][u]=1
for row in adj:
    print(*row)



