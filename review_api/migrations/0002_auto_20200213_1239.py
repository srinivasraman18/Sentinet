# Generated by Django 3.0.3 on 2020-02-13 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.IntegerField()),
                ('negative', models.IntegerField()),
                ('happy', models.IntegerField()),
                ('sad', models.IntegerField()),
                ('angry', models.IntegerField()),
                ('surprise', models.IntegerField()),
                ('love', models.IntegerField()),
                ('joy', models.IntegerField()),
                ('offensive', models.IntegerField()),
                ('non_offensive', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offensive', models.IntegerField()),
                ('non_offensive', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_id', models.IntegerField()),
                ('sentiment', models.CharField(max_length=10)),
                ('emotion', models.CharField(max_length=10)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review_api.Business')),
            ],
        ),
        migrations.RenameField(
            model_name='category',
            old_name='business_id',
            new_name='business',
        ),
        migrations.RemoveField(
            model_name='emotion',
            name='emotion',
        ),
        migrations.RemoveField(
            model_name='emotion',
            name='review_id',
        ),
        migrations.RemoveField(
            model_name='sentiment',
            name='review_id',
        ),
        migrations.RemoveField(
            model_name='sentiment',
            name='sentiment',
        ),
        migrations.AddField(
            model_name='emotion',
            name='angry',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emotion',
            name='business',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='review_api.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emotion',
            name='happy',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emotion',
            name='joy',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emotion',
            name='love',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emotion',
            name='sad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emotion',
            name='surprise',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentiment',
            name='business',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='review_api.Business'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentiment',
            name='negative',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sentiment',
            name='positive',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OffensiveText',
        ),
        migrations.AddField(
            model_name='categorydata',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review_api.Category'),
        ),
    ]
