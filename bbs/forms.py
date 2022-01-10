from django import forms

from bbs.models import File


class FileForm(forms.ModelForm):
    """ Fileモデルのフォーム
    ModelForm限定の方法としてclass Metaでwidgetを設定する。class以外も変更できる。
    https://narito.ninja/blog/detail/52/
    """
    class Meta:
        model = File
        fields = ("title", "summary", "img", "rank", "created_at", "alive")
        # field毎に異なるclassを設定する場合には、この方法を取る。
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "input",
            }),
            'summary': forms.TextInput(attrs={
                'class': "input",
            }),
            'img': forms.ClearableFileInput(attrs={
                # 'class': "file",
                'class': "input",
            }),
            'rank': forms.TextInput(attrs={
                'class': "input",
            }),
            'created_at': forms.DateInput(attrs={
                'class': 'input',
            }),
            'alive': forms.NullBooleanSelect(attrs={
                'class': "select-css",
            }),
        }
