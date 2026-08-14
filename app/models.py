from django.db import models

# Create your models here.
class Cidade (models.Model):
    nome = models.CharField(max_lenght=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_lenght=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Autor(models.Models):
    nome = models.Char.Field(max_lenght=100, verbose_name="Nome do autor")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCATE,verbose_name="Cidade do autor")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class Editora(models.Model):
    nome = models.CharField(max_lenght=100, verbose_name="Nome da editora")
    site = models.CharField(max_lenght=100, verbose_name="Site da editora")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCATE, verbose_name="Cidade da editora")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Editora"
        verbose_name_pural = "Editoras"

class Leitor(models.Model):
    nome = models.CharField(max_lenght=100, verbose_name="Nome do leitor")
    email = models.CharField(max_lenght=100, verbose_name="Email do leitor")
    cpf = models.CharField(max_lenght=11, unique=True, verbose_name="CPF do leitor")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Leitor"
        verbose_name = "Leitores"

class Genero(models.Model):
    nome = models.CharField(max_lenght=100, verbose_name="Gênero")
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

