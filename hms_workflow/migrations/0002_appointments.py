# Generated by Django 4.2.3 on 2023-07-29 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms_workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('notes', models.TextField(blank=True)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_workflow.doctor')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_workflow.hospital')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hms_workflow.patient')),
            ],
        ),
    ]
