from __future__ import annotations

import unittest
from pathlib import Path


FORBIDDEN_BASENAMES = {
    "msis2.1_test.F90",
    "msis2.1_test_in.txt",
    "msis2.1_test_ref_dp.txt",
    "msis21.parm",
    "msis_calc.F90",
    "msis_constants.F90",
    "msis_dfn.F90",
    "msis_gfn.F90",
    "msis_gtd8d.F90",
    "msis_init.F90",
    "msis_tfn.F90",
    "msis_utils.F90",
}

FORTRAN_SUFFIXES = {".f", ".f90", ".for", ".f95"}


class RepositorySafetyContractTests(unittest.TestCase):
    def setUp(self):
        self.repo_root = Path(__file__).resolve().parents[1]

    def test_no_official_nrl_payload_basenames_are_present(self):
        hits = []
        for path in self.repo_root.rglob("*"):
            if ".git" in path.parts or not path.is_file():
                continue
            if path.name in FORBIDDEN_BASENAMES:
                hits.append(path.relative_to(self.repo_root).as_posix())
        self.assertEqual([], hits)

    def test_no_fortran_source_is_present(self):
        hits = []
        for path in self.repo_root.rglob("*"):
            if ".git" in path.parts or not path.is_file():
                continue
            if path.suffix.lower() in FORTRAN_SUFFIXES:
                hits.append(path.relative_to(self.repo_root).as_posix())
        self.assertEqual([], hits)

    def test_oracle_fixture_area_contains_governance_only(self):
        fixture_dir = self.repo_root / "tests" / "fixtures"
        self.assertTrue(fixture_dir.is_dir())
        allowed = {
            "README.md",
            "oracle_fixture_manifest.schema.json",
        }
        present = {
            p.name for p in fixture_dir.iterdir()
            if p.is_file()
        }
        self.assertEqual(allowed, present)


if __name__ == "__main__":
    unittest.main()
