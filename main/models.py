from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=90)
    twitter_url = models.URLField()
    facebook_url = models.URLField()
    instagram_url = models.URLField()

    def __str__(self):
        return self.name


class Record(models.Model):
    name = models.CharField(max_length=90)
    overall_wins = models.IntegerField()
    overall_loses = models.IntegerField()
    conference_wins = models.IntegerField()
    conference_loses = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    year_start = models.IntegerField()
    year_end = models.IntegerField()

    def __str__(self):
        return self.name


class SeasonSchedule(models.Model):
    season = models.CharField(max_length=90)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    year_start = models.IntegerField()
    year_end = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.team.name, self.season)


class ScheduleItem(models.Model):
    HOME_AWAY_CHOICES = (
        ('HOME', 'HOME'),
        ('AWAY', 'AWAY'),
        ('TBD', 'TBD'),
    )

    name = models.CharField(max_length=90)
    date = models.DateTimeField()
    opponent = models.CharField(max_length=90)
    location = models.TextField()
    home_away = models.CharField(choices=HOME_AWAY_CHOICES, max_length=6)
    win = models.BooleanField()
    loss = models.BooleanField()
    score = models.CharField(max_length=14)
    season = models.ForeignKey(SeasonSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


##### ROSTER ######

class Roster(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def get_players(self):
        return self.player_set.all()


class Player(models.Model):

    YEAR_CHOICES = (
        ('FR.', 'FR.'),
        ('SO.', 'SO.'),
        ('JR.', 'JR.'),
        ('SR.', 'SR.'),
    )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    roster = models.ManyToManyField(Roster)
    jersey_number = models.IntegerField()
    position = models.CharField(max_length=20)
    height = models.CharField(max_length=14)
    weight = models.IntegerField()
    year_class = models.CharField(choices=YEAR_CHOICES, max_length=5)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


### STAFF ####

class StaffMember(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    title = models.CharField(max_length=90)
    email = models.EmailField()
    phone = models.CharField(max_length=18)
    team = models.ManyToManyField(Team)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)
