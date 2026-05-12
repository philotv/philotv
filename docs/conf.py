project = 'Philo TV login'
author = 'Philo TV login'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Google & Bing Verification Meta Tags
html_context = {
    "meta_tags": """
    
<meta name="google-site-verification" content="ySGxGN4oLx8a2r8biPwCqpOqWCg1LuRj0sioc_kij-M" />
    <meta name="msvalidate.01" content="99668E7FC0E0C7162DF10466BF3247E7" />
    """
}

# Base URL for sitemap
html_baseurl = 'https://userphilo.readthedocs.io/en/latest/'
