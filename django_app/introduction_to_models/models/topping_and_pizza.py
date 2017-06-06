from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        # 자신이 가지고있는 토핑목록을 뒤에 출력
        # result_string = ''
        # for topping in self.toppings.all():
        #     result_string += topping.name
        #     result_string += ', '
        #
        # result_string = result_string[:-2]
        # return '{} {}'.format(
        #     self.name,
        #     result_string
        # )
        return '{} ({})'.format(self.name, ', '.join([t.name for t in self.toppings.all()]))

    class Meta:
        ordering = ('name',)
