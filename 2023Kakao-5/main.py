def solution(commands):
    SIZE = 50 * 50

    parent = [i for i in range(SIZE)]
    value = [None] * SIZE

    def idx(r, c):
        return (r - 1) * 50 + (c - 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return

        if value[x] is None and value[y] is not None:
            parent[x] = y
        else:
            parent[y] = x
            if value[x] is None:
                value[x] = value[y]

    answer = []

    for cmd in commands:
        parts = cmd.split()

        if parts[0] == "UPDATE":
            if len(parts) == 4:
                r, c, v = int(parts[1]), int(parts[2]), parts[3]
                root = find(idx(r, c))
                value[root] = v
            else:
                v1, v2 = parts[1], parts[2]
                for i in range(SIZE):
                    if parent[i] == i and value[i] == v1:
                        value[i] = v2

        elif parts[0] == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            union(idx(r1, c1), idx(r2, c2))

        elif parts[0] == "UNMERGE":
            r, c = int(parts[1]), int(parts[2])
            target = idx(r, c)
            root = find(target)
            saved = value[root]

            members = []
            for i in range(SIZE):
                if find(i) == root:
                    members.append(i)

            for m in members:
                parent[m] = m
                value[m] = None

            value[target] = saved

        elif parts[0] == "PRINT":
            r, c = int(parts[1]), int(parts[2])
            root = find(idx(r, c))
            answer.append(value[root] if value[root] else "EMPTY")

    return answer


print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))