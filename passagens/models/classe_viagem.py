from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseViagem(models.TextChoices):
        ECONOMICA = 'ECON', _('Econômica')
        EXECUTIVA = 'EXEC', _('Executiva')
        PRIMEIRA_CLASSE = 'PRIC', _('Primeira Classe')