# Author: CRS 01/10/22
def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = v * 2
    return lst


print(double_stuff([0, 1, 2, 3]) == [0, 2, 4, 6])
print(double_stuff([0.1, 1.2, 2.3, 3.4]) == [0.2, 2.4, 4.6, 6.8])
print(double_stuff(["0", 1, 2.3, 3]) == ["00", 2, 4.6, 6])
