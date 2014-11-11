

class Problem(object):

    def __init__(self, id):
        self.id = id
        return super(Problem, self).__init__()


    def __str__(self):
        return self.__doc__

