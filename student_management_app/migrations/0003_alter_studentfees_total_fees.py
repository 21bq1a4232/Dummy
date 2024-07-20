# Generated by Django 5.0.6 on 2024-07-01 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_management_app", "0002_remove_feesstructure_lab_fee_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentfees",
            name="total_fees",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="student_management_app.courses",
            ),
        ),
    ]