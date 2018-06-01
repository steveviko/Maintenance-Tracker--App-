import os
import tempfile

import pytest,Flask


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data
@pytest.fixture
def client():
    db_fd, flask.app.config['DATABASE'] = tempfile.mkstemp()
    flask.app.config['TESTING'] = True
    client = flask.app.test_client()

    with flask.app.app_context():
        flask.init_db()

    yield client

    os.close(db_fd)
    os.unlink(flask.app.config['DATABASE'])
if __name__ == '__main__':
    app.run(debug=True)
def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data