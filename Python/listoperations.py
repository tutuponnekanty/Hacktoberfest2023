# MINIMUM ELEMENT
def min_list(lst):
    mini = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < mini:
            mini = lst[i]
    return mini

# MAXIMUM ELEMENT
def max_list(lst):
    maxi = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > maxi:
            maxi = lst[i]
    return maxi

# OBVIOUS SORT
def obv_sort(lst):
    x = []
    while lst:
        mini = min_list(lst)
        x.append(mini)
        lst.remove(mini)
    return x

# BEFORE APPEND
def list_append_before(l, z):
    newl = z + l
    return newl

# AFTER APPEND
def list_append_after(l, z):
    newld = l + z
    return newld

# AVERAGE LIST
def avg_list(lst):
    total = sum(lst)
    avg = total / len(lst)
    return avg

# DEFINING LISTS
l = []
f1 = int(input("Enter number of elements in list 1: "))
print("Enter elements in the first list:")
for x in range(f1):
   l.append(int(input()))

z = []
f2 = int(input("Enter number of elements in list 2: "))
print("Enter elements in the second list:")
for m in range(f2):
    z.append(int(input()))

# PRINT    
print("The first list is", l)
print("\nThe second list is", z)
print("\nThe minimum element in the first list is", min_list(l))
print("\nThe maximum element in the first list is", max_list(l))
print("\nThe minimum element in the second list is", min_list(z))
print("\nThe maximum element in the second list is", max_list(z))
print("\nThe obviously sorted list 1 is", obv_sort(l))
print("\nThe obviously sorted list 2 is", obv_sort(z))
print("\nThe second list appended before the first list is", list_append_before(l, z))
print("\nThe second list appended after the first list is", list_append_after(l, z))
