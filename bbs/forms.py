from django import forms

from bbs.models import Category, File


class FileForm(forms.ModelForm):
    """ Fileモデルのフォーム
    ModelForm限定の方法としてclass Metaでwidgetを設定する。class以外も変更できる。
    https://narito.ninja/blog/detail/52/
    """
    class Meta:
        model = File
        fields = ("title", "category", "summary", "src", "rank", "created_at", "alive")
        # field毎に異なるclassを設定する場合には、この方法を取る。
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "input",
            }),
            'category': forms.Select(attrs={
                'class': "select-css",
            }),
            'summary': forms.Textarea(attrs={
                'class': "textarea",
            }),
            'src': forms.ClearableFileInput(attrs={
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


class CategoryForm(forms.ModelForm):
    """ Categoryモデルのフォーム """
    class Meta:
        model = Category
        fields = ('name', 'path_name', 'rank', 'created_at', 'restrict', 'alive')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "input",
            }),
            'path_name': forms.TextInput(attrs={
                'class': "input",
            }),
            'rank': forms.TextInput(attrs={
                'class': "input",
            }),
            'created_at': forms.DateInput(attrs={
                'class': "input",
            }),
            'restrict': forms.CheckboxInput(attrs={
                'class': "checkboxinput",
            }),
            'alive': forms.CheckboxInput(attrs={
                'class': "checkboxinput",
            }),
        }