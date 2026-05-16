from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('tipo', models.CharField(max_length=100)),
                ('classe_risco', models.CharField(max_length=100)),
                ('data_aquisicao', models.DateField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
