import collections
INF = 99999999999


def find_name_id(name):
    global cnt, name_dict
    if name_dict.get(name) is None:
        name_dict[name] = cnt
        cnt += 1
    return name_dict.get(name)


M, N = map(int, input().split())
node = [INF] * 5000
inDegree = [set() for _ in range(200)]
graph = [[] for _ in range(200)]
recipes = [[] for _ in range(200)]
name_dict = {}
cnt = 0

q = collections.deque()
for _ in range(M):
    s, v = input().split()
    name_id = find_name_id(s)
    node[name_id] = min(node[name_id], int(v))

for i in range(N):
    s, v = input().split("=")
    name_id = find_name_id(s)

    recipe = []
    for j in v.split("+"):
        num = int(j[0])
        name = j[1:]
        j_id = find_name_id(name)
        inDegree[name_id].add(j_id)
        recipe.append([j_id, num])
        graph[j_id].append(name_id)
    recipes[name_id].append(recipe)

temp = [0] * cnt
for i in range(cnt):
    temp[i] = len(inDegree[i])
inDegree = temp

for i in range(0, cnt):
    if inDegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for next in graph[now]:
        inDegree[next] -= 1
        if inDegree[next] == 0:
            for recipe in recipes[next]:
                temp = 0
                for index, value in recipe:
                    temp += node[index] * value
                node[next] = min(node[next], temp)
            q.append(next)

if name_dict.get("LOVE") is None:
    print(-1)
else:
    love_id = find_name_id("LOVE")
    if node[love_id] == INF:
        print(-1)
    elif node[love_id] > 1000000000:
        print(1000000001)
    else:
        print(node[love_id])