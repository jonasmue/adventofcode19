def get_input(file_name):
    with open(file_name, 'r') as f:
        return f.readlines()


def build_orbit_dict(orbit_list):
    orbit_dict = {}
    for orbit in orbit_list:
        orbits = orbit.split(')')
        orbitee = orbits[0].strip()
        orbiter = orbits[1].strip()
        orbit_dict[orbiter] = orbitee

    return orbit_dict
