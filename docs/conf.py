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
       "config": {
            "master_doc": "en/index",
   },
   "zh": {
       "use_config_file": False,
       "config": {
            "master_doc": "zh/index",
   },
}

current_project  = get_project(multiproject_projects)

