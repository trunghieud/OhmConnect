from app_main import app
from tests import OhmTestCase


class CommunityTest(OhmTestCase):
    
    def test_community_api(self):
        with app.test_client() as c:
            response = c.get('/community')
            assert "Devanshi Shah" not in response.data
            assert "Justin Bieber" in response.data
