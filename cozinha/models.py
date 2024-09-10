from django.db import models
from django.contrib.auth.models import User
from categoria.models import Category
# Create your models here.
class Food(models.Model):
    Author = models.ForeignKey(User,on_delete=models.CASCADE)#usuario logado,onde ira detectar o usuario logado e mostrar na publicação
    name = models.CharField(max_length=50)#nome da comida
    description = models.TextField(max_length=100)#descrição da comida
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)#categoria da comida
    date_publication = models.DateTimeField(auto_now_add=True)#data que foi postado

    def __str__(self) -> str: #converte para string
        return self.name 


class Meta:
    db_table = 'foods' #tabela do banco de dados

    