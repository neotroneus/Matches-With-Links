from django.db import models

class Match(models.Model):
    match_description = models.CharField(max_length=200)
    match_details = models.CharField(max_length=1000)
    match_logo = models.FileField()

    def __str__(self):
        return self.match_description


class Links(models.Model):
    match = models.ForeignKey(Match, on_delete= models.CASCADE)
    details = models.CharField(default='', max_length=1000)
    link_logo = models.FileField(default='')
    the_link = models.CharField(default='', max_length=1000)


    def __str__(self):
        return self.details