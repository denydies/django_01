import pytest

from account.models import User

from main.models import Post, Category, ContactUs


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to DB for all tests
    """


@pytest.fixture(scope='function')
def usr_fixt():
    user = User.objects.create()
    yield user


@pytest.fixture(scope='function')
def post_fixt():
    post = Post.objects.create()
    yield post


@pytest.fixture(scope='function')
def category_fixt():
    category = Category.objects.create()
    yield category


@pytest.fixture(scope='function')
def contactus_fixt():
    contactus = ContactUs.objects.create()
    yield contactus
