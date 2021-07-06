from __future__ import unicode_literals
import smtplib
from django import conf
from django.core.exceptions import MiddlewareNotUsed
from django.db import models
from datetime import datetime
from django.utils.html import format_html
from smtplib import SMTPAuthenticationError
from django.core.mail import send_mail
from django.conf import settings

import sys

class Contato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=25)
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def send_mail(self):
        message_admin = """
        Nova Mensagem - Jhon Leno
        Nome: {0}
        Email: {1}
        Telefone: {2}
        Assunto: {3}

        Mensagem: {4}

        """

        message_admin = message_admin.format(self.nome, self.email, self.telefone,
         self.assunto, self.mensagem )

        message = """
        
        Ola {0}
        Obrigado por entrar em contato
        Espero que tenha gostado do projeto.
        
        """

        message = message.format(self.nome)

        try:
            send_mail(
                'Novo Contato',
                message_admin,
                'Jhon Leno FC <jhongamesoficial@gmail.com>',
                settings.ADMINS,
                fail_silently=False
        )
            send_mail (
                'Auto Mensagem',
                message,
                'Jhon Leno FC <jhongamesoficial@gmail.com>',
                [self.email],
                fail_silently=False
            )
            self.email_sent = True
            self.save()

        except smtplib.SMTPAuthenticationError:
            pass
def send_confirmation_email(sender, instance, created, **wkargs):
    if not instance.email_sent:
        instance.send_mail()

models.signals.post_save.connect(
    send_confirmation_email, sender=Contato, dispatch_uid='contato.Record')