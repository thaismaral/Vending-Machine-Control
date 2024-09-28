estoque = 20
caixaDineiro2 = 45
caixaDineiro5 = 45
caixaDineiro10 = 1
caixaMoeda25 = 45
caixaMoeda50 = 45
caixaMoeda01 = 45
while True:
   print("Para Administrador: 1")
   print("Para Consumidor: 2")
   acessoInicial = int(input("Digite o seu acesso: "))
   if acessoInicial ==1:
       print("=" * 40)
       print("Bem vindo a Administrador")
       senha = int(input("Digite a senha:"))
       if senha != 2005:
           print("Senha incorreta")
           print("=" * 40)
           continue
       if senha == 2005:
           print("Para adicionar dinheiro: 1")
           print("Para averiguar dinheiro: 2")
           print("Para adicionar bebidas: 3")
           print("Para averiguar estoque de bebidas: 4")
           print("=" * 40)
           acessoADM = int(input("Digite o seu acesso: "))
           if acessoADM == 1:
               print("1 - Para adicionar moedas de R$0,25")
               print("2 - Para adicionar moedas de R$0,50")
               print("3 - Para adicionar moedas de R$1,00")
               print("4 - Para adicionar cédulas de R$2,00")
               print("5 - Para adicionar cédulas de R$5,00")
               print("6 - Para adicionar cédulas de R$10,00")
               admDinheiro = int(input("Digite o seu acesso: "))
               if admDinheiro == 1:
                   print("Quantas moedas serão adicionadas?")
                   caixaMoeda25 += int(input())
                   continue
               if admDinheiro == 2:
                   print("Quantas moedas serão adicionadas?")
                   caixaMoeda50 += int(input())
                   continue
               if admDinheiro == 3:
                   print("Quantas moedas serão adicionadas?")
                   caixaMoeda01 += int(input())
                   continue
               if admDinheiro == 4:
                   print("Quantas moedas serão adicionadas?")
                   caixaDineiro2 += int(input())
                   continue
               if admDinheiro == 5:
                   print("Quantas moedas serão adicionadas?")
                   caixaDineiro5 += int(input())
                   continue
               if admDinheiro == 6:
                   print("Quantas moedas serão adicionadas?")
                   caixaDineiro10 += int(input())
                   continue
           if acessoADM == 2:
               print("Há",caixaMoeda25,",moedas de R$0,25")
               print("Há",caixaMoeda50,"moedas de R$0,50")
               print("Há",caixaMoeda01,"moedas de R$1,00")
               print("Há",caixaDineiro2,"notas de R$2,00")
               print("Há",caixaDineiro5,"notas de R$5,00")
               print("Há",caixaDineiro10,"notas de R$10,00")
               totalDinheiro = (caixaMoeda25 + caixaMoeda50 + caixaMoeda01 + caixaDineiro2 + caixaDineiro5 + caixaDineiro10)
               print("Há",totalDinheiro,"no caixa")
           if acessoADM == 3:
               print("Quantas bebidas serão adicionadas?")
               estoque += int(input())
               print("=" * 40)
           if acessoADM == 4:
               print("Há",estoque,"bebidas disponível na máquina")
           else:
               print("=" * 40)
   elif acessoInicial == 2:
       if estoque > 0:
           print("=" * 60)
           print("Bem-vindo a Maquina de ")
           print("Valor da bebida é: R$5,00")
           print("Máximo de bebidas é 2")
           qtdBebida = int(input("Digite a quantidade de sucos desejados: "))
           print("=" * 60)
           if qtdBebida > 2:
               print ("Máximo de bebidas é 2")
               print("=" * 60)
               continue
           if qtdBebida <= 2:
               if qtdBebida > estoque:
                   print("Não há bebidas disponíveis no momento, tente pedir uma quantidade menor ou fale com nossoadministrador")
                   print("=" * 60)
               else:
                   estoque -= qtdBebida
                   print("Para pagamento em cédula: 1")
                   print("Para pagamento em moeda: 2")
                   print("Para pagamento em cédula e moeda: 3")
                   formaPagamento = int(input("Digite seu pagamento:"))
                   print("=" * 60)
                   if formaPagamento == 1:
                       total = 0
                       while total < 5:
                           cedulas2 = int(input("Digite quantas cédulas serão inseridas de R$2,00: "))
                           if cedulas2 >=1:
                               total += (2 * cedulas2)
                               if total > 5 * qtdBebida:
                                   troco = total - (5 * qtdBebida)
                                   caixaDineiro2 += cedulas2
                                   print("*" * 60)
                                   print("Seu troco é de R$", troco)
                                   print("Obrigado pela compra!")
                                   print("Retire sua bebida")
                                   print("*" * 60)
                                   estoque -= qtdBebida
                               if total == 5 * qtdBebida:
                                   caixaDineiro2 += cedulas2
                                   print("*" * 60)
                                   print("Obrigado pela compra!")
                                   print("Retire sua bebida")
                                   print("*" * 60)
                                   estoque -= qtdBebida
                               if total < 5 * qtdBebida:
                                   cedulas5 = int(input("Digite quantas cédulas serão inseridas de R$5,00: "))
                                   if cedulas5 >= 1:
                                       total += (5 * cedulas5)
                                       if total == 5 * qtdBebida:
                                           caixaDineiro5 += cedulas5
                                           print("Obrigado pela compra!")
                                           print("Retire sua bebida")
                                           print("=" * 60)
                                           estoque -= qtdBebida
                                       elif total > 5 * qtdBebida:
                                           troco = total - (5 * qtdBebida)
                                           caixaDineiro5 += cedulas5
                                           print("Seu troco é de R$", troco)
                                           print("Obrigado pela compra!")
                                           print("Retire sua bebida")
                                           print("=" * 60)
                                           estoque -= qtdBebida
                                       else:
                                           print("Você não possui dinheiro suficiente para realizar a compra.")
                                           estoque += qtdBebida
                                           print("=" * 60)
                                           break
                                   else:
                                       cedulas10 = int(input("Digite quantas cédulas serão inseridas de R$10,00: "))
                                       if cedulas10 < 1:
                                           print("Você não possui dinheirobsuficiente para realizar a compra.")
                                           estoque += qtdBebida
                                           print("=" * 60)
                                       else:
                                           total += (10 * cedulas10)
                                           troco = total - (5 * qtdBebida)
                                           caixaDineiro10 += cedulas10
                                           print("Seu troco é de R$", troco)
                                           print("Obrigado pela compra!")
                                           print("Retire sua bebida")
                                           print("=" * 60)
                                           estoque -= qtdBebida
                           else:
                               cedulas5 = int(input("Digite quantas cédulas serão inseridas de R$5,00: "))
                               if cedulas5 >= 1:
                                   total += (5 * cedulas5)
                                   if total == 5 * qtdBebida:
                                       caixaDineiro5 += cedulas5
                                       print("Obrigado pela compra!")
                                       print("Retire sua bebida")
                                       print("=" * 60)
                                       estoque -= qtdBebida
                                   elif total > 5 * qtdBebida:
                                       troco = total - (5 * qtdBebida)
                                       caixaDineiro5 += cedulas5
                                       print("Seu troco é de R$", troco)
                                       print("Obrigado pela compra!")
                                       print("Retire sua bebida")
                                       print("=" * 60)
                                       estoque -= qtdBebida
                                   else:
                                       print("Você não possui dinheiro suficiente para realizar a compra.")
                                       estoque += qtdBebida
                                       print("=" * 60)
                               else:
                                   cedulas10 = int(input("Digite quantas cédulas serão inseridas de R$10,00: "))
                                   if cedulas10 < 1:
                                       print("Você não possui dinheiro suficiente para realizar a compra.")
                                       estoque += qtdBebida
                                       print("=" * 60)
                                   else:
                                       total += (10 * cedulas10)
                                       troco = total - (5 * qtdBebida)
                                       caixaDineiro10 += cedulas10
                                       print("Seu troco é de R$", troco)
                                       print("Obrigado pela compra!")
                                       print("Retire sua bebida")
                                       print("=" * 60)
                                       estoque -= qtdBebida
                   if formaPagamento == 2:
                       total = 0
                       moeda25 = int(input("Digite quantas moedas serão inseridas de R$0,25: "))
                       total += (moeda25 * 0.25)
                       if total == 5 * qtdBebida:
                            print("Obrigado pela compra!")
                            print("Retire sua bebida")
                            print("=" * 60)
                            estoque -= qtdBebida
                       else:
                            moeda50 = int(input("Digite quantas moedas serão inseridas de R$0,50: "))
                            total += (moeda50 * 0.50)
                            if total == 5 * qtdBebida:
                                print("Obrigado pela compra!")
                                print("Retire sua bebida")
                                print("=" * 60)
                                estoque -= qtdBebida
                            else:
                                moeda01 = int(input("Digite quantas moedas serão inseridas de R$1,00: "))
                                total += (moeda01 * 1)
                                if total == 5 * qtdBebida:
                                    print("Obrigado pela compra!")
                                    print("Retire sua bebida")
                                    print("=" * 60)
                                    estoque -= qtdBebida
                                elif total > 5 * qtdBebida:
                                    troco = total - (5 * qtdBebida)
                                    print("Seu troco é de R$", troco)
                                    print("Obrigado pela compra!")
                                    print("Retire sua bebida")
                                    print("=" * 60)
                                    estoque -= qtdBebida
                                else:
                                    print("Você não possui dinheiro suficiente para realizar a compra.")
                                    estoque += qtdBebida
                                    print("=" * 60)
                   if formaPagamento == 3:
                        total = 0
                        nota2 = int(input("Digite quantas cédulas serão inseridas de R$2,00: "))
                        nota5 = int(input("Digite quantas cédulas serão inseridas de R$5,00: "))
                        nota10 = int(input("Digite quantas cédulas serão inseridas de R$10,00: "))
                        moeda25 = int(input("Digite quantas moedas serão inseridas de R$0,25: "))
                        moeda50 = int(input("Digite quantas moedas serão inseridas de R$0,50: "))
                        moeda01 = int(input("Digite quantas moedas serão inseridas de R$1,00: "))
                        total += ((moeda01 * 1) + (moeda50 * 0.50) + (moeda25 * 0.25) + (nota10 * 10) + (nota5 * 5) + (nota2* 2))
                        if total == 5 * qtdBebida:
                           print("Obrigado pela compra!")
                           print("Retire sua bebida")
                           print("=" * 60)
                           estoque -= qtdBebida
                        elif total > 5 * qtdBebida:
                           troco = total - (5 * qtdBebida)
                           print("Seu troco é de R$", troco)
                           print("Obrigado pela compra!")
                           print("Retire sua bebida")
                           print("=" * 60)
                           estoque -= qtdBebida
                        else:
                           print("Você não possui dinheiro suficiente para realizar a compra.")
       else:
        estoque += qtdBebida
        print("Não há bebidas disponíveis no momento, tente pedir uma quantidade menor ou fale com nosso administrador")
        print("*" * 60)
   else:
       print("Digite seu acesso")