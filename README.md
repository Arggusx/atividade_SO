### Simulador de Sistema Operacional (Python)

Este projeto é uma simulação prática dos principais conceitos de Sistemas Operacionais, como gerenciamento de processos, filas, troca de contexto e algoritmos de escalonamento.
O objetivo é representar o comportamento de um pequeno kernel capaz de criar, controlar e executar processos de forma semelhante a um SO real.

## Funcionalidades Principais

1. Criar e gerenciar processos com informações como:

- PID (identificador único)

- Nome

- Tempo de CPU restante

- Memória ocupada

- Prioridade (1 = mais alta)

- Estado: Pronto, Executando, Bloqueado, ou Finalizado

2. Executar os principais algoritmos de escalonamento de CPU:

- FIFO (First In First Out)

- SJF (Shortest Job First)

- RR (Round Robin) → Quantum = 2 ciclos

- PRIO (Por prioridade)

3. Gerenciar o estado dos processos com comandos de bloqueio, desbloqueio e encerramento.

## Estrutura do Código

**Representa cada processo do sistema, contendo todos os seus atributos e estado.**

1. Classe Processo

class Processo:
    def __init__(self, pid, nome):
        self.pid = pid
        self.nome = nome
        self.cpu = random.randint(1, 10)
        self.mem = random.randint(50, 200)
        self.prio = random.randint(1, 5)
        self.estado = "Pronto"


- cpu → Tempo restante de execução do processo.

- mem → Quantidade de memória consumida (gerada aleatoriamente).

- prio → Define a prioridade (1 é a mais alta).

- estado → Indica em qual fila o processo se encontra.

2. Classe SistemaOperacional

 **Gerencia todos os processos criados e implementa os algoritmos de escalonamento.**

## Principais métodos:

- create(nome):	Cria um novo processo com atributos aleatórios
- listar():	Lista todos os processos e seus estados
- block(pid):	Bloqueia um processo
- unblock(pid):	Desbloqueia um processo
- kill(pid):	Finaliza um processo
- run(algoritmo):	Executa o algoritmo de escalonamento escolhido
- executar_fila(): 	Simula execução para FIFO, SJF e PRIO
- round_robin():	Executa a simulação do algoritmo Round Robin

3. Loop principal: (main())

**Implementa o terminal interativo do simulador, permitindo que o usuário digite comandos como se estivesse em um shell de sistema operacional.**

def main():
    so = SistemaOperacional()
    print("Mini Sistema Operacional iniciado. Digite 'help' para comandos.")

    while True:
        comando = input("SO> ").strip().split()
        ...


1.  Comandos disponíveis:

- create <nome>:	Cria um novo processo
- list:	Lista os processos existentes
- run <algoritmo>:	Executa o escalonador (fifo, sjf, rr, prio)
- block <PID>:	Bloqueia um processo
- unblock <PID>:	Desbloqueia um processo
- kill <PID>:	Encerra um processo
- exit:	Encerra o sistema

2. Algoritmos de Escalonamento

- FIFO (First In, First Out): **Executa os processos na ordem em que foram criados, sem interrupções até o término.**

- SJF (Shortest Job First): **Escolhe primeiro o processo com menor tempo de CPU restante.**

- PRIO (Por Prioridade): **Executa primeiro os processos com maior prioridade (menor número).**

- RR (Round Robin): **Cada processo recebe 2 unidades de CPU (quantum) por ciclo. Se não terminar nesse tempo, ele retorna ao fim da fila.**

3. Simulação de Execução

## Cada ciclo consome 1 unidade de CPU, representada visualmente com uma pausa (time.sleep(0.3)).
Quando o tempo de CPU chega a zero, o processo muda seu estado para Finalizado.

1. Exemplo:

SO> create chrome
SO> create vscode
SO> create spotify
SO> list

PID  | Nome       | CPU | MEM  | PRIO | Estado
-----------------------------------------------
1    | chrome     | 6   | 150  | 3    | Pronto
2    | vscode     | 4   | 120  | 1    | Pronto
3    | spotify    | 8   | 90   | 5    | Pronto

SO> run prio
Executando escalonamento: PRIO...

-> Executando vscode (PID 2) - CPU restante: 4
✓ Processo 2 finalizado!

-> Executando chrome (PID 1) - CPU restante: 6
✓ Processo 1 finalizado!

-> Executando spotify (PID 3) - CPU restante: 8
✓ Processo 3 finalizado!