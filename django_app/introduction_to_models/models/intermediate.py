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
        # return self.club_set.get(tradeinfo__date_leaved__isnull=True)
        return self.current_club.club

    # current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴

    # @property
    # def current_tradeinfo(self):
    #     tradeinfo_self = TradeInfo.objects.get(
    #         player=self.id,
    #         date_leaved__isnull=True
    #     )
    #     return '선수명: {}, 소속클럽: {}, 입단날짜: {}'.format(
    #         tradeinfo_self.player,
    #         tradeinfo_self.club,
    #         tradeinfo_self.date_joined
    #     )

    @property
    def current_tradeinfo(self):
        return self.tradeinfo_set.get(date_leaved__isnull=True)


class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo',
        through_fields=('club', 'player',),
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        # 2015년에 현직이었던 -> 2015년에 하루라도 현직이었던 선수
        # ex) 2015년에 현직으로 존재했던 선수일 경우
        # 떠난 날짜가 2015. 1. 1 보다는 커야한다
        # 들어온 날짜는 2016. 1. 1 보다는 작아야 한다 / 2015. 12. 31보다는 작거나 같아야 한다
        if year:
            return self.players.filter(
                Q(tradeinfo__date_joined__lt=datetime(year + 1, 1, 1)) &
                (
                    Q(tradeinfo__date_leaved__gt=datetime(year, 1, 1)) |
                    Q(tradeinfo__date_leaved__isnull=True)
                )
            )
        else:
            return self.players.filter(tradeinfo__date_leaved__isnull=True)
            # squad 메서드에 현직 선수들만 리턴
            # 인수로 년도(2017, 2015...등)를 받아
            # 해당 년도의 현직 선수들을 리턴,
            # 주어지지 않으면 현재를 기준으로 함


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True)
    recommender = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        related_name='tradeinfo_set_by_recommender',
        null=True,
        blank=True
    )
    prev_club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
        blank=True
    )

    @property
    def is_current(self):
        return self.date_leaved is None

    def __str__(self):
        # 선수이름, 구단명(시작일자~종료일자)
        # date_leaved가 None일 경우, '현직'을 출력하도록 함

        # 내가 쓴거
        # if self.date_leaved is None:
        #     self.date_leaved = '현직'

        return '{}, {}({}~{})'.format(
            self.player.name,
            self.club.name,
            self.date_joined,
            self.date_leaved or '현직',
            # self.date_leaved if self.date_leaved else '현직'
        )
