import threading
 
# classe principal com duas funções
class principal (threading.Thread):
    def __init__(self, threadID, nome, cont):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.nome = nome
        self.cont = cont
 
    def run(self):
        print (" Iniciando a %s com %d processos" % (self.nome,self.cont))
        processo(self.nome, self.cont)
 
def processo(nome, cont):
    while cont:
        print (" A %s realiza o processo %d" % (nome, cont))
        cont = cont - 1
 
# Instanciando a classe principal
thread1 = principal(1, "THREAD 1", 20)
thread2 = principal(2, "THREAD 2", 15)
 
# iniciando as threads
thread1.start()
thread2.start()
 
pipes = []
pipes.append(thread1)
pipes.append(thread2)
 
for i in pipes:
    i.join()
 
input('\nTecle ENTER para sair...')

