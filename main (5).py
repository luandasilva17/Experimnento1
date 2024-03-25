from suds.client import Client

# URL do WSDL do serviço da calculadora
url = 'http://www.dneonline.com/calculator.asmx?WSDL'

# Cria um cliente para o serviço da calculadora
client = Client(url)

# Função para somar dois números usando o serviço da calculadora
def add(x, y):
    return client.service.Add(x, y)

# Função para subtrair dois números usando o serviço da calculadora
def subtract(x, y):
    return client.service.Subtract(x, y)

# Função para multiplicar dois números usando o serviço da calculadora
def multiply(x, y):
    return client.service.Multiply(x, y)

# Função para dividir dois números usando o serviço da calculadora
def divide(x, y):
    return client.service.Divide(x, y)

# Exemplo de uso das funções
num1 = 10
num2 = 5

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
