project = 'Subaru GPS'
author = 'Subaru GPS'
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

# Bing search verification
html_context = {
    'bing_verification_code': '89E119164B044B0B4EE80A50AB60418E'
}

# Base URL for sitemap
html_baseurl = 'https://guide-subarugps.readthedocs.io/en/latest/'
