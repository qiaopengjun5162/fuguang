"""
Django settings for fuguangapi project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 新增apps作为导包路径，导包路径默认保存sys.path属性中，所有的python的import或者from导包语句默认都是从sys.path中记录的路径下查找模块
sys.path.insert(0, str( BASE_DIR / "apps") )
sys.path.insert(0, str( BASE_DIR / "utils") )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eznjvxi)dl&lp8(&ijsprjv1luf-g&i8dyrn@t(1la)k@p4c&j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders', # cors跨域子应用
    # 'rest_framework_swagger',  # swagger接口文档
    'drf_yasg',  # 接口文档drf_yasg

    'home',
    'users',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # cors跨域的中间件
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fuguangapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fuguangapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'dj_db_conn_pool.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE_FUGUANG_NAME'),
        'PORT': os.getenv('MYSQL_DATABASE_FUGUANG_PORT'),
        'HOST': os.getenv('MYSQL_DATABASE_FUGUANG_HOST'),
        'USER': os.getenv('MYSQL_DATABASE_FUGUANG_USER'),
        'PASSWORD': os.getenv('MYSQL_DATABASE_FUGUANG_PASSWORD'),
        'OPTIONS': {
            'charset': 'utf8mb4',  # 连接选项配置,mysql8.0以上无需配置
        },
        'POOL_OPTIONS': {  # 连接池的配置信息
            'POOL_SIZE': 10,  # 连接池默认创建的链接对象的数量
            'MAX_OVERFLOW': 10  # 连接池默认创建的链接对象的最大数量
        }
    }
}

# redis configration
# https://django-redis-chs.readthedocs.io/zh_CN/latest/#
# 设置redis缓存
CACHES = {
    # 默认缓存
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # 项目上线时,需要调整这里的路径
        "LOCATION": "redis://:123456@127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 提供给admin站点的session存储
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:123456@127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 提供存储短信验证码
    "sms_code":{
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://:123456@127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# 设置用户登录admin站点时,记录登录状态的session保存到redis缓存中
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# 设置session保存的位置对应的缓存配置项
SESSION_CACHE_ALIAS = "session"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# 访问静态文件的url地址前缀
STATIC_URL = 'static/'

# 设置django的静态文件目录[手动创建]
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 项目中存储上传文件的根目录[手动创建]，注意，uploads目录需要手动创建否则上传文件时报错
MEDIA_ROOT = BASE_DIR / "uploads"
# 访问上传文件的url地址前缀
MEDIA_URL = "/uploads/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 日志配置
# https://docs.djangoproject.com/zh-hans/4.2/topics/logging/
LOGGING = {
    'version': 1,  # 使用的日志模块的版本，目前官方提供的只有版本1，但是官方有可能会升级，为了避免升级出现的版本问题，所以这里固定为1
    'disable_existing_loggers': False,  # 是否禁用其他的已经存在的日志功能？肯定不能，有可能有些第三方模块在调用，所以禁用了以后，第三方模块无法捕获自身出现的异常了。
    'formatters': {  # 日志格式设置，verbose或者simple都是自定义的
        'verbose': {  # 详细格式，适合用于开发人员不在场的情况下的日志记录。
            # 格式定义：https://docs.python.org/3/library/logging.html#logrecord-attributes
            # levelname 日志等级
            # asctime   发生时间
            # module    文件名
            # process   进程ID
            # thread    线程ID
            # message   异常信息
            'format': '{levelname} {asctime} {module} {funcName} {process:d} {thread:d} {message}',
            'style': '{',  # 变量格式分隔符
        },
        'simple': {  # 简单格式，适合用于开发人员在场的情况下的终端输出
            'format': '{levelname} {module} {funcName} {message}',
            'style': '{',
        },
    },
    'filters': {  # 过滤器
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理流程，console或者mail_admins都是自定义的。
        'console': {
            'level': 'DEBUG',  # 设置当前日志处理流程中的日志最低等级
            'filters': ['require_debug_true'],  # 当前日志处理流程的日志过滤
            'class': 'logging.StreamHandler',  # 当前日志处理流程的核心类，StreamHandler可以帮我们把日志信息输出到终端下
            'formatter': 'simple'  # 当前日志处理流程的日志格式
        },
        # 'mail_admins': {
        #     'level': 'ERROR',                  # 设置当前日志处理流程中的日志最低等级
        #     'class': 'django.utils.log.AdminEmailHandler',  # AdminEmailHandler可以帮我们把日志信息输出到管理员邮箱中。
        #     'filters': ['special']             # 当前日志处理流程的日志过滤
        # }
        # 按文件大小来分割日志
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            # 日志位置,日志文件名，日志保存目录logs必须手动创建
            'filename': BASE_DIR.parent / "logs/fuguang.log",
            # 单个日志文件的最大值，这里我们设置300M
            'maxBytes': 300 * 1024 * 1024,
            # 备份日志文件的数量，设置最大日志数量为10
            'backupCount': 20,
            # 日志格式: 详细格式
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志处理的命名空间
        'django': {  # 要在django中调用当前配置项的loging写入日志到文件中，名字必须叫"django"
            'handlers': ['console', 'file'],  # 当基于django命名空间写入日志时，调用那几个日志处理流程
            'propagate': True,  # 是否在django命名空间对应的日志处理流程结束以后，冒泡通知其他的日志功能。True表示允许
        },
    }
}

# drf配置
REST_FRAMEWORK = {
    # 自定义异常处理
    'EXCEPTION_HANDLER': 'fuguangapi.utils.exceptions.custom_exception_handler',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 自定义认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # jwt认证
        # 'rest_framework.authentication.SessionAuthentication',  # session认证
        # 'rest_framework.authentication.BasicAuthentication',

        # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
        # JWT认证:使用SimpleJWT库提供的JWTAuthentication类来进行认证
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # session认证
        'rest_framework.authentication.SessionAuthentication',
        # 基本认证
        'rest_framework.authentication.BasicAuthentication',


    ),
}

import datetime
# # jwt认证相关配置项
# JWT_AUTH = {
#     # 设置jwt的有效期
#     # 如果内部站点，例如：运维开发系统，OA，往往配置的access_token有效期基本就是15分钟，30分钟，1~2个小时
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(weeks=1), # 一周有效，
# }

SIMPLE_JWT = {
    # token有效时长(返回的 access 有效时长)
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(seconds=30),
    # token刷新的有效时间(返回的 refresh 有效时长)
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(seconds=20),
    "TOKEN_OBTAIN_SERIALIZER": "fuguangapi.utils.authenticate.MyTokenObtainPairSerializer",
}



# CORS的配置信息:
# 方案1：
# CORS_ORIGIN_WHITELIST = (
#     'http://www.fuguang.cn:3000',
# )
# CORS_ALLOW_CREDENTIALS = False  # 不允许ajax跨域请求时携带cookie

# 方案2：
CORS_ALLOW_ALL_ORIGINS = True

# SWAGGER_SETTINGS = {
#     # 基础样式
#     'SECURITY_DEFINITIONS': {
#         "basic": {
#             'type': 'basic'
#         }
#     },
#     # 如果需要登录才能够查看接口文档, 登录的链接使用restframework自带的.
#     'LOGIN_URL': 'rest_framework:login',
#     'LOGOUT_URL': 'rest_framework:logout',
#     # 'DOC_EXPANSION': None,
#     # 'SHOW_REQUEST_HEADERS':True,
#     # 'USE_SESSION_AUTH': True,
#     # 'DOC_EXPANSION': 'list',
#     # 接口文档中方法列表以首字母升序排列
#     'APIS_SORTER': 'alpha',
#     # 如果支持json提交, 则接口文档中包含json输入框
#     'JSON_EDITOR': True,
#     # 方法列表字母排序
#     'OPERATIONS_SORTER': 'alpha',
#     'VALIDATOR_URL': None,
# }

# 自定义的用户模型类
# `AUTH_USER_MODEL` 参数的设置以`点.`来分隔，表示`应用名.模型类名`。
# 注意：Django建议我们对于AUTH_USER_MODEL参数的设置一定要在第一次数据库迁移之前就设置好，否则后续使用可能出现未知错误。
AUTH_USER_MODEL = 'users.User'

# django自定义认证
AUTHENTICATION_BACKENDS = ['fuguangapi.utils.authenticate.CustomAuthBackend', ]