def main():
    V, E = map(int, input("Enter number of vertices and edges: ").split())

    adj = [[] for _ in range(V)]

    print(f"Enter {E} edges (u v), 0-indexed:")
    for _ in range(E):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)  
        

    print("\nAdjacency list:")
    for i in range(V):
        print(f"{i} -> {' '.join(map(str, adj[i]))}")


if __name__ == "__main__":
    main()