def main():
    #DEFININDO VARIVAEIS QUE IREI UTILIZAR.
    usuario = ""
    opcao = 0
    idade = 0
    email = ""
    cidade = ""
    profissao = ""
    while True:
               #Condiçao de loop.
               print("MENU\t\t")
               print("1.Cadastrar usuario.")
               print("2.Ver usuario cadatrado.")
               print("3.Sair do sistema.\n")
               opcao = int(input("Escolha uma das opções:"))
            
               if opcao == 1:
                       usuario = input("Qual o seu nome: " )
                       idade = int(input("Qual a sua idade? "))
                       email = input("Qual o seu e-mail?")
                       cidade = input("Em qual cidade mora? ")
                       profissao = input("Qual a sua profissao? ")
                       print("Usuario cadastrado com sucesso. ")
               elif opcao == 2:
                       if usuario == "" and idade == 0 and email == "" and cidade == "" and profissao == "":
                               #Condiçao para verificar se esta tudo corretamente preenchido.
                               print("Nenhum usuario cadastrado anteriormente.")
                       else:
                               print("Usuario cadastrado anteriormente:\nNome: ", usuario,"\nIdade: ", idade, "\nE-mail: ", email, "\nCidade: ", cidade, "\nProfissão: ", profissao, "\n\t============\t")
               elif opcao == 3:
                       print("========Encerrando o sistema.========")
                       break
               else:
                       print("Opção inválida. Tente novamente.")
                       
#Condiçao obrigatoria para o codigo def main() funcionar:
if __name__ == "__main__":
        
        main()