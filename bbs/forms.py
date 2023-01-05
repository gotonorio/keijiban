from django import forms

from bbs.models import File


CSS_CHOICES = (
    ('contain', '全体表示'),
    ('cover', '等サイズ'),
)


class FileForm(forms.ModelForm):
    """ 
    (1) 不要な画像ファイルは削除することとして、alive要素は封印する。
    (2) 表示順は新しい画像優先とするため、rank要素は封印する。
    ModelForm限定の方法としてclass Metaでwidgetを設定する。class以外も変更できる。
    https://narito.ninja/blog/detail/52/
    """
    class Meta:
        model = File
        fields = ("title", "summary", "img", "created_at")
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
            'created_at': forms.DateTimeInput(attrs={
                'class': 'input',
            }),
            # 'alive': forms.NullBooleanSelect(attrs={
            #     'class': "select-css",
            # }),
            # 'rank': forms.TextInput(attrs={
            #     'class': "input",
            # }),
        }


class SwitchCSSForm(forms.Form):
    """ 掲示板のcssを切り替えるためのform """
    css = forms.ChoiceField(
        label='CSS',
        widget=forms.Select(attrs={'class': 'select-css'}),
        choices=CSS_CHOICES,
        required=True,
    )
