import pytest
import menu
def test_emptyFile():
    	assert "This is invalid json. Try again." == menu.menu_project("menu5.json")