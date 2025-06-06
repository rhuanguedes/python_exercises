# Dicionário para armazenar os veículos estacionados, com a placa como chave.
veiculos_estacionados = {}

# Dicionário para contar a quantidade de veículos por tipo.
contador_tipo = {"motocicleta": 0, "carro de passeio": 0, "camionete": 0}

# Variáveis para controlar os veículos isentos e o total arrecadado.
veiculos_isentos = 0
total_arrecadado = 0

# Loop principal do programa, que fica em execução até o usuário decidir encerrar
while(True):

    # Exibe o menu principal para o usuário
    print("=== Unicesumar Parking ===")
    print("=-" * 30)
    print("[1] Registrar entrada\n[2] Registrar saída\n[3] Exibir relatório\n[4] Fechar o programa")
    print("=-" * 30)
    
    # Solicita ao usuário a opção escolhida (1, 2, 3 ou 4)
    opcao = int(input("Selecione uma opção: "))

    # Opção 1: Registrar a entrada de um veículo
    if opcao == 1:
        print('Você selecionou a opção "Registrar entrada".')
        print("=-" * 30)

        # Solicita e formata a placa do veículo
        placa = input("Placa do veículo: ").upper()
        print("=-" * 30)

        # Apresenta as opções de tipo de veículo
        print("Selecione o tipo de veículo:")
        print("[1] Motocicleta\n[2] Carro de passeio\n[3] Camionete")
        print("=-" * 30)
        
        # Solicita ao usuário a opção de tipo de veículo
        tipo_opcao = int(input("Escolha uma opção: "))
        print("=-" * 30)

        # Mapeia a opção selecionada para o tipo de veículo correspondente
        if tipo_opcao == 1:
            tipo = "motocicleta"
        elif tipo_opcao == 2:
            tipo = "carro de passeio"
        elif tipo_opcao == 3:
            tipo = "camionete"
        else:
            # Caso a opção não seja válida, informa o erro e volta ao início do loop
            print("Opção inválida! Tipo de veículo não registrado.")
            continue

        # Solicita a hora e o minuto de entrada
        hora_entrada = input("Hora(s) de entrada: ")
        print("=-" * 30)
        minuto_entrada = input("Minuto(s) de entrada: ")
        print("=-" * 30)

        # Armazena os dados do veículo no dicionário veiculos_estacionados
        veiculos_estacionados[placa] = {
            "tipo": tipo,
            "hora_entrada": int(hora_entrada),
            "minuto_entrada": int(minuto_entrada)
        }

        # Incrementa o contador do tipo de veículo registrado
        contador_tipo[tipo] += 1

        # Informa que a entrada foi registrada com sucesso
        print("Entrada registrada com sucesso!")
        print("=-" * 30)

    # Opção 2: Registrar a saída de um veículo
    elif opcao == 2:
        print('Você selecionou a opção "Registrar saída".')
        print("=-" * 30)

        # Solicita a placa do veículo
        placa = input("Placa do veículo: ").upper()

        # Verifica se o veículo está registrado no dicionário
        if placa in veiculos_estacionados:
            # Solicita hora e minuto de saída
            hora_saida = int(input("Hora(s) de saída: "))
            minuto_saida = int(input("Minuto(s) de saída: "))

            # Obtém os dados de entrada do veículo
            dados = veiculos_estacionados[placa]

            # Calcula o tempo total de estacionamento (em minutos)
            tempo_entrada = dados["hora_entrada"] * 60 + dados["minuto_entrada"]
            tempo_saida = hora_saida * 60 + minuto_saida
            tempo_total = tempo_saida - tempo_entrada

            # Verifica o valor a ser pago com base no tempo total de estacionamento
            if tempo_total <= 15:
                print(f"Veículo {dados['tipo']} com placa {placa} está isento de pagamento.")
                veiculos_isentos += 1
                valor_pagar = 0
            elif tempo_total <= 60:
                valor_pagar = 1.50
                print(f"Veículo {dados['tipo']} com placa {placa} deve pagar: R${valor_pagar:.2f}")
            else:
                horas_extras = (tempo_total - 60) // 60
                if (tempo_total - 60) % 60 > 0:
                    horas_extras += 1
                valor_pagar = 1.50 + horas_extras * 1.00
                print(f"Veículo {dados['tipo']} com placa {placa} deve pagar: R${valor_pagar:.2f}")

            # Atualiza o total arrecadado
            total_arrecadado += valor_pagar

            # Decrementa o contador do tipo de veículo que saiu
            contador_tipo[dados['tipo']] -= 1

            # Remove o veículo do dicionário, já que ele saiu
            del veiculos_estacionados[placa]

        else:
            # Caso a placa não seja encontrada
            print("Veículo não encontrado!")

    # Opção 3: Exibir o relatório
    elif opcao == 3:
        print("=== Relatório ===")
        print("=-" * 30)
        # Exibe o número de veículos estacionados no momento
        print(f"Veículos estacionados no momento: {len(veiculos_estacionados)}")
        # Exibe o total arrecadado até o momento
        print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
        # Exibe o total de veículos isentos de pagamento
        print(f"Total de veículos isentos: {veiculos_isentos}")
        # Exibe a quantidade de veículos por tipo
        print("Quantidade de veículos por tipo:")
        for tipo_veiculo, quantidade in contador_tipo.items():
            print(f"{tipo_veiculo.capitalize()}: {quantidade}")

    # Opção 4: Fechar o programa
    elif opcao == 4:
        print("Encerrando programa...")
        break

    # Caso o usuário escolha uma opção inválida
    else:
        print("Selecione uma opção válida!")


