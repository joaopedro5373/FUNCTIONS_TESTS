def verificar_senha(senha:str)->bool:
    if(type(senha) is not str):
        raise TypeError("A senha precisa ser uma string.")
    elif(len(senha) == 0 or senha.isspace()):
        raise ValueError("A senha não pode ser vazia.")
    if(len(senha) < 8):
        return False
    temMaiuscula = any(c.isupper() for c in senha)
    temMinuscula = any(c.islower() for c in senha)
    temNumero = any(c.isdigit() for c in senha)
    tem_especial = any(not c.isalnum() for c in senha)
    if(temMaiuscula and temMinuscula and temNumero and tem_especial):
        return True
    else: return False