# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sdg*7d0vfaqb)0%f%$n*$8wmopr!3s&yqxn#!-e+1sz&hl&==w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # ✅ Set to False for production!

ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']  # ✅ Replace 'yourdomain.com' with actual domain

# Application definition
INSTALLED_APPS = [
    ...
    'csp',  # ✅ Add this if using django-csp for Content Security Policy
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',  # ✅ Add this line for CSP enforcement
]

# ✅ Secure cookies (only sent over HTTPS)
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ✅ Browser-side security headers
SECURE_BROWSER_XSS_FILTER = True  # Helps prevent reflected XSS
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents MIME-type sniffing
X_FRAME_OPTIONS = 'DENY'  # Prevents clickjacking by disallowing your site in iframes

# ✅ Optional: HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ✅ Content Security Policy settings (via django-csp)
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", 'ajax.googleapis.com')
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
CSP_IMG_SRC = ("'self'", 'data:')

# ✅ You already have this
AUTH_USER_MODEL = "bookshelf.CustomUser"

# 🔐 Redirect all HTTP to HTTPS
SECURE_SSL_REDIRECT = True  # ✅ Forces HTTPS

# 🔐 HTTP Strict Transport Security (HSTS) - tells browsers to always use HTTPS
SECURE_HSTS_SECONDS = 31536000  # ✅ 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # ✅ Apply to subdomains too
SECURE_HSTS_PRELOAD = True  # ✅ Allow preload list submission

# ✅ Add comments for documentation

# 🔒 Ensure cookies only work over HTTPS
SESSION_COOKIE_SECURE = True  # ✅ For session cookies
CSRF_COOKIE_SECURE = True     # ✅ For CSRF protection

# Security Headers - Protect against clickjacking, XSS, and MIME sniffing

X_FRAME_OPTIONS = 'DENY'  # Prevent your site from being framed (clickjacking protection)
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME sniffing
SECURE_BROWSER_XSS_FILTER = True  # Enable browser XSS filter
