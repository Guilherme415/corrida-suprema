from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Jogador",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=100)),
                ("pontuacao", models.IntegerField(default=0)),
                ("cor_carro", models.CharField(default="vermelho", max_length=20)),
                ("fases_vencidas", models.IntegerField(default=0)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-pontuacao", "criado_em"]},
        ),
    ]
