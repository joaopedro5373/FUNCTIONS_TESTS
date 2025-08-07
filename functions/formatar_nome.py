def formatar_nome(nome:str, sobrenome:str)->str:
    if(type(nome) == str and type(sobrenome) == str):
        if(len(nome) == 0 or nome.isspace() or len(sobrenome) == 0 or sobrenome.isspace()):
            raise ValueError("Os campos nome e sobrenome não podem estar vazios.")
    else: raise TypeError("Nome e sobrenome devem ser do tipo string.")
    nomeCompleto = f"{nome} {sobrenome}"
    return nomeCompleto
