# File: docs/conf.py

from multiproject.utils import get_project

extensions = [
   "multiproject",
]

multiproject_projects = {
   # Set `use_config_file` to false
   # to avoid including the files twice.
   "en": {
       "use_config_file": False,
   },
   "zh": {
       "use_config_file": False,
   },
}

current_project  = get_project(multiproject_projects)

master_doc = "index"

# Set all values directly
# -----------------------

if current_project == 'en':
   # File: docs/user/conf.py
   from en.conf import *
elif current_project == 'zh':
   # File: docs/dev/conf.py
   from zh.conf import *
