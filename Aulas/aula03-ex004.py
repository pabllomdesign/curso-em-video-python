#Solicite ao usuário o salário por hora e o número de horas trabalhadas no mês, e calcule o salário mensal.
salario_hora = float(input('Informe seu salario/hora de trabalho: '))
horas_trabalhadas = float(input('Informe as horas trabalhadas: '))

print(f'Salario hora: {salario_hora} | Quantidade de horas trabalhadas: {horas_trabalhadas} \nSeu salario mês será de: R${salario_hora*(horas_trabalhadas)}')