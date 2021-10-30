from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    post_date = models.DateTimeField(auto_now_add=True)
    blogger = models.ForeignKey('Blogger', on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-post_date', ]


class Blogger(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    post = models.CharField(max_length=100)
    biography = models.CharField(max_length=100)
    COUNTRY_CHOICES = (
        (None, 'Выберите страну'),
        ('a', 'Беларусь'),
        ('b', 'Канада'),
        ('c', 'Польша'),
        ('d', 'США'),
    )
    country = models.CharField(max_length=1, choices=COUNTRY_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', ]


class Comment(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date_added', ]
