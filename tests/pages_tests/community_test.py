from app_main import app
from tests import OhmTestCase


class CommunityTest(OhmTestCase):
    def test_get_five(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "Elvis Presley" in response.data
            assert "Chuck Norris" in response.data
            assert "Justin Bieber" in response.data
