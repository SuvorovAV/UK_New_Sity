# Generated by Django 2.2.24 on 2021-06-15 11:43

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=128, verbose_name='Город')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': '001 Города',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3, verbose_name='Номер')),
                ('add_number', models.CharField(blank=True, default='-', max_length=3, verbose_name='Корпус')),
                ('sq_home', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Площадь')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': '007 Дома',
            },
        ),
        migrations.CreateModel(
            name='Metrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Единица измерения')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активная')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Единица измерения',
                'verbose_name_plural': '003 Единицы измерения',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Услуга')),
                ('rate', models.DecimalField(decimal_places=3, default=0, max_digits=7, verbose_name='Тариф')),
                ('factor', models.DecimalField(decimal_places=2, default=1, max_digits=3, verbose_name='Коэфициент')),
                ('const', models.BooleanField(db_index=True, default=True, verbose_name='Константа')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активная')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Услугу',
                'verbose_name_plural': '005 Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServicesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активная')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': '004 Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=128, verbose_name='Улица')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': '002 Улицы',
            },
        ),
        migrations.CreateModel(
            name='VariablePayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 734372), verbose_name='Создан')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='data')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Итого')),
                ('pre_total', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Итого')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж (перепенные)',
                'verbose_name_plural': 'Платежи (переменные)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], default=None, max_length=1, null=True, verbose_name='Пол')),
                ('type_electric_meter', models.CharField(blank=True, choices=[('1', 'однотарифный'), ('2', 'двухтарифный')], default=None, max_length=1, null=True, verbose_name='Тип счетчика')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL, verbose_name='Пользоваель')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': '009 Профили',
                'ordering': ('updated',),
            },
        ),
        migrations.CreateModel(
            name='UK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('num_building', models.CharField(max_length=3, verbose_name='Номер здания')),
                ('phone', models.CharField(blank=True, help_text='Номер телефона в формате - 79823212334', max_length=11, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('inn', models.CharField(max_length=10, verbose_name='ИНН')),
                ('ps', models.CharField(max_length=20, verbose_name='Расчетный счет')),
                ('bik', models.CharField(max_length=10, verbose_name='БИК')),
                ('ks', models.CharField(max_length=20, verbose_name='Кор.счет')),
                ('bank', models.CharField(max_length=128, verbose_name='Банк')),
                ('web_addr', models.CharField(max_length=128, verbose_name='Сайт')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.City', verbose_name='Город')),
                ('street', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Street', verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Управляющая компания',
                'verbose_name_plural': '006 Управляющие компании',
            },
        ),
        migrations.CreateModel(
            name='Subsidies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.PositiveIntegerField(default=0, verbose_name='Субсидии')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Services', verbose_name='Услуга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Субсидия',
                'verbose_name_plural': '010 Субсидии',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='Standart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 726539), verbose_name='Создан')),
                ('col_water', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Норматив ХВС')),
                ('hot_water', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Норматив ХГС')),
                ('electric_day', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True, verbose_name='Норматив ЭЛ.День')),
                ('electric_night', models.DecimalField(decimal_places=2, default=None, max_digits=6, null=True, verbose_name='Нориматив ЭЛ.Ночь')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Норматив',
                'verbose_name_plural': 'Нормативы',
                'ordering': ('-period',),
            },
        ),
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='mainapp.ServicesCategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='services',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit', to='mainapp.Metrics', verbose_name='Единицы'),
        ),
        migrations.CreateModel(
            name='Recalculations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 731075), verbose_name='Создан')),
                ('recalc', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Сумма')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Services', verbose_name='Услуга')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Перерасчет',
                'verbose_name_plural': 'Перерасчеты',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 736997), verbose_name='Создан')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Данные')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Сумма')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Начисление',
                'verbose_name_plural': 'Начисления',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='Privileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.PositiveIntegerField(default=0, verbose_name='Льготы')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='mainapp.Services', verbose_name='Услуга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Льгота',
                'verbose_name_plural': '011 Льготы',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='PersonalAccountStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Состояние')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Состояние счета',
                'verbose_name_plural': 'Состояния счетов',
                'ordering': ('amount',),
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(verbose_name='Период')),
                ('amount_profit', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Сумма')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='MainBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 738125), verbose_name='Создан')),
                ('direction', models.CharField(choices=[('D', 'Оплата'), ('C', 'Начисление')], max_length=1, verbose_name='Направление')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Сумма')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Главная книга',
                'verbose_name_plural': 'Главная книга',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='HouseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 725485), verbose_name='Создан')),
                ('col_water', models.PositiveIntegerField(null=True, verbose_name='Хол.вода')),
                ('hot_water', models.PositiveIntegerField(null=True, verbose_name='Гор.вода')),
                ('electric_day', models.PositiveIntegerField(null=True, verbose_name='Электр.день')),
                ('electric_night', models.PositiveIntegerField(null=True, verbose_name='Электр.ночь')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Домовой счетчик (история)',
                'verbose_name_plural': 'Домовые счетчики (история)',
                'ordering': ('-updated',),
            },
        ),
        migrations.CreateModel(
            name='HouseCurrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 724508), verbose_name='Создан')),
                ('col_water', models.PositiveIntegerField(default=None, null=True, verbose_name='Хол.вода')),
                ('hot_water', models.PositiveIntegerField(default=None, null=True, verbose_name='Гор.вода')),
                ('electric_day', models.PositiveIntegerField(default=None, null=True, verbose_name='Электр.день')),
                ('electric_night', models.PositiveIntegerField(default=None, null=True, verbose_name='Электр.ночь')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.House', verbose_name='Дом')),
            ],
            options={
                'verbose_name': 'Домовой счетчик (текущий)',
                'verbose_name_plural': 'Домовые счетчики (текущие)',
            },
        ),
        migrations.AddField(
            model_name='house',
            name='category_rate',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.ServicesCategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='house',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.City', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Street', verbose_name='Улица'),
        ),
        migrations.AddField(
            model_name='house',
            name='uk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.UK', verbose_name='Управляющая компания'),
        ),
        migrations.CreateModel(
            name='HistoryCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 730217), verbose_name='Создан')),
                ('col_water', models.PositiveIntegerField(null=True, verbose_name='Гор.вода')),
                ('hot_water', models.PositiveIntegerField(null=True, verbose_name='Хол.вода')),
                ('electric_day', models.PositiveIntegerField(blank=True, null=True, verbose_name='Электр.день')),
                ('electric_night', models.PositiveIntegerField(blank=True, null=True, verbose_name='Электр.ночь')),
                ('electric_single', models.PositiveIntegerField(blank=True, null=True, verbose_name='Электр.однотариф')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Индивид. счетчик (история)',
                'verbose_name_plural': 'Индивид. счетчики (история)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='HeaderData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Данные')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Начисление',
                'verbose_name_plural': 'Начисления',
            },
        ),
        migrations.CreateModel(
            name='CurrentCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(default=datetime.datetime(2021, 6, 1, 11, 43, 10, 729525), verbose_name='Создан')),
                ('col_water', models.PositiveIntegerField(default=None, null=True, verbose_name='Холодная вода')),
                ('hot_water', models.PositiveIntegerField(default=None, null=True, verbose_name='Горячая вода')),
                ('electric_day', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Электроэнергия день')),
                ('electric_night', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Электроэнергия ночь')),
                ('electric_single', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Электроэнергия')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Индивид. счетчик (текущий)',
                'verbose_name_plural': 'Индивид. счетчики (текущие)',
                'ordering': ('-period',),
            },
        ),
        migrations.CreateModel(
            name='ConstantPayments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='data')),
                ('total', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Сумма')),
                ('pre_total', models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Сумма')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж (постоянные)',
                'verbose_name_plural': 'Платежи (постоянные)',
            },
        ),
        migrations.CreateModel(
            name='Appartament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3, verbose_name='Номер квартиры')),
                ('add_number', models.PositiveIntegerField(default=0, verbose_name='Комната')),
                ('sq_appart', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Площадь')),
                ('num_owner', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Кол-во проживающих')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Активный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.House', verbose_name='Дом')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appartament', to=settings.AUTH_USER_MODEL, verbose_name='Жилец')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': '008 Квартиры',
                'unique_together': {('house', 'number', 'add_number')},
            },
        ),
    ]
