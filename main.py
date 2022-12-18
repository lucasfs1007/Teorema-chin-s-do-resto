from math import gcd

qntEq = int(input("Quantas equações existem nesse sistema? "))

# Criar vetor para os a, b e n de cada equação
a = []
b = []
n = []

# Ler os valores de a, b e n de cada equação
for i in range(0, qntEq):
    print("Digite o valor de a%d: " % (i+1))
    a.append(int(input()))
    print("Digite o valor de b%d: " % (i+1))
    b.append(int(input()))
    print("Digite o valor de n%d: " % (i+1))
    n.append(int(input()))
    # Verificar se a ou n é diferente de 0
    if(a[i] == 0):
        print("O valor de a deve ser diferente de 0!")
        exit()
    elif(n[i] == 0):
        print("O valor de n deve ser diferente de 0!")
        exit()

# Verificar se o MDC de ai e ni é 1
for i in range(0, qntEq):
    mdc = gcd(a[i], n[i])
    if(mdc != 1):
        print("Os numeros devem ser primos entre si,")
        print("e o MDC(%d, %d) = %d" % (a[i], n[i], mdc))
        print("ou seja, a%d e n%d não são primos entre si." % (i+1, i+1))
        exit()

# Verificar se o MDC de ni e nj é 1
for j in range(i, qntEq):
    if(i != j):
        mdc = gcd(n[i], n[j])
        if(mdc != 1):
            print("Os numeros devem ser primos entre si,")
            print("e o MDC(%d, %d) = %d" % (n[i], n[j], mdc))
            print("ou seja, n%d e n%d não são primos entre si." % (i+1, j+1))
            exit()

# Calcular os x para que as equações sejam satisfeitas
vetorX = []
for i in range(0, qntEq):
    x = 0
    c = 1
while(c != 0):
    x += 1
    c = (a[i]*x - b[i]) % n[i]
    vetorX.append(x)

# Realizar o multiplicatório de todos os n para ficar em N
N = 1
for i in n:
    N *= i

# Criar vetor para os N/ni
Nvet = []
for i in n:
    Nvet.append(int(N/i))

# Criar vetor para os inversos de N/ni
invNvet = []
for i in range(0, qntEq):
    x = 0
    c = 1
while(c != 0):
    # Procura todos os x possíveis para a equação
    # deixar o resto igual a 0
    x += 1
    c = (Nvet[i]*x-1)%n[i]
    invNvet.append(x)

# Calcular o L
L = 0
for i in range(0, qntEq):
    L += vetorX[i]*Nvet[i]*invNvet[i]

print("\nEm x ≡ %d(mod %d)" % (L, N))

# Calcular o x final

"""# Com o res positivo
x = 0
c = 1
achouX = False
while(achouX == False):
x+=1
c = x-L
if(c > 0):
c = c%N
if(c == 0):
achouX = True

print("O valor de x é: %d" % x)"""

# Com o res inteiro
x = 0
c = 1
achouX = False
while(achouX == False):
    x+=1
    c = x-L
    c = c%N
    if(c == 0):
        achouX = True


print("A solução para esse sistema é x = %d" % x)