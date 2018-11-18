import pytest

from python_skeleton_project.greet_world import greet_world


@pytest.mark.parametrize("descriptor", [
    (None),
    ("Big")
])
def test_dummy(descriptor):
    greet_world(descriptor)
