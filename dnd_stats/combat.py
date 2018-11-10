from cmd import Cmd
from typing import List
import click
from entity import Entity


class InteractiveCombat(Cmd):
    """
    Interactive CLI used for a combat within DND.
    """

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.participants: List[Entity] = []
        self.turn = -1

    def do_exit(self, inp):
        """
         Exits the application
        :param inp: None
        """
        if self.config.verbose:
            click.echo('Exiting')
        exit(0)

    def do_add_character(self, inp: str):
        """
        Add a character to the combat
        :param inp: [Character Name] [Position x],[Position y]
        :return:
        """
        name, position = inp.split()
        pos_x, pos_y = position.split(',')
        self.participants.append(Entity(name, (int(pos_x), int(pos_y))))

    def do_list_all(self, inp):
        """
        Lists all characters participating in combat.
        :param inp:
        """
        for i in range(len(self.participants)):
            click.echo(f'{i}: {self.participants[i].name}')

    def do_set_initiative(self, inp: str):
        """
        Sets the initiative of a player
        :param inp:
        """
        player, initiative = inp.split()
        if player.isdigit():
            self.participants[int(player)].set_initiative(int(initiative))
        else:
            for entity in self.participants:
                if entity.name == player:
                    entity.set_initiative(initiative)
                    break

    def do_next(self):
        self.turn += 1
        player_number = self.turn % self.participants
        if self.config.verbose:
            click.echo(f'Round {player_number}, with player #{player_number} - {self.participants[player_number]} ')
