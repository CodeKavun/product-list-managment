from django import forms

from apps.core.models import Product, Brand, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'required': True
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'step': 0.5,
                'min': 0
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'required': True,
                'min': 0
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'required': True
            }),
            'brand': forms.Select(attrs={
                'class': 'form-control',
                'required': False
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'required': False
            })
        }


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            })
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True
            })
        }
