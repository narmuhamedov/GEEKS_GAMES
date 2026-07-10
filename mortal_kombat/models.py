from django.db import models


class NewsMk(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите название новости')
    description = models.TextField(verbose_name='укажите новость')
    emodji = models.CharField(max_length=1, null=True, verbose_name='укажите эмодзи')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.created_at}'
    
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'






class PersonMk(models.Model):
    photo = models.ImageField(upload_to='persons_mk/', 
                              verbose_name='загрузите фото пресонажа')
    name = models.CharField(max_length=15, 
                            verbose_name='укажите имя персонажа')
    age = models.PositiveIntegerField(verbose_name='укажите возраст',
                                      default=30)
    KINDOM = (
        ('земное царство', 'земное царство'),
        ('внешний мир', 'внешний мир'),
        ('неизвестно', 'неизвестно')
    )
    kindom = models.CharField(max_length=100, choices=KINDOM, default='земное царство',
                              verbose_name='укажите царство обитания персонажа')
    
    description = models.TextField(verbose_name='укажите описание персонажа', blank=True)

    video_fight = models.URLField(verbose_name='укажите ссылку на бой')

    created_at = models.DateField(auto_now_add=True)

    views = models.PositiveIntegerField(default=0, null=True)

    class Meta:
        verbose_name = 'персонажа'
        verbose_name_plural = 'персонажи'

    def __str__(self):
        return self.name




