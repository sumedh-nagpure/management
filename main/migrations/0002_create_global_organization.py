from django.db import migrations

def create_global_organization(apps, schema_editor):
    Organization = apps.get_model('main', 'Organization')
    Organization.objects.create(name='Global', email_domain='')

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_global_organization),
    ]
