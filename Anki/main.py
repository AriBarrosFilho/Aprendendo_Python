import re

def formatar_texto(texto):
    # Quebra o texto em linhas
    linhas = texto.strip().split("\n")
    
    nova_lista = []
    contador = 1

    for linha in linhas:
        # Usa expressão regular para identificar frases no formato correto ou incorreto
        match = re.match(r'(\d+)?\)?(.*?)(\?|:)', linha.strip())
        
        if match:
            # Captura a frase e a resposta
            frase = match.group(2).strip()
            pontuacao = match.group(3)
            
            # Isola a resposta (se houver) da pergunta
            partes = linha.split(pontuacao, 1)
            if len(partes) > 1:
                resposta = partes[1].strip()
            else:
                resposta = ""
                
            # Corrige a capitalização da frase
            frase_corrigida = frase.capitalize()
            
            # Cria a nova linha com o marcador, pergunta corrigida e resposta
            nova_linha = f"{contador:03d}) {frase_corrigida}{pontuacao}\t{resposta}"
            nova_lista.append(nova_linha)
            
            contador += 1
    
    # Retorna o texto formatado
    return "\n".join(nova_lista)