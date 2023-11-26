from Mypackage.innerpkg.FOO import Foo


class Bar(Foo):
    def set_another(self, another: int) -> bool:
        """Set another things

        :param another: another thing
        :type another: int
        :return: True if correctly set
        :rtype: bool
        """
        ...
