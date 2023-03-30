def decorator_imprimir(function):
    def mensagem(*args, **kwargs):
        print('Inicio do calculo')
        function(*args, **kwargs)    
    return mensagem
@decorator_imprimir 
def juros_simples(capital, taxa, tempo):
    resultado = capital * (taxa / 100) * tempo
    print (resultado)
capital = int (input('Digite capital: '))
taxa = int (input('Digite taxa: '))
tempo = int (input('Digite tempo: '))
juros_simples(capital, taxa, tempo)
    