import yagmail
from decouple import (
    AutoConfig
)


class EmailAutomation():
    """
    Enviar emails.
    """
    def __init__(self, my_email, my_password):
        self.MY_EMAIL = my_email
        self.MY_senha = my_password

    def enviar_email(
        self,
        addressee,
        title=None,
        email_content=None,
        attachments=None
    ):
        email = self.MY_EMAIL
        senha = self.MY_senha

        usuario = yagmail.SMTP(user=email, password=senha)

        usuario.send(
            to=addressee,
            subject=title,
            contents=email_content,
            attachments=attachments,
        )

        print("Email enviado!!!")


if __name__ == "__main__":
    config = AutoConfig(r'../.env')

    my_email = config('MY_EMAIL')
    my_password = config('MY_PASSWORD')
    my_other_email = config('MY_OTHER_EMAIL')
    email_title = "A Referência da Linguagem Python."

    email_content = """
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

    attach_file = "seu_anexo.pdf"

    email = EmailAutomation(
        my_email=my_email,
        my_password=my_password,
    )

    email.enviar_email(
        addressee=my_other_email,
        title=email_title,
        email_content=email_content,
        attachments=attach_file,
    )
