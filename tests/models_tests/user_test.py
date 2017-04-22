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
        rows = User.get_recent(10)
        assert len(rows) == 3
        for row in rows:
            if row['user_id'] == 1:
                assert row['phones'] == ['+14086441234', '+14086445678']
                assert row['location'] == 'EUROPE'
            elif row['user_id'] == 2:
                assert row['phones'] == ['+14086551234']
                assert row['location'] is None
            elif row['user_id'] == 3:
                assert row['phones'] == []
                assert row['location'] == 'USA'
