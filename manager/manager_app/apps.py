from django.apps import AppConfig


class ManagerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager_app'
    verbose_name = 'Manager App'
