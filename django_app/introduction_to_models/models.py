from django.db import models


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PERSON_TYPES = (
        ('student', '학생'),
        ('teacher', '선생'),
    )
    # recursive relationships (재귀 관계) 실습
    # 자신과 다대일 관계가 있는 객체 (ForeignKey)
    person_type = models.CharField(
        '유형',
        max_length=10,
        choices=PERSON_TYPES,
        default=PERSON_TYPES[0][0]
    )
    # teacher속성 지정 (ForeignKey, 'self'를 이용해 자기 자신을 가리킴 null=True허용)
    teacher = models.ForeignKey(
        'self',
        null=True,
        on_delete=models.CASCADE,
        blank=True
    )
    name = models.CharField(
        '이름',
        max_length=60
    )
    shirt_size = models.CharField(
        '셔츠사이즈',
        max_length=1,
        choices=SHIRT_SIZES,
        help_text='셔츠사이즈 입니다.'
    )

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
