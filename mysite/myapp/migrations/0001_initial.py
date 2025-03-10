# Generated by Django 5.1.5 on 2025-02-24 05:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'equipo',
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'grupo',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'rol',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='activo', max_length=20)),
                ('descripcion', models.CharField(default='activo por defecto', max_length=150)),
            ],
            options={
                'db_table': 'status',
            },
        ),
        migrations.CreateModel(
            name='Status_jugador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='activo', max_length=20)),
                ('descripcion', models.CharField(default='activo por defecto', max_length=100)),
            ],
            options={
                'db_table': 'status_jugador',
            },
        ),
        migrations.CreateModel(
            name='Estadisticas_Jugador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('arrimes_lanzados', models.IntegerField(default=0)),
                ('arimes_buenos', models.IntegerField(default=0)),
                ('average_arrimes', models.IntegerField(default=0)),
                ('bolas_lanzadas', models.IntegerField(default=0)),
                ('bolas_buenas', models.IntegerField(default=0)),
                ('average_bolas', models.IntegerField(default=0)),
                ('rastreros_lazados', models.IntegerField(default=0)),
                ('rastreros_buenos', models.IntegerField(default=0)),
                ('average_rastrero', models.IntegerField(default=0)),
                ('equipo_id', models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.equipo')),
            ],
            options={
                'db_table': 'estadisticas_jugador',
            },
        ),
        migrations.AddField(
            model_name='equipo',
            name='grupo_id',
            field=models.ForeignKey(db_column='grupo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.grupo'),
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('cedula', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('genero', models.CharField(max_length=1)),
                ('equipo_id', models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.equipo')),
                ('estadisticas_id', models.ForeignKey(db_column='estadisticas_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.estadisticas_jugador')),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.status_jugador')),
            ],
            options={
                'db_table': 'jugador',
            },
        ),
        migrations.AddField(
            model_name='estadisticas_jugador',
            name='jugador_id',
            field=models.ForeignKey(db_column='jugador_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.jugador'),
        ),
        migrations.CreateModel(
            name='Jugador_equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('equipo_id', models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.equipo')),
                ('jugador_id', models.ForeignKey(db_column='jugador_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.jugador')),
            ],
            options={
                'db_table': 'jugador_equipo',
            },
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('puntos', models.IntegerField(default=0)),
                ('puntos_rival', models.IntegerField(default=0)),
                ('equipo_id', models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, related_name='partido_equipo', to='myapp.equipo')),
                ('equipo_rival_id', models.ForeignKey(db_column='equipo_rival_id', on_delete=django.db.models.deletion.CASCADE, related_name='partidos_rival', to='myapp.equipo')),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.status')),
            ],
            options={
                'db_table': 'partido',
            },
        ),
        migrations.AddField(
            model_name='estadisticas_jugador',
            name='partido_id',
            field=models.ForeignKey(db_column='partido_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.partido'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='status_id',
            field=models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.status'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='status_id',
            field=models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.status'),
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('ubicacion', models.CharField(max_length=300)),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.status')),
            ],
            options={
                'db_table': 'torneo',
            },
        ),
        migrations.AddField(
            model_name='partido',
            name='torneo_id',
            field=models.ForeignKey(db_column='torneo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.torneo'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='torneo_id',
            field=models.ForeignKey(db_column='torneo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.torneo'),
        ),
        migrations.AddField(
            model_name='estadisticas_jugador',
            name='torneo_id',
            field=models.ForeignKey(db_column='torneo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.torneo'),
        ),
        migrations.CreateModel(
            name='Estadisticas_equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('victorias', models.IntegerField(default=0)),
                ('derrotas', models.IntegerField(default=0)),
                ('equipo_id', models.ForeignKey(db_column='equipo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.equipo')),
                ('grupo_id', models.ForeignKey(db_column='grupo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.grupo')),
                ('torneo_id', models.ForeignKey(db_column='torneo_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.torneo')),
            ],
            options={
                'db_table': 'estadisticas_partido',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=15)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=300)),
                ('correo', models.EmailField(max_length=254)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_ultima_sesion', models.DateTimeField(auto_now_add=True)),
                ('rol_id', models.ForeignKey(db_column='rol_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.rol')),
                ('status_id', models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.status')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.AddField(
            model_name='equipo',
            name='delegado_equipo',
            field=models.ForeignKey(db_column='delegado_equipo', on_delete=django.db.models.deletion.CASCADE, to='myapp.usuario'),
        ),
    ]
