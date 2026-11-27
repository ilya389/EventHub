from django.contrib import admin

from .models import Event, Registration, ContactMessage

# Register your models here.

class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 0
    readonly_fields = ('created_at',)

admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_published')
    list_filter = ('is_published', 'date')
    search_fields = ('title', 'location')
    inlines = [RegistrationInline]

admin.site.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'status', 'created_at')
    list_filter = ('status', 'event')
    search_fields = ('name', 'email')

admin.site.register(ContactMessage)