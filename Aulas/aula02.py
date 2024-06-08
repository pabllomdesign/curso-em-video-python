#Crie um script que leia algo pelo teclado e msotre na tela o seu tipo primitivo e todas as informações possíveis.
InfoTeclado = input('Digite algo: ')
print(f'O tipo primitido de "{InfoTeclado}" é', type(InfoTeclado))
print(f'"{InfoTeclado}" é numerico?', InfoTeclado.isnumeric())
print(f'"{InfoTeclado}" é Alfanumerico?', InfoTeclado.isalnum())
print(f'"{InfoTeclado}" contém somente espaços?', InfoTeclado.isspace())
print(f'"{InfoTeclado}" esta em maiúscula?', InfoTeclado.isupper())
print(f'"{InfoTeclado}" esta em minuscula?', InfoTeclado.islower())
