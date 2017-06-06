from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    # current_club프로퍼티에 현재 속하는 Club리턴
    # current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴


class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo'
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        pass
        # squad 메서드에 현직 선수들만 리턴
        # 인수로 년도(2017, 2015...등)를 받아
        # 해당 년도의 현직 선수들을 리턴,
        # 주어지지 않으면 현재를 기준으로 함


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True)
