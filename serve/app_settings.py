from django.conf import settings
from django.shortcuts import resolve_url
from django.urls import get_script_prefix
from django.utils.functional import lazy
import os


""" 
Serve CDN or static css files to your template. 
"""
CSS_PATH = getattr(settings, 'STYLESHEETS', [
    {
        'src': ''
    },
])


""" 
Serve CDN or static js files to your template. 
"""
JAVASCRIPT_PATH = getattr(settings, 'JAVASCRIPT', [
    {
        'src': ''
    },
])


""" 
Serve CDN or static fonts files to your template. 
"""
FONT_PATH = getattr(settings, 'FONTS', [
    {
        'src': ''
    },
])

# Lazy-evaluate URLs so including app.urls in root urlconf works
resolve_url = lazy(resolve_url, str)

# Get script prefix for apps not mounted under /
_SCRIPT_PREFIX = get_script_prefix()


""" 
Path to the service worker implementation.  
    Default implementation is empty. 
"""
SERVICE_WORKER_PATH = getattr(
    settings, 'SERVICE_WORKER_PATH',
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'dist/templates/manifest', 'serviceworker.js'))

""" 
App parameters to include in manifest.json and appropriate meta tags. 
"""
APP_NAME = getattr(settings, 'APP_NAME', 'MyApp')
APP_DESCRIPTION = getattr(settings, 'APP_DESCRIPTION', 'Django Angular Progressive Web App')
APP_ROOT_URL = resolve_url(getattr(settings, 'APP_ROOT_URL', _SCRIPT_PREFIX))
APP_THEME_COLOR = getattr(settings, 'APP_THEME_COLOR', '#000')
APP_BACKGROUND_COLOR = getattr(settings, 'APP_BACKGROUND_COLOR', '#fff')
APP_DISPLAY = getattr(settings, 'APP_DISPLAY', 'standalone')
APP_SCOPE = resolve_url(getattr(settings, 'APP_SCOPE', _SCRIPT_PREFIX))
APP_DEBUG_MODE = getattr(settings, 'APP_DEBUG_MODE', True)
APP_ORIENTATION = getattr(settings, 'APP_ORIENTATION', 'any')
APP_START_URL = resolve_url(getattr(settings, 'APP_START_URL', _SCRIPT_PREFIX))
APP_FETCH_URL = resolve_url(getattr(settings, 'APP_FETCH_URL', _SCRIPT_PREFIX))
APP_STATUS_BAR_COLOR = getattr(settings, 'APP_STATUS_BAR_COLOR', 'default')
APP_ICONS = getattr(settings, 'APP_ICONS', [
    {
        'src': '/static/img/icon-72x72.png',
        'size': '72x72'
    },
    {
        'src': '/static/img/icon-96x96.png',
        'size': '96x96'
    },
    {
        'src': '/static/img/icon-128x128.png',
        'size': '128x128'
    },
    {
        'src': '/static/img/icon-144x144.png',
        'size': '144x144'
    },
    {
        'src': '/static/img/icon-152x152.png',
        'size': '152x152'
    },
    {
        'src': '/static/img/icon-192x192.png',
        'size': '192x192'
    },
    {
        'src': '/static/img/icon-384x384.png',
        'size': '384x384'
    },
    {
        'src': '/static/img/icon-512x512.png',
        'size': '512x512'
    }
])
APP_SPLASH_SCREEN = getattr(settings, 'APP_SPLASH_SCREEN', [
    {
        'src': '/static/img/splash-640x1136.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/splash-750x1334.png',
        'media': '(device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/splash-1242x2208.png',
        'media': '(device-width: 621px) and (device-height: 1104px) and (-webkit-device-pixel-ratio: 3)'
    },
    {
        'src': '/static/img/splash-1125x2436.png',
        'media': '(device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3)'
    },
    {
        'src': '/static/img/splash-828x1792.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/splash-1242x2688.png',
        'media': '(device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3)'
    },
    {
        'src': '/static/img/splash-1536x2048.png',
        'media': '(device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/splash-1668x2224.png',
        'media': '(device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/splash-1668x2388.png',
        'media': '(device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2)'
    },
    {
        'src': '/static/img/splash-2048x2732.png',
        'media': '(device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2)'
    }

])
APP_DIR = getattr(settings, 'APP_DIR', 'auto')
APP_LANG = getattr(settings, 'APP_LANG', 'en-US')
