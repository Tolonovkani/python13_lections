from views_mixins import *


class Post(CreadMixin, ReadMixing, UpdateMixin, DeletMixin, SaveMixin):
    pass


class Coment(CreadMixin, ReadMixing, DeletMixin, SaveMixin):
    pass



class Like(CreadMixin, ReadMixing, DeletMixin, SaveMixin):
    pass 