import os
import sys

sys.path.insert(0, os.path.abspath("../source"))
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../OC_Python_P13_Lettings/lettings/'))
sys.path.insert(0, os.path.abspath('../../OC_Python_P13_Lettings/lettings/models'))
sys.path.insert(0, os.path.abspath('../../OC_Python_P13_Lettings/lettings/views'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'orange-county-lettings'
copyright = '2024, Sandra Weidenthal'
author = 'Sandra Weidenthal'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinxcontrib_django',

]

# Configure the path to the Django settings module
django_settings = "oc_lettings_site.settings"

templates_path = ['_templates']
exclude_patterns = []
autosummary_generate = True
napoleon_use_param = True
napoleon_attr_annotations = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
