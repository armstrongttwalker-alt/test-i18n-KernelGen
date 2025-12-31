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

from multiproject.utils import get_project

sys.path.append(os.path.abspath("_ext"))

extensions = [
    "multiproject",
    "myst_parser",
    # For testing, conditionally disable the custom 404 pages on dev docs
    # "notfound.extension",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_tabs.tabs",
    "sphinx_prompt",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    # "sphinxcontrib.httpdomain",
    "sphinxcontrib.video",
    "sphinxemoji.sphinxemoji",
    "sphinxext.opengraph",
]

multiproject_projects = {
    "en": {
        "use_config_file": False,
        "config": {
            "project": "Your Project Name (English)",
            "html_title": "Your Project English Documentation",
        },
    },
    "zh": {
        "use_config_file": False,
        "config": {
            "project": "您的项目名称（中文）",
            "html_title": "您的中文项目文档",
        },
    },
}

# 设置默认项目为英文
if os.environ.get("PROJECT") not in multiproject_projects:
    os.environ["PROJECT"] = "en"

docset = get_project(multiproject_projects)

# 只在英文项目中启用404扩展（根据需求调整）
if docset == "en":
    extensions.append("notfound.extension")

# 根据项目设置语言特定的配置
if docset == "en":
    language = "en"
    html_title = "Your Project English Documentation"
    copyright = "Your Company © 2023"
    version = "1.0.0"
    
elif docset == "zh":
    language = "zh_CN"
    html_title = "您的中文项目文档"
    copyright = "您的公司 © 2023"
    version = "1.0.0"

ogp_site_name = f"Your Project Documentation ({'English' if docset == 'en' else 'Chinese'})"
ogp_use_first_image = True
ogp_image = "https://your-domain.com/logo.png"
ogp_custom_meta_tags = (
    '<meta name="twitter:card" content="summary_large_image" />',
)
ogp_enable_meta_description = True
ogp_description_length = 300

templates_path = ["_templates"]

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

master_doc = "index"
release = version

# 排除模式可以根据语言项目调整
exclude_patterns = ["_build", "shared", "_includes"]
if docset == "zh":
    # 中文项目可能需要排除一些英文特定的文件
    exclude_patterns.append("en-specific")
elif docset == "en":
    # 英文项目可能需要排除一些中文特定的文件
    exclude_patterns.append("zh-specific")

default_role = "obj"
intersphinx_cache_limit = 14
intersphinx_timeout = 3

# 根据语言设置不同的交叉引用映射
base_intersphinx_mapping = {
    "python": ("https://docs.python.org/3.10/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

if docset == "zh":
    # 中文项目的交叉引用可以使用中文文档
    intersphinx_mapping = {
        **base_intersphinx_mapping,
        "python-zh": ("https://docs.python.org/zh-cn/3.10/", None),
        # 添加其他中文文档的映射
    }
else:
    intersphinx_mapping = base_intersphinx_mapping

intersphinx_disabled_reftypes = ["*"]

myst_enable_extensions = [
    "deflist",
]

# 语言特定的epilog内容
if docset == "zh":
    rst_epilog = """
.. |product_name| replace:: 您的产品名称
.. |company_name| replace:: 您的公司名称
"""
else:
    rst_epilog = """
.. |product_name| replace:: Your Product Name
.. |company_name| replace:: Your Company Name
"""

htmlhelp_basename = f"YourProject{'En' if docset == 'en' else 'Zh'}doc"

latex_documents = [
    (
        "index",
        f"YourProject{'En' if docset == 'en' else 'Zh'}.tex",
        f"Your Project {'English' if docset == 'en' else 'Chinese'} Documentation",
        "Your Name",
        "manual",
    ),
]

man_pages = [
    (
        "index",
        f"your-project-{'en' if docset == 'en' else 'zh'}",
        f"Your Project {'English' if docset == 'en' else 'Chinese'} Documentation",
        ["Your Name"],
        1,
    )
]

# 语言文件路径
locale_dirs = [
    f"locale/{docset}/",  # 假设语言文件在locale/en/和locale/zh/目录下
]
gettext_compact = False
gettext_uuid = True
gettext_location = True

# 主题配置
html_theme = "sphinx_book_theme"
html_static_path = ["_static", f"{docset}/_static"]
html_css_files = ["css/custom.css", "css/sphinx_prompt_css.css"]
html_js_files = ["js/expand_tabs.js"]

html_logo = f"{docset}/_static/logo.png" if os.path.exists(f"{docset}/_static/logo.png") else "_static/logo.png"
html_theme_options = {
    "logo_only": True,
    "language": language,
}

html_context = {
    # 根据项目设置不同的GitHub路径
    "conf_py_path": f"/docs/{docset}/",
    "display_github": True,
    "github_user": "your-username",
    "github_repo": "your-repo",
    "github_version": "main",
    "current_language": docset,
    "languages": [
        ("en", "English"),
        ("zh", "中文"),
    ],
}

# 激活自动章节标签插件
autosectionlabel_prefix_document = True

# 404页面配置
if docset == "en":
    notfound_context = {
        "title": "Page Not Found",
        "body": """
<h1>Page Not Found</h1>
<p>Sorry, we couldn't find that page.</p>
<p>Try using the search box or go to the homepage.</p>
""",
    }
elif docset == "zh":
    notfound_context = {
        "title": "页面未找到",
        "body": """
<h1>页面未找到</h1>
<p>抱歉，我们找不到该页面。</p>
<p>请尝试使用搜索框或返回首页。</p>
""",
    }

linkcheck_retries = 2
linkcheck_timeout = 1
linkcheck_workers = 10
linkcheck_ignore = [
    r"http://127\.0\.0\.1",
    r"http://localhost",
    r"https://yourproject\.readthedocs\.io",
    r"https?://docs\.example\.com",
    r"https://github\.com.+?#L\d+",
]

extlinks = {
    "issue": ("https://github.com/your-username/your-repo/issues/%s", "#%s"),
}

# 禁用epub mimetype警告
suppress_warnings = ["epub.unknown_project_files"]

# 添加项目特定的配置
if docset == "en":
    # 英文项目特定的配置
    html_favicon = f"{docset}/_static/favicon.ico"
elif docset == "zh":
    # 中文项目特定的配置
    html_favicon = f"{docset}/_static/favicon.ico"
    
# 如果使用Read the Docs，设置正确的版本
if os.environ.get('READTHEDOCS'):
    rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
    if rtd_version == 'latest':
        rtd_version = 'latest'
    elif rtd_version == 'stable':
        rtd_version = 'stable'
    else:
        rtd_version = rtd_version