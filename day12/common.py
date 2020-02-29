from time import time


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def absolute_sum(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def as_list(self):
        return [self.x, self.y, self.z]


class Moon:
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.velocity = Vector(0, 0, 0)

    @staticmethod
    def get_velocity_summand(u1, u2):
        return max(min(u2 - u1, 1), -1)

    def update_position(self):
        self.position.add(self.velocity)

    def update_velocity(self, other):
        x_increment = Moon.get_velocity_summand(self.position.x, other.position.x)
        y_increment = Moon.get_velocity_summand(self.position.y, other.position.y)
        z_increment = Moon.get_velocity_summand(self.position.z, other.position.z)
        self.velocity.add(Vector(x_increment, y_increment, z_increment))

    def potential_energy(self):
        return self.position.absolute_sum()

    def kinetic_energy(self):
        return self.velocity.absolute_sum()

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


def get_input(file_name):
    with open(file_name, 'r') as f:
        moons = []
        for i, line in enumerate(f.readlines()):
            split = line.strip().split(',')
            x = float(split[0].split('=')[1])
            y = float(split[1].split('=')[1])
            z = float(split[2].split('=')[1][:-1])
            m = Moon(i, Vector(x, y, z))
            moons.append(m)
        return moons


def update_velocity(moons):
    for m1 in moons:
        for m2 in moons:
            if m1 == m2:
                continue
            m1.update_velocity(m2)


def update_position(moons):
    for m in moons:
        m.update_position()


def time_step(moons):
    update_velocity(moons)
    update_position(moons)


def simulate_motion(moons, n_steps=1000):
    for i in range(n_steps):
        time_step(moons)


def calculate_system_energy(moons):
    energy = 0
    for m in moons:
        energy += m.total_energy()
    return energy
