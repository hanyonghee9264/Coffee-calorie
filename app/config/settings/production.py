from .base import *

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.production.application'

secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']

DATABASES = secrets['DATABASES']


# django-storages
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
AWS_ACCESS_KEY_ID = secrets['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']

# 로그폴더 생성
LOG_DIR = os.path.join(ROOT_DIR, '.log')
# 로그 폴더가 존재하지 않으면 폴더 생성
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] %(name)s (%(asctime)s)\n\t%(message)s'
        },
    },
    'handlers': {
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default',
            'maxBytes': 10485760,
            'backupCount': 10,
        },
        'file_info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'filename': os.path.join(LOG_DIR, 'info.log'),
            'formatter': 'default',
            'maxBytes': 10485760,
            'backupCount': 10,
        },
        # console에 StreamHandler는
        # 터미널창에 표시
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'file_error',
                'file_info',
                'console',
            ],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

