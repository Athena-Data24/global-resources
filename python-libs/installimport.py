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
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            # Import the package after installation
            globals()[alias] = importlib.import_module(package)
        else:
            print(f"{package} is already installed.")

# List of packages with aliases
required_packages = {
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
}

# Run the function
install_and_import(required_packages)

# Example usage
print(np.__version__)  # Checking if numpy was imported successfully as np
