from abc import abstractmethod, ABC

class Band(ABC):
    members = []

    def __init__(self, name, band):
        self.band = band
        self.name = name
        Band.members.append(self)

    def __str__(self):
        return f'"Name: "{self.name}, "Band: "{self.band}'

    def __repr__(self):
        return f'"Name: "{self.name}, "Band: "{self.band}'

    def play_solos(self):
        for member in self.members:
            return f'Super {member.name} solo from {member}'

    @classmethod
    def create_from_data(self, data):
        for musician in data:
          if musician['instrument'] == 'Guitar':
              self.members.append(
                  Guitarist(musician['name'], musician['instrument']))
              continue

          elif musician['instrument'] == 'Bass':
              self.members.append(Bassist(musician['name'], musician['instrument']))
              continue

          elif musician['instrument'] == 'Drums':
              self.members.append(Drummer(musician['name'], musician['instrument']))
              continue

        @classmethod
        def to_list(self):
            return self.members

class Musician(Band):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Hello all, my name is {self.name}'


    musician_type = []

    @classmethod
    def get_members(self):
        return self.musician_type

class Guitarist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def __str__(self):
        return f"I'm {self.name}, and I play Guitar"

    def __repr__(self):
        return f"The guitariest is: {self.name}"

    def play_solo(self):
        return 'tun tun ttattatun'

    def get_instrument(self):
        return 'guitar'

class Bassist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def __str__(self):
        return f"I'm {self.name}, and I play Bass"

    def __repr__(self):
        return f"The guitariest is: {self.name}"

    def play_solo(self):
        return 'basssss basss booommb'

    def get_instrument(self):
        return 'Bass'

class Drummer(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def __str__(self):
        return f"I'm {self.name}, and I play Drums"

    def __repr__(self):
        return f"The guitariest is: {self.name}"

    def play_solo(self):
        return 'badum badum brumm badum brumm'

    def get_instrument(self):
        return 'Drums'

if __name__ == "__main__":
    jwan = Guitarist('Jwan', 'Guitarist')
    sia = Bassist('Sia', 'Bassist')
    mikel = Drummer('Mikel', 'Drummer')
    print(jwan.__str__())
    print(jwan.get_instrument())
    print(jwan.play_solo())
    # print(sia)
    # print(sia.get_instrument())
    # print(sia.play_solo())
    # print(mikel)
    # print(mikel.get_instrument())
    # print(mikel.play_solo())
