def fat(n):
    if n == 0:
        return 0
    else:
        return n + fat(n-1)


resultado = fat(24)
print(resultado)
