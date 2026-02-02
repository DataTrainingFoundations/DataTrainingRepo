#https://www.codewars.com/kata/5884b6550785f7c58f000047

def group(arr):
    seen = {}
    order = []

    for x in arr:
        if x not in seen:
            seen[x] = [x]
            order.append(x)
        else:
            seen[x].append(x)

    return [seen[x] for x in order]

print(group([3, 2, 6, 2, 1, 3]))