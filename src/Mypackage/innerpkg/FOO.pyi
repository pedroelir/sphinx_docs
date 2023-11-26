from typing import Dict


class Foo:
    def get_something(self, some: int, thing: str) -> Dict[list]:
        """Get something

        :param some: Some thing
        :type some: int
        :param thing: Thing of some
        :type thing: str
        :return: Dictonary of some things
        :rtype: Dict[list]
        """
        ...

    def set_some(self, some: int) -> bool:
        """Set some things

        :param some: something
        :type some: int
        :return: True if correctly set
        :rtype: bool
        """
        ...
