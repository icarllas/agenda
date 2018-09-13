from django.db import models
from django.utils import timezone
from libgravatar import Gravatar

class Event (models.Model):
    priorities_list = (

        ('0', 'sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito Urgente'),
        ('4', 'Ultra mega hiper Urgente')

    )


    date = models.DateField()
    event = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=priorities_list)

    def __str__(self):
        return self.event

class Commit (models.Model):
    """Comentário efetuado em um determinado evento"""

    author = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.CharField(max_length=80)
    commented = models.DateField(default=timezone.now)
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name="comment_event")
    """Retornar a partir do endereço de email, um avatar configurado"""
    def avatar(self):
        g = Gravatar(self.email)
        return g.get_image(default='idention')

    def __str__(self):
        return "{} comentou em {:%c}".format(self.author, self.commented)
