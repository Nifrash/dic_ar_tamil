from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Word

class WordResource(resources.ModelResource):
    class Meta:
        model = Word
        fields = (
            'id',
            'tamil_word',
            'arabic_word',
            'category',
            'example_sentence',
            'created_at',
        )
        import_id_fields = ('tamil_word',)

@admin.register(Word)
class WordAdmin(ImportExportModelAdmin):
    resource_class = WordResource

    list_display = (
        'tamil_word',
        'arabic_word',
        'category',
        'is_approved',
        'created_by',
        'created_at',
    )

    list_filter = (
        'category',
        'is_approved',
        'created_at',
    )

    search_fields = (
        'tamil_word',
        'arabic_word',
        'category',
    )

    list_editable = ('is_approved',)
    ordering = ('tamil_word',)