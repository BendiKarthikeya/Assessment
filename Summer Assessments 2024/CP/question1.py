'''Given an empty list and a stream of N numbers. Print min, max, sum, average and 
mode (optional and if there are multiple modes then print any) after insertion of each 
element from the stream to the list.
Example Input:
5
2 4 3 2 -3
Example output
▪ min, max, sum, average and mode after addition of 2 is 2, 2, 2, 2, 2.
▪ min, max, sum, average and mode after addition of 4 is 2, 4, 6, 3, 4.
▪ min, max, sum, average and mode after addition of 3 is 2, 4, 9, 3, 4.
▪ min, max, sum, average and mode after addition of 2 is 2, 4, 11, 2.75, 2.
▪ min, max, sum, average and mode after addition of -3 is -3, 3, 8, 1.6, 2.
'''

N=int(input())
arr=list(map(int,input().split()))
sums=0
for i in arr:
    sums=sums+i
mins=arr[0]
for j in arr:
    if(j<mins):
        mins=j
if(mins==arr[0]):
    maxs=arr[1]
    for w in arr:
        if(w>maxs):
            maxs=w
else:
    maxs=arr[0]
    for w in arr:
        if(w>maxs):
            maxs=w
ave=sums/len(arr)
print(sums)
print(mins)
print(maxs)
print(ave)

'''def min_val(lst):
    return min(lst)

def max_val(lst):
    return max(lst)

def sum_val(lst):
    return sum(lst)

def avg_val(lst):
    return sum(lst) / len(lst)

def mode_val(lst):
    counts = {}
    mode = lst[0]
    max_count = 1
    current_count = 1

    lst.sort()

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            mode = lst[i]

    return mode

if _name_ == "_main_":
    n = int(input())
    a = list(map(int, input().split()))

    v = []

    for i in range(n):
        v.append(a[i])
        print(f"min, max, sum, average and mode after addition of {a[i]} is {min_val(v)} {max_val(v)} {sum_val(v)} {avg_val(v):.2f} {mode_val(v)}")'''
    