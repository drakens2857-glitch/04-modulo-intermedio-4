from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial = True

dependencies = [
migrations.swappable_dependency(settings.AUTH_USER_MODEL),
]
operations = [
migrations.CreateModel(
name='Categoria',
fields=[
('id', models.BigAutoField(auto_created=True, primary_key=True,
serialize=False, verbose_name='ID')),
('nombre', models.CharField(max_length=100, unique=True)),
('descripcion', models.TextField(blank=True)),
('creado', models.DateTimeField(auto_now_add=True)),
],
options={
'verbose_name': 'Categoría',
'verbose_name_plural': 'Categorías',
'ordering': ['nombre'],
},
),

]