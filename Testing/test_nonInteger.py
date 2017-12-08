import pytest
import menu
def test_nonInteger():
    	assert [46,0,178] == menu.menu_project("menu6.json")