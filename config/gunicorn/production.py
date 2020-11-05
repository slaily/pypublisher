from multiprocessing import cpu_count


bind = ['0.0.0.0:8008']
workers = cpu_count() * 2 + 1
timeout = 60
graceful_timeout = 60
preload_app = True
raw_env = [
    'DJANGO_SETTINGS_MODULE=project.settings.production'
]
