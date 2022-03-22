




#Como? enviar um e-mail com python.
import yagmail
from DadosDoUsuario import *

def enviar_email(destinatario, titulo=None, mensagem_do_email=None, anexo=None):
    email = meu_email
    senha = minha_senha

    usuario = yagmail.SMTP(user=email, password=senha)

    usuario.send(
        to = destinatario,
        subject = titulo,
        contents = mensagem_do_email,
        attachments = anexo,
    )

    print("Email enviado!!!")

if __name__ == "__main__":
    conteudo_do_email = """
    <p>Este manual de referência descreve a 
    sintaxe e a “semântica central” da linguagem. 
    É conciso, mas tenta ser exato e completo. 
    A semântica dos tipos de objetos embutidos 
    não essenciais e das funções e módulos embutidos 
    é descrita em A Biblioteca Padrão do Python. Para 
    uma introdução informal à linguagem, consulte O 
    tutorial de Python. Para programadores em C ou C++, 
    existem dois manuais adicionais: Estendendo e 
    Incorporando o Interpretador Python descreve a imagem 
    de alto nível de como escrever um módulo de extensão 
    Python, e o Manual de referência da API Python/C descreve 
    as interfaces disponíveis para programadores C/C++ em detalhes.</p>

    <p>ass:. samuelbarbosa_dev</p>
    """

    titulo_do_email = "A Referência da Linguagem Python."
    arquivo_anexo = "seu_anexo.pdf"

    enviar_email(
        meu_outro_email,
        titulo_do_email,
        conteudo_do_email,
        arquivo_anexo,
    )
