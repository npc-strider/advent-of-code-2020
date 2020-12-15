arr = [ int(x) for x in open('input').read().split(',') ]
idx = 30000000

def lookback(n, arr):
    arr.reverse()
    A = 0; c = 0
    for x in arr:
        c += 1
        if x == n:
            if A == 0:
                A = c
            else:
                return c - A
    return 0

def a(arr, idx):
    for t in range(len(arr),idx):
        arr.append(lookback(arr[t-1], arr[:t]))
    return arr[idx-1]

# print(a(arr, idx))
# OK the lookback approach is slow AF. Let's try arr different method!

def lut_search(lut, n, idx):
    if n in lut:
        d = idx - lut[n]
        lut[n] = idx
        return d
    else:
        lut.update({ n: idx })
        return 0
def b(arr, idx):
    lut = { arr[x]:x+1 for x in range(len(arr)) }
    for t in range(len(arr),idx):
        arr.append(lut_search(lut, arr[t-1], t))
    return arr[idx-1] 

print(b(arr, idx))