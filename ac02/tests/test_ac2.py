from BlogMock import BlogMock
import pytest

@pytest.fixture
def blogInstance():
    instance = BlogMock()
    return instance

def test_posts(blogInstance):
    assert len(blogInstance.get_posts()) == 100 

def test_posts_by_user_id_7(blogInstance):
    assert len(blogInstance.get_post_by_user_id(9)) == 10

def test_posts_by_user_id_1(blogInstance):
    assert blogInstance.get_post_by_user_id(1)[0]['userId'] == 1

def test_posts_by_user_id_3_title(blogInstance):
    assert blogInstance.get_post_by_user_id(3)[0]['title'] == 'asperiores ea ipsam voluptatibus modi minima quia sint'