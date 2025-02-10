class HashTable:
    """
    Implementação de uma Tabela Hash simples usando encadeamento separado.
    """
    def __init__(self, size=1000):
        """
        Inicializa a tabela hash com um tamanho padrão de 1000.
        A tabela é representada como uma lista de listas (para lidar com colisões).
        """
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """
        Função de hash simples: usa o operador de módulo para distribuir chaves.
        Retorna o índice na tabela hash.
        """
        return key % self.size
    
    def insert(self, key):
        """
        Insere um número na tabela hash.
        Somente insere se o número ainda não estiver presente no seu índice.
        """
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)
    
    def contains(self, key):
        """
        Verifica se um número já está presente na tabela hash.
        Retorna True se estiver, False caso contrário.
        """
        index = self._hash(key)
        return key in self.table[index]
    
    def get_numbers(self):
        """
        Retorna todos os números armazenados na tabela hash em uma lista.
        """
        numbers = [] 
        for bucket in self.table:
            numbers.extend(bucket) 
        return numbers