import json
from json import JSONDecodeError

from blueprint_posts.dao.comment import Comment
from exceptions.exceptions import DataSourceError


class CommentDAO:
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

    def load_comments(self):
        """
        Возвращает список экземпляров
        :return: list_of_comments
        """

        comments_data = self.load_data()
        comments = [Comment(**comment_data) for comment_data in comments_data]

        return comments


cd = CommentDAO("../../data/comments.json")

print(cd.load_comments())
