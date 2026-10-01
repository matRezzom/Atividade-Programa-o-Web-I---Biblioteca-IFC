from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField("Título", max_length=150)
    autor = models.CharField("Autor", max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoria")
    ano = models.PositiveIntegerField()
    disponivel = models.BooleanField("Disponível", default=True)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="emprestimos")
    aluno = models.CharField(max_length=100)
    data_retirada = models.DateField("Data de retirada", auto_now_add=True)
    devolvido = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return f"{self.livro} - {self.aluno}"