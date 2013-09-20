# -*- coding: UTF-8 -*-

from django.db import models

import os
from binascii import hexlify

def _createId():
    return hexlify(os.urandom(16))

#quests 
class Quest(models.Model):
    name = models.CharField(max_length=32, verbose_name='Короткое имя квеста')
    text = models.TextField(verbose_name='Текст квеста')
    image = models.CharField(max_length=50, verbose_name='Картинка', default='/static/images/quest/dumb.png')

    def __unicode__(self):
        return self.name


#decisions
class Decision(models.Model):
    BONUS = True
    PENALTY = False
    REWARD_CHOICES = (
        (BONUS, 'Бонус'),
        (PENALTY, "Штраф"),
    ) 
    name = models.CharField(max_length=30, verbose_name='Имя решения')
    dec_hash = models.CharField(max_length=32, default=_createId, unique=True, verbose_name='ID решения')
    text = models.TextField(verbose_name='Текст решения')
    text_after = models.TextField(verbose_name='Текст последствий')
    quest = models.ForeignKey(Quest, verbose_name='Ссылка на квест')
    code = models.TextField(max_length=30, verbose_name='Код к бонусу')
    reward_type = models.BooleanField(max_length=10, verbose_name='Бонус/штраф', choices=REWARD_CHOICES, default=BONUS)
    reward = models.CharField(max_length=32,verbose_name='Размер бонуса/штрафа')
    image = models.CharField(max_length=50, verbose_name='Картинка', default='/static/images/quest/dumb.png')

    def __unicode__(self):
        return self.quest.name + ' - ' + self.name


#tokens
class Token(models.Model):
    tok_hash = models.CharField(max_length=32, default=_createId, unique=True, verbose_name='ID токена') 
    linked_quest = models.ForeignKey(Quest, verbose_name='Ссылка на квест')
    demo = models.BooleanField(default=False, verbose_name='Демо')
    visible = models.BooleanField(default=True, verbose_name='Видимый')
    team = models.CharField(max_length=32, default="Нет команды")
    decision = models.ForeignKey(Decision, null=True, blank=True, verbose_name='Выбранное решение')

    def __unicode__(self):
        demo = ""
        if self.demo:
            demo = "[DEMO] "
        return demo + self.team + ": " + self.linked_quest.name
