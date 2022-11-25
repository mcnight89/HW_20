from unittest.mock import MagicMock
import pytest

from demostration_solution.dao.model.director import Director
from demostration_solution.dao.model.genre import Genre
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.dao.model.movie import Movie
from demostration_solution.service.movie import MovieService


@pytest.fixture
def movie_dao_fixture():
    movie_dao = MovieDAO(None)

    d1 = Director(id=1, name="d1")
    d2 = Director(id=2, name="d2")
    g1 = Genre(id=1, name="g1")
    g2 = Genre(id=2, name="g2")

    movie1 = Movie(
        id=1,
        title="asd",
        description="asad",
        trailer="asdasda",
        year=2022,
        rating=9.9,
        genre=g1,
        director=d1,
        genre_id=11,
        director_id=11

    )
    movie2 = Movie(
        id=2,
        title="asdd",
        description="asads",
        trailer="asda",
        year=2022,
        rating=9.9,
        genre=g2,
        director=d2,
        genre_id=11,
        director_id=11

    )

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) == 2

    def test_create(self):
        movie_data = {
            "description": "Slasher",
            "rating": 9.0,
            "id": 3,
            "trailer": "Slasher",
            "year": 2022,
            "title": "Slasher"
        }

        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_update(self):
        movie_data = {
            "description": "Slasher",
            "rating": 9.0,
            "id": 3,
            "trailer": "Slasher",
            "year": 2022,
            "title": "Slasher"
        }
        self.movie_service.update(movie_data)

    def test_delete(self):
        self.movie_service.delete(1)
