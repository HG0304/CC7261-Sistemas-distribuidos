# Lab 4 - Pub/Sub com topicos (ZeroMQ)

Resolucao do exercicio de `cc7261/pub-sub/lab.md`.

## O que foi implementado

- `publisher_hora.py` (P1): publica a hora atual no topico `hora`
- `publisher_dado.py` (P2): publica um inteiro aleatorio entre 1 e 6 no topico `dado`
- `subscriber_hora.py`: recebe apenas mensagens do topico `hora`
- `subscriber_dado.py`: recebe apenas mensagens do topico `dado`
- `subscriber_todos.py`: recebe publicacoes de ambos os publishers
- `proxy.py`: broker XPUB/XSUB para rotear publishers e subscribers

## Como executar

```bash
docker compose up --build
```

## Como verificar

- Logs de `subscriber_hora`: apenas mensagens iniciadas com `hora`
- Logs de `subscriber_dado`: apenas mensagens iniciadas com `dado`
- Logs de `subscriber_todos`: mensagens `hora` e `dado`

Para ver logs de um servico especifico:

```bash
docker compose logs -f subscriber_hora
```
