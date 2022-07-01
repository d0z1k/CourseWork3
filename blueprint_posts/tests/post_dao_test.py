import pytest as pytest

from blueprint_posts.dao.post import Post
from blueprint_posts.dao.post_dao import PostDAO


def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]

    for field in fields:
        assert hasattr(post, field), f"Нет поля {field}"


def get_by_pk_types(post_dao):
    post = post_dao.get_by_pk(1)
    assert type(post) == Post, "incorrect type for result single item"


class TestPostDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO("./blueprint_posts/tests/post_mock.json")
        return post_dao_instance

    # Получение всех

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, "incorrect type for result"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "incorrect type for result single item"

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_all()
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_all()
        correct_pks = {1, 2, 3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks, "Не совпадают полученные pk"

    # Получение по PK

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, "incorrect type for result single item"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_by_pk(1)
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_by_pk(991)
        assert post is None, "None для не существующего PK"

    @pytest.mark.parametrize("pk", [1, 2, 3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_by_pk(pk)
        assert post.pk == pk, f"Не верный РК для запроса поста с РК = {pk}"

    # Получение постов по строке

    def test_search_in_content_types(self, post_dao):
        posts = post_dao.search_in_content("ага")
        assert type(posts) == list, "incorrect type for result"

        post = post_dao.get_all()[0]
        assert type(post) == Post, "incorrect type for result single item"

    def test_search_in_content_fields(self, post_dao):
        posts = post_dao.search_in_content("dfgrgddwwrefg")
        assert posts == [], "Пустой список для несуществующей строки"

    @pytest.mark.parametrize("s, expected_pks", [
        ("Ага", {1}),
        ("Вышел", {2}),
        ("на", {1, 2, 3})
    ])
    def test_search_in_content_results(self, post_dao, s, expected_pks):
        posts = post_dao.search_in_content(s)
        pks = set([post.pk for post in posts])
        assert pks == expected_pks, f"Не верный результат при поиске {s}"

    # получение постов по автору

    def test_get_by_pk_types(self, post_dao):
        post = post_dao.get_by_poster("hank")
        assert type(post) == list, "incorrect type for result"

        post = post_dao.get_by_poster()[0]
        assert type(post) == Post, "incorrect type for result single item"

    def test_get_by_pk_fields(self, post_dao):
        post = post_dao.get_by_poster("hank")
        check_fields(post)

    def test_get_by_pk_none(self, post_dao):
        post = post_dao.get_by_poster(991)
        assert post is None, "None для не существующего Name"

