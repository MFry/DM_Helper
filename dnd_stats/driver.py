from cmd import Cmd


class Config:
    def __init__(self):
        self.verbose = False


class InteractiveInput(Cmd):

    def __init__(self, config):
        super().__init__()
        self.config = config

    def do_exit(self, inp):
        if self.config.verbose:
            print('Exiting.')
        exit(0)

    def add_attack(self, inp):
        pass
