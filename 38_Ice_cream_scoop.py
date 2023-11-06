class Scoop:
    def __init__(self, flavor: str):
        self.flavor = flavor

    def create_scoops(self):
        scoops = [Scoop('chocolate'),
                  Scoop('vanilla'),
                  Scoop('persimmon')]
        for scoop in scoops:
            print(scoop.flavor)


x = Scoop('Skonis')
x.create_scoops()
