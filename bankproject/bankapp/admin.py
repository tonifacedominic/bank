from django.contrib import admin

from bankapp.models import District,Details,Banks,Account

# Register your models here.


class DetailsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'dob','age','gender','pnumber','mailid','address','district','branch')
    list_editable = ('name',)
    ordering = ('id',)
admin.site.register(Details, DetailsAdmin)


class BanksAdmin(admin.ModelAdmin):
    list_display = ("id",'district','name',)
    list_editable = ('name', )
    ordering = ('district',)
admin.site.register(Banks, BanksAdmin)

admin.site.register(Account)

admin.site.register(District)

