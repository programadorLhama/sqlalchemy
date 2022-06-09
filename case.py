class AlgumaCoisa:
    def __enter__(self):
        print('Estou Entrando')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Estou Saindo')


with AlgumaCoisa() as ola:
    print('Estou no Meio')
