import pytest
from modules.world import Level
from modules.cockroach import Cockroach
from modules.items import Item

@pytest.fixture
def level():
    contents = []
    item = Item("exit", "The real exit")
    item.place((1,2))

    roach = Cockroach("roach", "a big green roach")
    roach.place((2,3))

    contents.append(item)
    contents.append(roach)
    return Level(contents, 4)

def test_level_accepts_a_list_of_contents_and_a_size(level):
    assert len(level.contents) == 2
    assert level.size == 4

def test_contents_at_coords_finds_no_contents_at_empty_coords(level):
    assert len(level.contents_at_coords((0,0))) == 0

def test_contents_at_coords_finds_contents_at_its_coords(level):
    results = level.contents_at_coords((2,3))
    assert len(results) == 1
    assert type(results[0]) is Cockroach

def test_get_by_name_returns_content_with_name(level):
    result = level.get_by_name("roach")
    assert result.name == "roach"

def test_get_by_name_returns_none_for_invalid_name(level):
    result = level.get_by_name("jabberwonky")
    assert result == None

def test_get_location_by_name_returns_just_coords(level):
    result = level.get_location_by_name("roach")
    assert result == (2,3)

