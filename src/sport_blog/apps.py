from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'sport_blog'

    def ready(self):
        import sport_blog.signals  # noqa
