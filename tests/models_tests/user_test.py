from tests import OhmTestCase
from models import User


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []

    def test_get_recent(self):
        rows = User.get_recent(1)
        assert len(rows) == 1
        rows = User.get_recent(3)
        assert len(rows) == 3
