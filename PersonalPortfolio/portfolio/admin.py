from django.contrib import admin
from .models import WorkExperience, Skill, Project, Education, About, Contact

admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(About)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'submitted_at')
    search_fields = ('name', 'email')