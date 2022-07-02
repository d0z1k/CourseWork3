import pytest

import main


class TestApi:
    post_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    @pytest.fixture
    def app_instance(self):
        return main.app.test_client()

    # Все посты
    def test_all_posts_status(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200

    #Не верные ключи
    def test_all_posts_keys_status(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        list_of_posts = result.get_json()

        for post in list_of_posts:
            assert post.keys() == self.post_keys, "Не верные ключи у словаря"


    # Конкретный пост
    def test_single_post_status(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 200

    # Не существующий пост
    def test_non_existing_post_status(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert result.status_code == 404

    #Не верный ключ
    def test_single_post_has_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post = result.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys
