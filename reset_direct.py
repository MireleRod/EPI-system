#script para resetar o autoincrement do banco de dados sqlite (só funciona após deletar os dados da db :/)

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epi_project.settings')
django.setup()

from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'colaboradores_colaborador'")
    connection.commit()
print('sequence resetada com sucesso sdfsdgrb')
