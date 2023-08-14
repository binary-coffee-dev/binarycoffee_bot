from abc import abstractmethod


class SocialAdapter:
    @abstractmethod
    def post(self, msg):
        pass
