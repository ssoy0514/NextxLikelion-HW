from django import forms
from .models import Link, Category
Category_choices = Category.objects.all().values_list('name', 'name')

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':"카테고리를 입력하세요"}),
        }
        
class AddLinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('link', 'link_name', 'category', 'memo')
        widgets = {
            'category' : forms.Select(choices=Category_choices, attrs= {'class':'form-control'}),
            'link' : forms.TextInput(attrs= {'class':'form-control', 'placeholder':"링크를 입력하세요."}),
            'link_name' : forms.TextInput(attrs= {'class':'form-control', 'placeholder':"제목을 입력하세요."}),
            'memo' : forms.TextInput(attrs= {'class':'form-control', 'placeholder':"메모를 입력하세요."}),
        }