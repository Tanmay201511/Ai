def dfs(a,b,visited):
    if (a,b) in visited:
     return False

    visited.add((a,b))
    print(a,b)

    if a == 2 or b == 2:
        print("Goal Reached!")
        return True

    if dfs(4,b,visited):
       return True
    if dfs(a,3,visited):
     return True

    if dfs(0,b,visited):
      return True
    if dfs(a,0,visited):
      return True

    transfer=min(a,3-b)
    if dfs(a-transfer,b+transfer,visited):
      return True

    transfer= min(b,4-a)
    if dfs(a+transfer,b-transfer,visited):
      return True

    return False

    
visited =set()
dfs(0,0,visited)
    