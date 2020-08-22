from abc import abstractmethod, ABC

class Band():
    members = []

    def __init__(self, name, band):
        self.band = band
        self.name = name
        Band.members.append(self.name)

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def play_solos(mem):
        for member in mem.members:
            return f'Super {member.instrument} solo from {member}'

    @classmethod
    def create_from_data(mem, data):
        for musician in data:
          if musician['instrument'] == 'Guitar':
              mem.members.append(
                  Guitarist(musician['name'], musician['instrument']))
              continue

          elif musician['instrument'] == 'Bass':
              mem.members.append(Bassist(musician['name'], musician['instrument']))
              continue

          elif musician['instrument'] == 'Drums':
              mem.members.append(Drummer(musician['name'], musician['instrument']))
              continue

        @classmethod
        def to_list(mem):
            return mem.members

class Musician(Band):
    musician_type = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_members(mem):
        return mem.musician_type

class Guitarist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'tun tun ttattatun'

    def get_instrument(self):
        return 'guitar'

class Bassist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'basssss basss booommb'

    def get_instrument(self):
        return 'Bass'

class Drummer(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'badum badum brumm badum brumm'

    def get_instrument(self):
        return 'Drums'

if __name__ == "__main__":
    jwan = Guitarist('Jwan', 'Guitarist')
    sia = Bassist('Sia', 'Bassist')
    mikel = Drummer('Mikel', 'Drummer')
    print(jwan)
    print(jwan.get_instrument())
    print(jwan.play_solo())
    print(sia)
    print(sia.get_instrument())
    print(sia.play_solo())
    print(mikel)
    print(mikel.get_instrument())
    print(mikel.play_solo())
