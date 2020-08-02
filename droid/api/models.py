from django.db import models
from django.contrib.auth import get_user_model

"""
A model is the single, definitive source of information about your data.
It contains the essential fields and behaviors of the data you’re storing.
Generally, each model maps to a single database table.
"""


class Anunciante(models.Model):
    """
    This class contains the representation of the fields in the Anunciante table.
    """
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'Anunciante'
        verbose_name_plural = 'Anunciantes'
        ordering = ['-created']

    def __str__(self):
        """A string representation of the model."""
        return self.name


class DemandaDePecas(models.Model):

    """
    This class contains the representation of the fields in the DemandaDePecas table.
    """

    STATUS_FINALIZACAO_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('FINALIZADA', 'Finalizada'),
    ]
    descricao_peca = models.CharField(max_length=150)
    endereco_entrega = models.CharField(max_length=150)
    anunciante = models.ForeignKey('Anunciante', on_delete=models.CASCADE)
    status_finalizacao = models.CharField(max_length=20, choices=STATUS_FINALIZACAO_CHOICES)

    created = models.DateTimeField('Created in', auto_now_add=True)
    modified = models.DateTimeField('Modified in', auto_now=True)

    class Meta:
        verbose_name = 'DemandaDePeca'
        verbose_name_plural = 'DemandaDePecas'
        ordering = ['-created']

    def __str__(self):
        """A string representation of the model."""
        return self.descricao_peca
