def get_exits(directions: dict):
    ans = []
    for k, v in directions.items():
        if v != 'no':
            ans.append(k)
    return ans
