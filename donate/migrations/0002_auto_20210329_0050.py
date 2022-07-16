# Generated by Django 3.1.5 on 2021-03-28 19:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('D', 'Denied')], default='P', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='DonationPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='BloodUnits',
            new_name='BloodUnit',
        ),
        migrations.RemoveField(
            model_name='user',
            name='area',
        ),
        migrations.AlterField(
            model_name='user',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('AB-', 'AB Negative'), ('AB+', 'AB Positive'), ('A-', 'A Negative'), ('A+', 'A Positive'), ('B-', 'B Negative'), ('B+', 'B Positive'), ('O-', 'O Negative'), ('O+', 'O Positive')], max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='street',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='BloodRequests',
        ),
        migrations.AddField(
            model_name='donationplace',
            name='donors',
            field=models.ManyToManyField(blank=True, null=True, related_name='donations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_donor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='requests',
            field=models.ManyToManyField(blank=True, through='donate.BloodRequest', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bloodbank',
            name='dp_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank', to='donate.donationplace'),
        ),
        migrations.AlterField(
            model_name='donationcamp',
            name='dp_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='camp', to='donate.donationplace'),
        ),
        migrations.DeleteModel(
            name='DonationPlaces',
        ),
    ]
