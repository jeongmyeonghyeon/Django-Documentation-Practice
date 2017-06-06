import datetime
from django.db import models
from django.db.models import Q


class Player(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    # current_club프로퍼티에 현재 속하는 Club리턴
    @property
    def current_club(self):
        return self.club_set.get(tradeinfo__date_leaved__isnull=True)

    # current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴
    @property
    def current_tradeinfo(self):
        tradeinfo_self = TradeInfo.objects.get(
            player=self.id,
            date_leaved__isnull=True
        )
        return '선수명: {}, 소속클럽: {}, 입단날짜: {}'.format(
            tradeinfo_self.player,
            tradeinfo_self.club,
            tradeinfo_self.date_joined
        )


class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo'
    )
    prev_club = models.ManyToManyField(
        Player,
        through='TradeInfo',
        through_fields=('Player', 'Club'),
        related_name='_related',
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        pass
        # if year is None:
        #     year = datetime.datetime.now().year
        #     return self.tradeinfo_set.get(date_leaved__isnull=True)
        #     # squad 메서드에 현직 선수들만 리턴
        #     # 인수로 년도(2017, 2015...등)를 받아
        #     # 해당 년도의 현직 선수들을 리턴,
        #     # 주어지지 않으면 현재를 기준으로 함
        # else:
        #     return self.tradeinfo_set.get(Q(date_joined__lte=year) | Q(date_leaved__isnull=True))


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True)
    # recommender = models.ForeignKey(
    #     Player,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )
    # prev_club = models.ForeignKey(
    #     Club,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )
    #
    # @property
    # def is_current(self):
    #     return self.date_leaved is None
