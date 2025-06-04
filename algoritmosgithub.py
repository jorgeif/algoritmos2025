import os


tamanho = 0

while(tamanho < 5):
    email = input("Insira seu usuário de E-Mail: ")
    tamanho = len(email)
    if(tamanho <= 5):
        print("Informe E-mail com mais de 5 caracteres")
print("Escolha a opção correspondente ao seu provedor de E-mails a seguir.")
opcoes = int(input("1. ifpr.edu.br\n2.gmail.com\n3.hotmail.com\n4.Outra opcao: "))
if(opcoes == 1):
    email = email + "@ifpr.edu.br"
elif(opcoes == 2):
    email = email + "@gmail.com"
elif(opcoes == 3):
    email = email + "@hotmail.com"
else: 

    servico = input("Digite o sufixo de seu usuário de email: ")
    while(not(".com" in servico)):
        servico = input("Digite o sufixo de seu usuário de email")

    email = email + "@" + servico

print(f"Seu E-Mail é {email}")

correto = input("Seu E-Mail está correto? (S) Sim ou (N) Não? ")
if(correto != "S" and correto != "s"):
    exit 

commit = input("Qual a mensagem do seu commit? ")
lencommit = len(commit)
while(lencommit < 10):
    commit = input("Mensagem pequena demais, qual a mensagem do seu commit? ")

print("---------------------------------\nIniciando comandos Git")


#configurar o email
c = f"git config user.email \"{email}\"  "
os.system(c)

#identificar novidades e incluir no commit
c = f"git add *"
os.system(c) 

#registrar o commit
c = f"git commit -m \"{commit}\"  "
os.system(c)

#enviar para os servidores do github
c = "git push"
print(c)