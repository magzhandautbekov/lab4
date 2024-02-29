def chisla_po_ubyvaniu(n):
    for i in range(n,0,-1):
        yield i

n = int(input())

chisla = chisla_po_ubyvaniu(n)
print(', '.join(map(str,chisla)))
