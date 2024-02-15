class carro:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

chevrolet = carro('Chevrolet', 'hylux')
print(chevrolet.marca)
print(chevrolet.modelo)
print(chevrolet.cor)

#---erro de atribuição, chama um valor que não existe