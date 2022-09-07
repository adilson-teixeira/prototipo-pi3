from django.contrib import admin

from .models import Square, Specie, Tree, Family

@admin.register(Square)
class SquereAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "is_display", 
        "description", 
        "address", 
        "image1",
        "image2",
        "image3",
        "altimg1", 
        "altimg2", 
        "altimg3", 
        "slug", 
        "created", 
        "modified",
        ]
    list_editable = [
        "description",
        "is_display",
        "address",
        "image1",
        "image2",
        "image3",
        "altimg1",      
        "altimg2",
        "altimg3",
        ]


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created", "modified"]

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created", "modified"]




@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "image1",
        "image2",
        "image3",
        "specie",
        "family",
        "square",
        "is_display",
        "altimg1",
        "altimg2",
        "altimg3",
        "source",
        "quantidade",
        "slug",
        "created",
        "modified",
    ]
    list_filter = ["is_display", "created", "modified"]
    list_editable = [
        "is_display",
        "source",
        "quantidade", 
        "image1",
        "altimg1",
        "image2",
        "altimg2",
        "image3",
        "altimg3",
    ]