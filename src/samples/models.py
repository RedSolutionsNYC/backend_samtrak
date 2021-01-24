from django.db import models

class Sample(models.Model):
    serialNo = models.CharField(max_length=25)
    cylinderChoices = [('S', '2 x 2'), ('M', '4 x 10'), ('L', '6 x 12')]
    cylinderSize = models.CharField(max_length=1, choices=cylinderChoices)
    #inspector
    #company
    #location

    def __str__(self):
        return self.serialNo, self.cylinderSize