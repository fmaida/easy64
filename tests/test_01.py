import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from pytest import fixture, raises
import easy64

@fixture
def santron():
    my_path = os.path.dirname(os.path.realpath(__file__))
    my_path = os.path.join(my_path, "files")
    my_path = os.path.join(my_path, "santron.d64")
    return my_path

@fixture
def i_do_not_exists():
    my_path = os.path.dirname(os.path.realpath(__file__))
    my_path = os.path.join(my_path, "files")
    my_path = os.path.join(my_path, "foo.d64")
    return my_path

def test_recognizement_01(santron):
    gigetto = easy64.Image()
    gigetto.load(santron)
    assert gigetto.file is not None

def test_file_exists_01(santron):
    gigetto = easy64.Image()
    gigetto.load(santron)

def test_file_do_not_exists_01(i_do_not_exists):
    with raises(FileNotFoundError) as ex:
        gigetto = easy64.Image()
        gigetto.load(i_do_not_exists)

def test_write_cjm_01(santron):
    gigetto = easy64.Image(filename=santron)
    my_path = gigetto.save_cjm()
    # breakpoint()
    assert os.path.exists(my_path)
