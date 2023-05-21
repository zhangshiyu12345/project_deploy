"""
Django settings for test_project project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
#引入settings.py文件 from django.conf import settings
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #项目绝对路经
#os.path.abspath(__file__):当前settings.py的绝对路劲
#os.path.dirname(os.path.abspath(__file__)):返回settings.py的上一级目录

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bjb#ctly2_+ku^c!n2*t^#*4op1%=9+k8iz-wiv66^uh$&$v(n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#True - 调试模式
#(1)检测代码改动后,立刻重启服务
#(2)报错页面
#(3)
#False - 正式启动模式/上线模式

ALLOWED_HOSTS = ['*']
#请求头里的Host的头(就是与地址栏一样),用来区别于虚拟站点,只有在这个数组中的请求我才接
#默认接127.0.0.1和localhost - DEBUG =True时有效
#正式上线后,在数组中填写的是上线的域名


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'front',
    'front_news',
    'tinymce',
    'front_researchGain',
    'front_resource',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.front.middleware.MiddleWare',
]

ROOT_URLCONF = 'test_project.urls' #django主路由文件的位置

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],#动态路经
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]
#模板使用 from django.shortcuts import render

WSGI_APPLICATION = 'test_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_project', #要连接的数据库名
        'USER':'root',
        'PASSWORD':'245478',
        'HOST':'db',
        'PORT':'3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans' #语言信息配置

TIME_ZONE = 'Asia/Shanghai' #时区

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/' #客户端访问静态内容的位置
STATIC_DIR = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [STATIC_DIR,]#让django去寻找伺服的静态文件

MEDIA_DIR = os.path.join(BASE_DIR,'media')
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'#引擎
EMAIL_HOST = 'smtp.qq.com'#騰訊QQ郵箱SMTP服務器地址
EMAIL_PORT = 25 #SMTP服務的端口浩
EMAIL_HOST_USER = '3419626728@qq.com'#發送郵件的QQ郵箱
EMAIL_HOST_PASSWORD = 'kwcxmeadxyyxcjeh'#授权码
#EMAIL_USE_TLS = False#魚SMTP服務器通信時,是否起動TLS鏈接(安全鏈接)默認FALSE
#gyszpkuvneblciia

#数据库缓存配置 需要手动执行　创建表的命令
CACHES = {
    'default':{
        'BACKEND':'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':'my_cache_table',#需要手动创建
        'TIMEOUT':300,#缓存保存时间　单位秒，默认值为300
        'OPTIONS':{
            'MAX_ENTRIES':300,#缓存最大数据条数
            'CULL_FREQUENCY':2,#缓存条数达到最大值时，删除1/x的缓存数据
        }
    }
}

TINYMCE_DEFAULT_CONFIG = {
    'theme': "silver",
    'plugins': "image,link",
    'toolbar': "image,link",
    'height':'300',
 }
