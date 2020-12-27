from django.db import models

# Create your models here.
class HjemmeSideInfoModel(models.Model):
    """
    Model for user to insert text to webpage
    """

    overskrift_1 = models.CharField(max_length=200,null=True,blank=True)
    tekst_1 = models.TextField(max_length=2000,null=True,blank=True)
    overskrift_2 = models.CharField(max_length=200,null=True,blank=True)
    tekst_2 = models.TextField(max_length=2000,null=True,blank=True)
    link_til_aktiv_gruppe = models.URLField(max_length=300)
    pris = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return "Endre tekst og pris"
