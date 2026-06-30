from django.db import models

class FightLocation(models.Model):
    name_loc = models.CharField(max_length=100)

    def __str__(self):
        return self.name_loc


class Hero(models.Model):
    name = models.CharField(max_length=100, verbose_name='какого персонажа выбираете?')
    weapon = models.CharField(max_length=100, verbose_name='каким оружием атакуете?')
    fight_location = models.ManyToManyField(FightLocation, null=True, blank=True)

    def __str__(self):
        return f'{self.name}:{', '.join(i.name_loc for i in self.fight_location.all())}'

class Person(models.Model):
    select_hero = models.OneToOneField(Hero, on_delete=models.CASCADE, null=True, blank=True)
    name_pers = models.CharField(max_length=100, default='Иван')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.select_hero}-{self.name_pers}'


class ReviewHero(models.Model):
    select_hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='review')
    MARKS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    marks = models.CharField(max_length=100, choices=MARKS, default='4')
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.select_hero} - {self.marks}'

    


