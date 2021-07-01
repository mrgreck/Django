from django.apps import AppConfig


class NewsPaperConfig(AppConfig):
    name = 'NewsPaper'

    def ready(self):
        import NewsPaper.signals
