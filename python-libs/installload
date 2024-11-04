import subprocess
import sys

def install_and_import(packages):
    """
    Checks if each package is installed; if not, installs it using pip.
    Args:
        packages (list): A list of package names as strings.
    """
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            print(f"{package} is already installed.")

# List of packages
required_packages = [
    'pandas',
    'numpy',
    'ydata_profiling',
    'xgboost',
    'optuna',
    'plotly',
    'shap',
    'hashlib',
    'catboost',
    'lightgbm'
]

# Run the function
install_and_import(required_packages)
