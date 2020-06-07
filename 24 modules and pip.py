import useful_tools
import docx

docx.Document()

# My scripts can be found in Finder at the high level folder PycharmProjects
# Or right_click the tab of this file and select -  'Reveal in Finder'
print(useful_tools.roll_dice(10))
print(useful_tools.meters_in_kilometer)
print(useful_tools.feet_in_mile)
print(useful_tools.get_file_ext("index.html"))
print(useful_tools.beatles[1])
print(useful_tools.beatles[-1])
print(useful_tools.beatles[0:])

# You can Google - List of Python Modules and you should see something like Python Module Index in the results for version ie 3.8.2
# https://docs.python.org/3/py-modindex.html
# Some of the modules listed are built into Python and some are External
# The External ones can be seen on the left-hand side of this window 'External Libraries' and go into 'python3.8'
# You can also simply google for a python module for what you want to do. Some third party/person has often already done it

# Example
# 1. Google python.docx (this module can create Word Docs from Python)
# 2. https://python-docx.readthedocs.io/en/latest/
# 3. https://python-docx.readthedocs.io/en/latest/user/install.html#install
# 4. Off the webpage copy: pip install python-docx (pip comes pre-installed with python 3 - Its a package manager -install, uninstall, update)
# 5. for pip open up Terminal (or cmd in Windows)
# 6. I keyed in: pip3 --version    (this came up with a version number which proved I have it)
# 7. I then keyed in pip3 install python-docx - this successfully installed the module
# 8. This module is now visible to the left of this editor under 'site-packages' folder
# 9. You will see folders 'docx' and python_docx-0.8.10...
#10. Can use pip to uninstall if you wanted to.  pip3 uninstall python-docx


