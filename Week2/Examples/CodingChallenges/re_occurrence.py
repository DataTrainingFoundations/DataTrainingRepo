#https://www.codewars.com/kata/5a7e6bd576c0e2f27d00237a

def has_reoccurrence(lst):
    seen = set()
    i = 0
    n = len(lst)

    while i < n:
        item = lst[i]

        # Skip the current sequence of the same item
        while i < n and lst[i] == item:
            i += 1

        # If we have seen this item before, it reoccurs after a break
        if item in seen:
            return True
        seen.add(item)

    return False

print(has_reoccurrence([0,0,1,0,0]))
print(has_reoccurrence([0,0,1,1,2,2,1,1]))
print(has_reoccurrence([0, 0, 0]))
print(has_reoccurrence([0,0,1,1,2,2]))