from django import forms
from potros.models import Noticias

class CustomImageWidget(forms.ClearableFileInput):
    template_name = 'custom_widgets/custom_image_widget.html'

    def __init__(self, attrs=None):
        attrs = attrs or {}
        super().__init__(attrs)

class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'cuerpo1', 'cuerpo2', 'imagen']

    def __init__(self, *args, **kwargs):
        super(NoticiasForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['imagen'].widget = CustomImageWidget()
