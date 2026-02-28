import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")


def enviar_requisicao(dados):
    socket.send_string(json.dumps(dados, ensure_ascii=False))
    resposta = json.loads(socket.recv_string())
    return resposta


def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("Descrição não pode ser vazia.")
        return
    resposta = enviar_requisicao({"acao": "adicionar", "descricao": descricao})
    print(resposta["mensagem"])


def remover_tarefa():
    try:
        tarefa_id = int(input("ID da tarefa a remover: ").strip())
    except ValueError:
        print("ID inválido.")
        return
    resposta = enviar_requisicao({"acao": "remover", "id": tarefa_id})
    print(resposta["mensagem"])


def listar_tarefas():
    resposta = enviar_requisicao({"acao": "listar"})
    if resposta.get("tarefas"):
        print("-" * 40)
        for t in resposta["tarefas"]:
            print(f"  [{t['id']}] {t['descricao']}")
        print("-" * 40)
    else:
        print(resposta["mensagem"])


def menu():
    print("\n===== Gerenciador de Tarefas =====")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas")
    print("0. Sair")
    return input("Escolha uma opção: ").strip()


print("Cliente conectado ao servidor de tarefas.")

while True:
    opcao = menu()
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        listar_tarefas()
    elif opcao == "0":
        print("Encerrando cliente.")
        break
    else:
        print("Opção inválida.")
