# File: docs/conf.py

extensions = [
   "multiproject",
]

multiproject_projects = {
   # Set `use_config_file` to false
   # to avoid including the files twice.
   "en": {
       "use_config_file": False,
   },
   "zh_CN": {
       "use_config_file": False,
   },
}

current_project  = get_project(multiproject_projects)

# Set all values directly
# -----------------------

if current_project == 'en':
   # File: docs/user/conf.py
   from en.conf import *
elif current_project == 'zh_CN':
   # File: docs/dev/conf.py
   from zh_CN.conf import *
