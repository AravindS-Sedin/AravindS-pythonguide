# ==================================================
# Virtual Environment & Dependency Manager
#
# Problem:
# Verify whether all required project dependencies
# are installed in the current Python environment.
#
# Tasks:
# 1. Check each required package dynamically.
# 2. Separate installed and missing packages.
# 3. Display dependency check results.
# 4. Report total installed vs missing packages.
#
# Concepts:
# importlib, Dependency Management,
# Virtual Environments, Exception Handling
# ==================================================


import importlib


class DependencyChecker:

    def __init__(self):
        self.required_packages = [
            "requests",
            "pandas",
            "numpy",
            "nonexistent"
        ]

        self.installed = []
        self.missing = []

    def check_packages(self):

        print("\nDependency Check")
        print("-" * 40)

        for package in self.required_packages:

            try:
                importlib.import_module(package)

                print(f"OK   {package}")
                self.installed.append(package)

            except ImportError:

                print(f"MISS {package}")
                self.missing.append(package)

    def summary(self):

        total_required = len(self.required_packages)
        total_installed = len(self.installed)
        total_missing = len(self.missing)

        print("\nSummary")
        print("-" * 40)

        print(f"Required Packages : {total_required}")
        print(f"Installed Packages: {total_installed}")
        print(f"Missing Packages  : {total_missing}")

        print("\nInstalled:")

        for package in self.installed:
            print(f"  - {package}")

        print("\nMissing:")

        for package in self.missing:
            print(f"  - {package}")

    def run(self):

        self.check_packages()
        self.summary()


def main():

    checker = DependencyChecker()
    checker.run()


if __name__ == "__main__":
    main()