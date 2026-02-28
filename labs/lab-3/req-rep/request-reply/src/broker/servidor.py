import zmq
import json

tarefas = []
proximo_id = 1


def processar_requisicao(dados):
    global proximo_id

    acao = dados.get("acao")

    if acao == "adicionar":
        tarefa = {
            "id": proximo_id,
            "descricao": dados.get("descricao", ""),
        }
        tarefas.append(tarefa)
        proximo_id += 1
        return {"status": "ok", "mensagem": f"Tarefa '{tarefa['descricao']}' adicionada com ID {tarefa['id']}."}

    elif acao == "remover":
        tarefa_id = dados.get("id")
        for i, t in enumerate(tarefas):
            if t["id"] == tarefa_id:
                removida = tarefas.pop(i)
                return {"status": "ok", "mensagem": f"Tarefa '{removida['descricao']}' (ID {removida['id']}) removida."}
        return {"status": "erro", "mensagem": f"Tarefa com ID {tarefa_id} não encontrada."}

    elif acao == "listar":
        if not tarefas:
            return {"status": "ok", "mensagem": "Nenhuma tarefa cadastrada.", "tarefas": []}
        return {"status": "ok", "mensagem": f"{len(tarefas)} tarefa(s) encontrada(s).", "tarefas": tarefas}

    else:
        return {"status": "erro", "mensagem": f"Ação '{acao}' desconhecida."}


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://broker:5556")

print("Servidor de tarefas iniciado.", flush=True)

while True:
    message = socket.recv_string()
    print(f"Requisição recebida: {message}", flush=True)

    try:
        dados = json.loads(message)
        resposta = processar_requisicao(dados)
    except json.JSONDecodeError:
        resposta = {"status": "erro", "mensagem": "Requisição inválida (JSON malformado)."}

    socket.send_string(json.dumps(resposta, ensure_ascii=False))

