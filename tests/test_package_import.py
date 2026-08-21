from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path


class PackageImportContractTests(unittest.TestCase):
    def test_package_imports_from_src_tree(self):
        repo_root = Path(__file__).resolve().parents[1]
        src = repo_root / "src"
        self.assertTrue(src.is_dir(), "src directory is missing")

        sys.path.insert(0, str(src))
        try:
            module = importlib.import_module("elara_x_nrlmsis")
        finally:
            sys.path.pop(0)

        self.assertIsNotNone(module)

    def test_expected_placeholder_modules_exist(self):
        repo_root = Path(__file__).resolve().parents[1]
        package = repo_root / "src" / "elara_x_nrlmsis"
        expected = {
            "__init__.py",
            "constants.py",
            "utilities.py",
            "parameters.py",
            "horizontal.py",
            "temperature.py",
            "density.py",
            "model.py",
            "legacy_interface.py",
        }
        present = {p.name for p in package.glob("*.py")}
        self.assertTrue(expected.issubset(present))


if __name__ == "__main__":
    unittest.main()
