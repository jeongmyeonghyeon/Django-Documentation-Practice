"""
Post 모델
    author = User의 연결
    title
    content
    created_date
        DateTimeField 사용
    modified_date
        DateTimeField사용

Comment 모델
    post = Post의 연결
    author = User의 연결
    content
    crated_date
    modified_date

User 모델
    name
    created_date
    modified_date
"""
from django.db import models
from utils.models.mixins import TimeStampedMixin


class Post(TimeStampedMixin):
    author = models.ForeignKey('User')
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 이 Post에 좋아요를 누른 사람들
    like_users = models.ManyToManyField(
        'User',
        related_name='like_posts',
        through='PostLike',
        # through_fields=('post', 'user')
    )


class Comment(TimeStampedMixin):
    post = models.ForeignKey('Post')
    author = models.ForeignKey('User')
    content = models.TextField()


class User(TimeStampedMixin):
    name = models.CharField(max_length=30)


class PostLike(models.Model):
    post = models.ForeignKey('Post')
    user = models.ForeignKey('User')
    created_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'introduction_to_models_post_like_users'
