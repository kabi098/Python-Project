
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FinTech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='ExpenseCategory',
        ),
        migrations.AlterField(
            model_name='income',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_catg', to='FinTech.incomecategory'),
        ),
    ]
