import random
import time

class Processo:
    def __init__(self, pid, nome):
        self.pid = pid
        self.nome = nome
        self.cpu = random.randint(1, 10)  
        self.mem = random.randint(50, 200)
        self.prio = random.randint(1, 5)  
        self.estado = "Pronto"

    def __str__(self):
        return f"{self.pid:<4} | {self.nome:<10} | {self.cpu:<3} | {self.mem:<4} | {self.prio:<4} | {self.estado:<10}"

class SistemaOperacional:
    def __init__(self):
        self.processos = []
        self.pid_counter = 1
        self.quantum = 2

    def create(self, nome):
        processo = Processo(self.pid_counter, nome)
        self.processos.append(processo)
        self.pid_counter += 1
        print(f"Processo '{nome}' criado com PID {processo.pid}")

    def listar(self):
        print("PID  | Nome       | CPU | MEM  | PRIO | Estado")
        print("-----------------------------------------------")
        for p in self.processos:
            print(p)

    def get_proc(self, pid):
        for p in self.processos:
            if p.pid == pid:
                return p
        return None

    def block(self, pid):
        p = self.get_proc(pid)
        if p and p.estado not in ["Finalizado", "Bloqueado"]:
            p.estado = "Bloqueado"
            print(f"Processo {pid} bloqueado.")
        else:
            print("PID inválido ou já bloqueado/finalizado.")

    def unblock(self, pid):
        p = self.get_proc(pid)
        if p and p.estado == "Bloqueado":
            p.estado = "Pronto"
            print(f"Processo {pid} desbloqueado.")
        else:
            print("PID inválido ou processo não está bloqueado.")

    def kill(self, pid):
        p = self.get_proc(pid)
        if p:
            p.estado = "Finalizado"
            p.cpu = 0
            print(f"Processo {pid} encerrado.")
        else:
            print("PID inválido.")

    def run(self, algoritmo):
        prontos = [p for p in self.processos if p.estado == "Pronto"]

        if not prontos:
            print("Nenhum processo pronto para execução.")
            return

        print(f"\nExecutando escalonamento: {algoritmo.upper()}...\n")

        if algoritmo == "fifo":
            fila = sorted(prontos, key=lambda x: x.pid)
            self.executar_fila(fila, fifo=True)

        elif algoritmo == "sjf":
            fila = sorted(prontos, key=lambda x: x.cpu)
            self.executar_fila(fila)

        elif algoritmo == "prio":
            fila = sorted(prontos, key=lambda x: x.prio)
            self.executar_fila(fila)

        elif algoritmo == "rr":
            self.round_robin()

        else:
            print("Algoritmo inválido!")

    def executar_fila(self, fila, fifo=False):
        for p in fila:
            if p.estado != "Pronto":
                continue
            p.estado = "Executando"
            while p.cpu > 0:
                print(f"-> Executando {p.nome} (PID {p.pid}) - CPU restante: {p.cpu}")
                p.cpu -= 1
                time.sleep(0.3)
            p.estado = "Finalizado"
            print(f"✓ Processo {p.pid} finalizado!\n")

    def round_robin(self):
        fila = [p for p in self.processos if p.estado == "Pronto"]

        while any(p.cpu > 0 and p.estado == "Pronto" for p in fila):
            for p in fila:
                if p.estado != "Pronto":
                    continue
                p.estado = "Executando"
                for _ in range(self.quantum):
                    if p.cpu > 0:
                        print(f"-> Executando {p.nome} (PID {p.pid}) - CPU restante: {p.cpu}")
                        p.cpu -= 1
                        time.sleep(0.3)
                    else:
                        break
                if p.cpu == 0:
                    p.estado = "Finalizado"
                    print(f"✓ Processo {p.pid} finalizado!\n")
                else:
                    p.estado = "Pronto"

def main():
    so = SistemaOperacional()
    print("Mini Sistema Operacional iniciado. Digite 'help' para comandos.")

    while True:
        comando = input("SO> ").strip().split()

        if not comando:
            continue

        cmd = comando[0]
        args = comando[1:]

        if cmd == "help":
            print("""
Comandos disponíveis:
  create <nome>     → Cria um novo processo
  list              → Lista processos
  run <algoritmo>   → Executa escalonador (fifo, sjf, rr, prio)
  block <PID>       → Bloqueia processo
  unblock <PID>     → Desbloqueia processo
  kill <PID>        → Encerra processo
  exit              → Sai do sistema
            """)
        elif cmd == "create" and args:
            so.create(args[0])
        elif cmd == "list":
            so.listar()
        elif cmd == "run" and args:
            so.run(args[0])
        elif cmd == "block" and args:
            so.block(int(args[0]))
        elif cmd == "unblock" and args:
            so.unblock(int(args[0]))
        elif cmd == "kill" and args:
            so.kill(int(args[0]))
        elif cmd == "exit":
            print("Encerrando o sistema...")
            break
        else:
            print("Comando inválido. Digite 'help' para ajuda.")


if __name__ == "__main__":
    main()
