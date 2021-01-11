bi_tree = {'A' : set(['B', 'C']),\
           'B' : set(['A','D','E']),\
           'C' : set(['A', 'F']),\
           'D' : set(['B']),\
           'E' : set(['B','F']),\
           'F' : set(['C','E'])}

def dfs(bi_tree, start):
    stack = [start] #갈 수 있는 곳
    visited = []

    while stack: #stack에 뭔가 하나라도 있는가 
        n = stack.pop()  
        if n not in visited: #가본적이 없다면
            #여기서 n에 간다.
            visited.append(n) #가본적 있어
            stack += bi_tree[n] #새로운 곳에 갔기때문에 다음 갈 수 있는 곳 추가.
            print(visited)
    return visited

dfs(bi_tree, 'A')


def bfs(bi_tree, start):
    queue = [start]
    visited = []

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue = queue + list(bi_tree[n] - set(visited))
            print(visited)
    return visited

bfs(bi_tree, 'A')

def dfs_paths(bi_tree, start, goal):
    stack = [(start, [start])] #갈 수 있는 곳
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in bi_tree[n] - set(path):
                stack.append((m, path+[m]))
    return result

print('here')

print(dfs_paths(bi_tree, 'A','F'))


def bfs_paths(bi_tree, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in bi_tree[n] - set(path):
                queue.append((m, path + [m]))
    return result


print(bfs_paths(bi_tree, 'A','F'))
