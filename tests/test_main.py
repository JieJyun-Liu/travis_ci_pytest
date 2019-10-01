import pytest
import main

def test_go():
	result = main.go()
	assert result == "Hello"
