from django.contrib import admin
from .models import Programms, HTMLField
from tinymce.widgets import TinyMCE  # Bu qatorni qo'shing


class ProgrammAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'download_link')

    formfield_overrides = {
        HTMLField: {'widget': TinyMCE(
            attrs={'cols': 100, 'rows': 30},
            mce_attrs={
                'plugins': 'advlist,autolink,lists,link,image,charmap,print,preview,anchor,'
                           'searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,code,help,wordcount',
                'toolbar': 'undo redo | formatselect | bold italic backcolor | alignleft aligncenter '
                           'alignright alignjustify | bullist numlist outdent indent | removeformat | help',
            }
        )},
    }


admin.site.register(Programms, ProgrammAdmin)
