# Classe Node que será utilizada para construir a fila
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Classe Queue para implementar a fila
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    # Método para enfileirar um elemento na fila
    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    # Método para desenfileirar um elemento da fila
    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.value

    # Método para verificar se a fila está vazia
    def is_empty(self):
        return self.front is None

    # Método para visualizar o primeiro elemento da fila
    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    # Método para exibir todos os elementos da fila
    def display_queue(self):
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# Instanciando a fila
q = Queue()

# Passo 2: Enfileirar elementos
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)  # Elemento adicionado
q.enqueue(5)  # Elemento adicionado
q.enqueue(6)  # Elemento adicionado
print("Estado atual da fila após novos enqueues:")
q.display_queue()

# Passo 3: Desenfileirar elementos
q.dequeue()
q.dequeue()
print("\nEstado da fila após desenfileirar dois elementos:")
q.display_queue()

# Passo 4: Visualizar o primeiro elemento
primeiro_elemento = q.peek()
print("\nPrimeiro elemento na fila após as remoções:", primeiro_elemento)

# Passo 5: Verificar se a fila está vazia
if q.is_empty():
    print("Fila está vazia")
else:
    print("Fila não está vazia")
