from django.contrib import admin
from models import Token, Quest, Decision

class TokenAdmin(admin.ModelAdmin):
    pass
admin.site.register(Token, TokenAdmin)

class QuestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Quest, QuestAdmin)

class DecisionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Decision, DecisionAdmin)