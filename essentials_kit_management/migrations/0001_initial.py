# Generated by Django 3.0.5 on 2020-06-06 01:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=300)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('upi_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('account_holder', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('min_quantity', models.IntegerField(default=0)),
                ('max_quantity', models.IntegerField()),
                ('price_per_item', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('LIVE', 'LIVE'), ('CLOSED', 'CLOSED'), ('DONE', 'DONE')], max_length=10, null=True)),
                ('description', models.TextField()),
                ('close_date', models.DateTimeField(null=True)),
                ('expected_delivery_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('brand', models.ManyToManyField(to='essentials_kit_management.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=50)),
                ('transaction_type', models.CharField(choices=[('CREDITED', 'CREDITED'), ('DEBITED', 'DEBITED')], default='CREDITED', max_length=50)),
                ('screen_shot', models.TextField()),
                ('payment_type', models.CharField(choices=[('PHONE_PAY', 'PHONE_PAY'), ('GOOGLE_PAY', 'GOOGLE_PAY'), ('PAYTM', 'PAYTM')], max_length=10)),
                ('remark', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('items', models.ManyToManyField(to='essentials_kit_management.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('pending_count', models.IntegerField()),
                ('out_of_stock', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essentials_kit_management.Brand')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essentials_kit_management.Form')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essentials_kit_management.Item')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='essentials_kit_management.Section')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='form',
            name='sections',
            field=models.ManyToManyField(to='essentials_kit_management.Section'),
        ),
    ]
