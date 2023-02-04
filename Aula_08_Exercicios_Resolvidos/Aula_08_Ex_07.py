# Definindo as Funções
def calculadora (a,b,op):
   """Calcula as operações +, -, x e /"""
   
   if op == "+":
       return a + b
   elif op == "-":
       return a - b
   elif op == "/":
       if b != 0:
           return a/b
       else:
           return "Divisão por zero"
   elif op == "x":
       return a*b
   else:
        return "Operador inválido."
        

# Programa Principal

a = float(input("Digite o primeiro valor: "))
op = input("Digite o operador [+, -, x ou /]: ")
b = float(input("Digite o segundo valor:"))

print(calculadora(a,b,op))