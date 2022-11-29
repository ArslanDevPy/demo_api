import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class Email(threading.Thread):
    def __init__(self, title, template_name, email, _dict):
        self.template_name = template_name
        self.title = title
        self.email = email
        self._dict = _dict
        threading.Thread.__init__(self)

    def run(self):
        message = render_to_string(self.template_name, self._dict)
        email = EmailMessage(self.title, message, to=[self.email])
        email.content_subtype = 'html'
        email.send()
