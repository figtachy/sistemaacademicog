from django.db import models

# Create your models here.
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupaçao")
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"


class AreasDoSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Areas do saber")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Area do saber"
        verbose_name_plural = "Areas do saber"
    

class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo da avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo avaliação"
        verbose_name_plural = "Tipos de avaliação"


class PeriodoCurso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Periodos do curso")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Periodo do curso"
        verbose_name_plural = "Periodos do curso"


class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    turno = models.CharField(max_length=100, verbose_name="Turno")

    def __str__(self):
        return f"{self.nome}, {self.turno}"

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=100, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    nome_do_pai = models.CharField(max_length=100, verbose_name="Nome do pai")
    nome_da_mae = models.CharField(max_length=100, verbose_name="Nome da mae")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    data_nasc = models.DateField()
    email = models.CharField(max_length=100, verbose_name="E-mail")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.data_nasc}, {self.cidade}, {self.ocupacao}"

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    site = models.CharField(max_length=100, verbose_name="Site")
    telefone = models.CharField(max_length=100, verbose_name="telefone")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}, {self.site}, {self.telefone}, {self.cidade}"

    class Meta:
        verbose_name = "Instituição de ensino"
        verbose_name_plural = "Instituições de ensino"


class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    carga_horaria_total = models.CharField(max_length=100, verbose_name="Carga horaria total")
    duracao_meses = models.CharField(max_length=100, verbose_name="Duração em meses")
    area_do_saber = models.ForeignKey(AreasDoSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}, {self.carga_horaria_total}, {self.duracao_meses}, {self.area_do_saber}, {self.instituicao}"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"


class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    area_do_saber = models.ForeignKey(AreasDoSaber, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}, {self.area_do_saber}"

    class Meta:
        verbose_name = "Diciplina"
        verbose_name_plural = "Disciplinas"


class Matricula(models.Model):
    instituicao = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()


    def __str__(self):
        return f"{self.instituicao}, {self.curso}, {self.pessoa}, {self.data_inicio}, {self.data_previsao_termino}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"


class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao}, {self.curso}, {self.disciplina}"

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.CharField(max_length=100, verbose_name="Número de faltas")


    def __str__(self):
        return f"{self.curso}, {self.disciplina}, {self.pessoa}, {self.numero_faltas}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequência"


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição")
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.descricao}, {self.data}, {self.curso}, {self.disciplina}, {self.pessoa}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"


class DisciplinaPorCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    carga_horaria = models.CharField(max_length=100, verbose_name="Carga horaria", default='')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoCurso, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.disciplina}, {self.carga_horaria}, {self.curso}, {self.periodo}"

    class Meta:
        verbose_name = "Disciplina por curso"
        verbose_name_plural = "Disciplinas por curso"