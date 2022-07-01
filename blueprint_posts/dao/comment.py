class Comment:
    """
    Абстракция комментов
    """

    def __init__(self, pk, post_pk, commenter_name, comment):
        self.pk = pk
        self.post_pk = post_pk
        self.commenter_name = commenter_name
        self.comment = comment

    def __repr__(self):

        return f"Comment(" \
               f"{self.pk}," \
               f"{self.post_pk}," \
               f"{self.commenter_name}," \
               f"{self.comment}" \
               f")"

