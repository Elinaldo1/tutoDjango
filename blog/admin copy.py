from django.contrib import admin
from django.db import models


class MyModel(models.Model):
    NewView = models.CharField(max_length=255)

    def __str__(self):
        return self.NewView

# class MyModelAdmin(admin.ModelAdmin):
    # queryset = Location.objects.all()


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ['codigo', 'frente']

# class MyViewInline(admin.TabularInline):
#     model = MyModel
#     readonly_fields = ['codigo', 'frente']


# class MyModelAdmin(admin.ModelAdmin):
#     inlines = [MyViewInline]


admin.site.register(MyModel, MyModelAdmin)