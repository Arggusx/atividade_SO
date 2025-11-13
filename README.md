# Simulador de Sistema Operacional (Python)

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

---

2. Executar os principais algoritmos de escalonamento de CPU:

    - FIFO (First In First Out)

    - SJF (Shortest Job First)

    - RR (Round Robin) → Quantum = 2 ciclos

    - PRIO (Por prioridade)

---

3. Gerenciar o estado dos processos com comandos de bloqueio, desbloqueio e encerramento.

## Estrutura do Código

1. Classe Processo

<img width="337" height="162" alt="Captura de tela 2025-11-13 090609" src="https://github.com/user-attachments/assets/3df56702-c7d6-4f2a-9b2a-a5450859fc82" />

- cpu → Tempo restante de execução do processo.
- mem → Quantidade de memória consumida (gerada aleatoriamente).
- prio → Define a prioridade (1 é a mais alta).
- estado → Indica em qual fila o processo se encontra.

---

2. Classe SistemaOperacional

 **Gerencia todos os processos criados e implementa os algoritmos de escalonamento.**

Principais métodos:

- create(nome):	Cria um novo processo com atributos aleatórios
- listar():	Lista todos os processos e seus estados
- block(pid):	Bloqueia um processo
- unblock(pid):	Desbloqueia um processo
- kill(pid):	Finaliza um processo
- run(algoritmo):	Executa o algoritmo de escalonamento escolhido
- executar_fila(): 	Simula execução para FIFO, SJF e PRIO
- round_robin():	Executa a simulação do algoritmo Round Robin

---

3. Loop principal: (main())

**Implementa o terminal interativo do simulador, permitindo que o usuário digite comandos como se estivesse em um shell de sistema operacional.**

<img width="1480" height="1850" alt="def_main" src="https://github.com/user-attachments/assets/20ba2af4-bc4d-451d-9e27-4b0a3d6b8768" />


1.  Comandos disponíveis:

    - create <nome>:	Cria um novo processo
    - list:	Lista os processos existentes
    - run <algoritmo>:	Executa o escalonador (fifo, sjf, rr, prio)
    - block <PID>:	Bloqueia um processo
    - unblock <PID>:	Desbloqueia um processo
    - kill <PID>:	Encerra um processo
    - exit:	Encerra o sistema

---

2. Algoritmos de Escalonamento

    - FIFO (First In, First Out): **Executa os processos na ordem em que foram criados, sem interrupções até o término.**

    - SJF (Shortest Job First): **Escolhe primeiro o processo com menor tempo de CPU restante.**

    - PRIO (Por Prioridade): **Executa primeiro os processos com maior prioridade (menor número).**

    - RR (Round Robin): **Cada processo recebe 2 unidades de CPU (quantum) por ciclo. Se não terminar nesse tempo, ele retorna ao fim da fila.**

---

3. Simulação de Execução

**Cada ciclo consome 1 unidade de CPU, representada visualmente com uma pausa (time.sleep(0.3)).
Quando o tempo de CPU chega a zero, o processo muda seu estado para Finalizado.**

Exemplo:

<img width="451" height="648" alt="Captura de tela 2025-11-13 092727" src="https://github.com/user-attachments/assets/101ae988-7e90-4385-88a6-9ca12a520004" />
