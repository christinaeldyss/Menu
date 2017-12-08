import pytest
import menu
def test_noID():
    	assert [46, 0, 163] == menu.menu_project("menu3.json")