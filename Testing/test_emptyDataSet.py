import pytest
import menu
def test_emptyDataSet():
    	assert "No data is available." == menu.menu_project("menu4.json")