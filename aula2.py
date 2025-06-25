#python não tem vetor, mas tem lista(que é mais flexiveç,é mais versatil)
#vetores: são variaveis, possuem muitos valores e todos devem possuir o mesmo tipo de dado (não pode ser int ou float ou bool, apenas um desses
#indice: número dentros dos colchetes ([]), representa a posição que estamos acessando dentro do vetor
#obs: em python, a primeira posição é representada pelo índice 0 e a última posição é representada pelo indice n - 1 (n = tamanho do vetor)




#aluno = ["Jorge", "Caio", "Manoel"]
#print(aluno)
#y = int(input("Quantos alunos tem nessa turma? "))
#lista[0] = [""] * y
#lista[0] = "Jorge" 
#print("Na posição", 0 "está o aluno", lista[0])

#nums = [9, 18, 41, 65, 88, 121]
#nomes = ["Rafael", "Ayslan", "Daniela", "Frank"]
#numfloat = [3290.90, 128.50, 85.90, 789.31]
# x = [0] * 5
# x[0] = int(input("Digite um número: "))
# x[1] = int(input("Digite um número: "))
# x[2] = int(input("Digite um número: "))
# x[3] = int(input("Digite um número: "))
# x[4] = int(input("Digite um número: "))
# print(x)
# print([x[4], x[3], x[2], x[1], x[0]])
# print(x[0] * 2, x[1] * 2, x[2] * 2, x[3] * 2, x[4] * 2)
# print(x[0] / 2, x[1] / 2, x[2] / 2, x[3] / 2, x[4] / 2)


# nome = [0] * 4
# nome[0] = input("Nome: ")
# nome[1] = input("Endereço: ")
# nome[2] = input("Telefone: ")
# nome[3] = input("Email: ")
# print(nome)

vetor = [0] * 4
vetor[0] = float(input("Digite um número: "))
vetor[1] = float(input("Digite um número: "))
vetor[2] = float(input("Digite um número: "))
vetor[3] = float(input("Digite um número: "))
print(vetor[0] + vetor[1] + vetor[2] + vetor[3])
print((vetor[0] + vetor[1] + vetor[2] + vetor[3]) / 4)
print(vetor[0] * vetor[1] * vetor[2] * vetor[3])
maiorqmil = 0
if(vetor[0] > 1000):
    maiorqmil += 1
if(vetor[1] > 1000):
    maiorqmil += 1 
if(vetor[2] > 1000):
    maiorqmil +=1
if(vetor[3] > 1000):
    maiorqmil +=1
print(f"O número de valores maior que mil é: {maiorqmil}")
maior = None
if maior is None or maior < vetor[0]:
    maior = vetor[0]
if maior is None or maior < vetor[1]:
    maior = vetor[1]
if maior is None or maior < vetor[2]:
    maior = vetor[2]
if maior is None or maior < vetor[3]:
    maior = vetor[3]
print(f"O maior valor é: {maior}")