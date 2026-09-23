import pytest
from pathlib import Path

PKG_DIR = Path(__file__).parents[1] / "workflow_packages/growth.launch_announcement"

def test_manifest_is_valid():
    manifest_path = PKG_DIR / "workflow.json"
    assert manifest_path.exists()
    
def test_entrypoint_exists():
    main_path = PKG_DIR / "main.py"
    assert main_path.exists()

