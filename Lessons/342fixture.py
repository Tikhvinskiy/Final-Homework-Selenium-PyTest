import pytest


#
# @pytest.fixture(scope="class")
# def prepare_faces():
#     print("^_^", "\n")
#     yield
#     print(":3", "\n")
#
#
# @pytest.fixture()
# def very_important_fixture():
#     print(":)", "\n")
#
#
# @pytest.fixture(autouse=True)
# def print_smiling_faces():
#     print(":-Р", "\n")
#
#
# class TestPrintSmilingFaces():
#     def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
#         print(1)
#
#     def test_second_smiling_faces(self, prepare_faces):
#         print(2)

# 351
@pytest.mark.xfail(strict=True, reason="fuck")
def test_succeed():
    assert True


@pytest.mark.xfail()
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
