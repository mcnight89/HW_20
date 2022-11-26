from unittest.mock import MagicMock
import pytest
from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture
def director_dao_fixture():
    director_dao = DirectorDAO(None)

    pupa = Director(id=1, name="pupa")
    lupa = Director(id=2, name="lupa")

    director_dao.get_one = MagicMock(return_value=lupa)
    director_dao.det_all = MagicMock(return_value=[pupa, lupa])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None
        assert director.name == "lupa"

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert len(directors) > 0

    def test_create(self):
        director_data = {
            "name": "Uppa"
        }

        director = self.director_service.create(director_data)
        assert director.id is not None

    def test_update(self):
        director_data = {
            "id": 1,
            "name": "UUppa"
        }
        self.director_service.update(director_data)

    def test_delete(self):
        self.director_service.delete(1)
