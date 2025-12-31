"""
Shared Sphinx configuration using sphinx-multiproject.

To build each project, the ``PROJECT`` environment variable is used.

.. code:: console

   $ make html  # build default project
   $ PROJECT=en make html  # build the English project
   $ PROJECT=zh make html  # build the Chinese project

for more information read https://sphinx-multiproject.readthedocs.io/.
"""

import os
import sys

# 修复导入：检查不同的导入方式
try:
    # 首先尝试 sphinx_multiproject
    from sphinx_multiproject.utils import get_project
    print("INFO: Using sphinx_multiproject")
except ImportError:
    try:
        # 然后尝试 multiproject
        from multiproject.utils import get_project
        print("INFO: Using multiproject")
    except ImportError:
        # 如果都失败，创建一个简单的 get_project 函数
        print("WARNING: sphinx-multiproject not found. Using simple project selection.")
        def get_project(projects):
            return os.environ.get("PROJECT", "en")

sys.path.append(os.path.abspath("_ext"))

# 基础扩展 - 只包含实际安装的
extensions = [
    "multiproject",  # Sphinx扩展名，不是Python模块名
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    # 暂时注释掉可能出问题的扩展
    # "sphinx_tabs.tabs",  # 可能模块名不同
    # "sphinx_prompt",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    # 注释掉未安装的扩展
    # "sphinxcontrib.httpdomain",
    # "sphinxcontrib.video",
    # "sphinxemoji.sphinxemoji",
    "sphinxext.opengraph",
]

# 检查并添加实际安装的扩展
try:
    import sphinx_tabs
    extensions.append("sphinx_tabs.tabs")
    print("INFO: sphinx_tabs extension added")
except ImportError:
    print("INFO: sphinx_tabs not available")

try:
    import sphinx_prompt
    extensions.append("sphinx_prompt")
    print("INFO: sphinx_prompt extension added")
except ImportError:
    print("INFO: sphinx_prompt not available")

multiproject_projects = {
    "en": {
        "use_config_file": False,
        "config": {
            "project": "KernelGen Documentation",
            "html_title": "KernelGen Documentation",
        },
    },
    "zh": {
        "use_config_file": False,
        "config": {
            "project": "KernelGen 文档",
            "html_title": "KernelGen 文档",
        },
    },
}

docset = get_project(multiproject_projects)

ogp_site_name = "KernelGen Documentation"
ogp_use_first_image = True
ogp_image = "https://docs.readthedocs.io/en/latest/_static/img/logo-opengraph.png"
ogp_custom_meta_tags = (
    '<meta name="twitter:card" content="summary_large_image" />',
)
ogp_enable_meta_description = True
ogp_description_length = 300

templates_path = ["_templates"]
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

master_doc = "index"
copyright = "KernelGen Team & contributors"
version = "1.0.0"
release = version
exclude_patterns = ["_build", "shared", "_includes"]
if docset == "zh":
    exclude_patterns.append("en")
elif docset == "en":
    exclude_patterns.append("zh")
default_role = "obj"
intersphinx_cache_limit = 14
intersphinx_timeout = 3
intersphinx_mapping = {
    "python": ("https://docs.python.org/3.10/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

intersphinx_disabled_reftypes = ["*"]

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    # "linkify",
    "strikethrough",
    "substitution",
    "tasklist",
    "attrs_inline",
    "attrs_block",
]
htmlhelp_basename = "KernelGendoc"
latex_documents = [
    (
        "index",
        "KernelGen.tex",
        "KernelGen Documentation",
        "KernelGen Team",
        "manual",
    ),
]
man_pages = [
    (
        "index",
        "kernelgen",
        "KernelGen Documentation",
        ["KernelGen Team"],
        1,
    )
]

language = "en" if docset == "en" else "zh_CN"

locale_dirs = [
    f"{docset}/locale/",
]
gettext_compact = False

html_theme = "sphinx_book_theme"
html_static_path = ["_static", f"{docset}/_static"]
html_css_files = ["css/custom.css"]
# 先不添加 sphinx_prompt_css.css，可能不存在
html_js_files = []

html_logo = "img/logo.svg"
html_theme_options = {
    "logo_only": True,
}
html_context = {
    "conf_py_path": f"/docs/{docset}/",
    "display_github": True,
    "github_user": "armstrongttwalker-alt",
    "github_repo": "test-i18n-KernelGen",
    "github_version": "main",
    "plausible_domain": f"{os.environ.get('READTHEDOCS_PROJECT')}.readthedocs.io",
}

rst_epilog = """
.. |org_brand| replace:: KernelGen Community
.. |com_brand| replace:: KernelGen for Business
.. |git_providers_and| replace:: GitHub, Bitbucket, and GitLab
.. |git_providers_or| replace:: GitHub, Bitbucket, or GitLab
"""

autosectionlabel_prefix_document = True

linkcheck_retries = 2
linkcheck_timeout = 1
linkcheck_workers = 10
linkcheck_ignore = [
    r"http://127\.0\.0\.1",
    r"http://localhost",
    r"https://github\.com.+?#L\d+",
]

extlinks = {
    "issue": ("https://github.com/armstrongttwalker-alt/test-i18n-KernelGen/issues/%s", "#%s"),
}

suppress_warnings = ["epub.unknown_project_files"]