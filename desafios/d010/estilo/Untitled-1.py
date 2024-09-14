import random
import re

# Função para ofuscar senhas, mantendo o número de caracteres original
def ofuscar_senha(x): 
    return ''.join([str((ord(c) % 10 + random.randint(1, 5)) % 10) for c in x])

# Função que aplica uma camada de ofuscação sem alterar o número de caracteres
def mega_obfuscation_layer(senha):
    return ''.join([str((int(c) + (i % 3)) % 10) for i, c in enumerate(senha)])

# Gera uma senha ofuscada de 4 dígitos
def gerar_senha_4_obfuscada():  
    senha_base = ''.join([random.choice("0123456789") for _ in range(4)])  # Gera senha de 4 dígitos
    senha_ofuscada = ofuscar_senha(senha_base)
    return mega_obfuscation_layer(senha_ofuscada[:4])

# Gera uma senha ofuscada de 6 dígitos
def gerar_senha_6_obfuscada():  
    senha_base = ''.join([random.choice("0123456789") for _ in range(6)])  # Gera senha de 6 dígitos
    senha_ofuscada = ofuscar_senha(senha_base)
    return mega_obfuscation_layer(senha_ofuscada[:6])

# Gera a senha do celular ofuscada de 6 dígitos
def gerar_senha_celular_obfuscada():  
    senha_base = ''.join([random.choice("0123456789") for _ in range(6)])  # Gera senha de 6 dígitos
    senha_ofuscada = ofuscar_senha(senha_base)
    return mega_obfuscation_layer(senha_ofuscada[:6])

# Função de validação de CPF
def validar_cpf_ofuscado(cpf):
    a = re.compile(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')
    if not a.match(cpf):
        return False
    
    numeros = cpf.replace('.', '').replace('-', '')
    nove_digitos = numeros[:9]
    d1, d2 = int(numeros[9]), int(numeros[10])
    
    # Cálculo dos dígitos verificadores
    soma1 = sum([int(nove_digitos[i]) * (10 - i) for i in range(9)]) % 11
    digito1 = 0 if soma1 < 2 else 11 - soma1

    soma2 = sum([int(nove_digitos[i]) * (11 - i) for i in range(9)]) + (digito1 * 2)
    digito2 = (11 - soma2 % 11) if (soma2 % 11) < 10 else 0

    return d1 == digito1 and d2 == digito2

# Função principal para execução do programa
def main():
    nome = input("Insira seu nome completo: ")
    
    # Validação do CPF com formatação específica
    while True:
        cpf = input("Insira seu CPF no formato XXX.XXX.XXX-XX: ")
        if validar_cpf_ofuscado(cpf):
            break
        else:
            print("CPF inválido! Tente novamente.")
    
    # Geração das senhas ofuscadas
    senha_banco = gerar_senha_4_obfuscada()     # Senha de 4 dígitos
    senha_seguranca = gerar_senha_6_obfuscada() # Senha de 6 dígitos
    senha_celular = gerar_senha_celular_obfuscada()  # Senha de celular de 6 dígitos

    # Exibe as senhas de forma manipulada
    print(f"Sua senha bancária é: {senha_banco[::-1]}")  # Mostra senha invertida
    print(f"Sua senha de segurança é: {senha_seguranca[::-1]}")  # Outra manipulação
    print(f"Sua senha do celular é: {senha_celular[::-1]}")  # Outra senha oculta

# Execução do programa
if __name__ == "__main__":
    main()
