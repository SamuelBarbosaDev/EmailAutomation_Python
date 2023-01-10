import yagmail
from decouple import (
    AutoConfig
)


class EmailAutomation():
    """
    send emails.
    """

    def __init__(self, my_email, my_password):
        self.MY_EMAIL = my_email
        self.MY_PASSWORD = my_password

    def send_email(
        self,
        addressee,
        title=None,
        email_content=None,
        attachments=None
    ):

        user = yagmail.SMTP(
            user=self.MY_EMAIL,
            password=self.MY_PASSWORD
        )

        user.send(
            to=addressee,
            subject=title,
            contents=email_content,
            attachments=attachments,
        )

        print("Email sent!!!")


if __name__ == "__main__":
    config = AutoConfig(r'../EmailAutomation_Python/core/.env')

    my_email = config('MY_EMAIL')
    my_password = config('MY_PASSWORD')
    my_other_email = config('MY_OTHER_EMAIL')
    email_title = "What is Python? Executive Summary."

    email_content = """
    <p>What is Python? Executive Summary
    Python is an interpreted, object-oriented,
    high-level programming language with dynamic semantics.
    Its high-level built in data structures, combined with dynamic
    typing and dynamic binding, make it very attractive for Rapid
    Application Development, as well as for use as a scripting or glue
    language to connect existing components together. Python's simple,
    easy to learn syntax emphasizes readability and therefore reduces
    the cost of program maintenance. Python supports modules and packages,
    which encourages program modularity and code reuse. The Python interprete
    and the extensive standard library are available in source or binary form
    without charge for all major platforms, and can be freely distributed.</p>

    <p>ass:. samuelbarbosa_dev</p>
    """

    attach_file = None

    email = EmailAutomation(
        my_email=my_email,
        my_password=my_password,
    )

    email.send_email(
        addressee=my_other_email,
        title=email_title,
        email_content=email_content,
        attachments=attach_file,
    )
