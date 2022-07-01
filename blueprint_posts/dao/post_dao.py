import json
from json import JSONDecodeError

from blueprint_posts.dao.post import Post
from exceptions.exceptions import DataSourceError


class PostDAO:
    """
    Класс работы с постами(загружает\ищет)
    """

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """
        Загружает данные из Json в список словарей
        :return: posts_data
        """

        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удается получить данные из {self.path}')

        return posts_data

    def load_posts(self):
        """
        Возвращает список экземпляров
        :return: list_of_posts
        """

        posts_data = self.load_data()

        list_of_posts = [Post(**post_data) for post_data in posts_data]
        return list_of_posts

    def get_all(self):
        """
        Загружает все посты
        :return: posts
        """

        posts = self.load_posts()
        return posts

    def get_by_pk(self, pk):
        """
        получает пост по PK
        :param pk:
        :return:post
        """

        if type(pk) != int:
            raise TypeError("pk должно быть числом")
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):
        """
        ищет посты по сабстрингу
        :param substring:
        :return:matching_posts
        """
        if type(substring) != str:
            raise TypeError("substring должно быть строкой")

        substring = str(substring)
        posts = self.load_posts()

        matching_posts = [post for post in posts if substring in post.content.lower()]

        return matching_posts

    def get_by_poster(self, user_name):
        """
        ищет посты по автору
        :param user_name:
        :return:matching_posts
        """

        if type(user_name) != str:
            raise TypeError("имя должно быть строкой")

        user_name = str(user_name).lower()
        posts = self.load_posts()

        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]

        return matching_posts




