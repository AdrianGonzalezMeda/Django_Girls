from django import forms
from .models import Post, Comment


# class PostForm(forms.ModelForm):  Ya no nos sirve de nada por que se crea directamente en las class based view, que heredan de model form mixins que es quien
#le da el comportamiento de crear formiularios basados en un modelo


# 	class Meta:
# 		model = Post
# 		fields = ('title', 'text',)

class CommentForm(forms.ModelForm):


	class Meta:
		model = Comment
		fields = ('text',)