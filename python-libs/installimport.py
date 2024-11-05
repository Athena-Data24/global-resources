import subprocess
import sys
import importlib

def install_and_import(packages):
    """
    Checks if each package is installed; if not, installs it using pip.
    Args:
        packages (dict): A dictionary with package names as keys and aliases as values.
    """
    for package, alias in packages.items():
        try:
            # Try importing the package
            globals()[alias] = importlib.import_module(package)
            print(f"{package} imported successfully as {alias}.")
        except ImportError:
            print(f"{package} not found. Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            # Try importing the package after installation
            globals()[alias] = importlib.import_module(package)
            print(f"{package} installed and imported successfully as {alias}.")
        else:
            print(f"{package} is already installed.")

# List of packages with aliases (declared outside the function)
"""required_packages = {
    'pandas': 'pd',
    'numpy': 'np',
    'ydata_profiling': 'ydata_profiling',
    'xgboost': 'xgb',
    'optuna': 'optuna',
    'plotly': 'plotly',
    'shap': 'shap',
    'hashlib': 'hashlib',
    'catboost': 'catboost',
    'lightgbm': 'lgb'
}"""

required_packages = {
    'pandas': 'pd',
    'numpy': 'np'}

# Run the function with the required packages
install_and_import(required_packages)

# Example usage: Checking if numpy was imported successfully as np
try:
    print(np.__version__)  # This will print the version of numpy if it was successfully imported
except NameError:
    print("numpy was not imported successfully.")
