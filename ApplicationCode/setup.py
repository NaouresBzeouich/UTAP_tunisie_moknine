import sys
from cx_Freeze import setup, Executable

# Your main script file (replace 'your_script.py' with your actual script's name)
script = '__init__.py'

# Dependencies (add any other dependencies your script uses)
includes = []

# Create an executable
exe = Executable(
    script,
    base=None,  # Set this to None for a GUI application
)

# Additional data files (add the paths to your Excel and image files)
additional_files = [
    ('userList.xlsx', 'userList.xlsx'),  # Include userList.xlsx
    ('subscriberlist.xlsx', 'subscriberlist.xlsx'),  # Include subscriberlist.xlsx
    ('utap (2).ico', 'utap (2).ico'),  # Include utap (2).ico
]

# Build options
build_options = {
    'includes': includes,
    'include_files': additional_files,
}

# Setup configuration
setup(
    name='YourAppName',  # Replace with your app's name
    version='1.0',
    description='Description of your app',
    options={'build_exe': build_options},
    executables=[exe],
)
