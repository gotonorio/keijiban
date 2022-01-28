from django import forms

from bbs.models import File


CSS_CHOICES = (
    ('cover', '等サイズ'),
    ('contain', '全体表示'),
)


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
            'img': forms.FileInput(attrs={
                'class': "input",
            }),
            'rank': forms.TextInput(attrs={
                'class': "input",
            }),
            'created_at': forms.DateTimeInput(attrs={
                'class': 'input',
            }),
            'alive': forms.NullBooleanSelect(attrs={
                'class': "select-css",
            }),
        }


class SwitchCSSForm(forms.Form):
    """ 掲示板のcssを切り替えるためのform """
    css = forms.ChoiceField(
        label='CSS',
        widget=forms.Select(attrs={'class': 'select-css'}),
        choices=CSS_CHOICES,
        required=True,
    )
