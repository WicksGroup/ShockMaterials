"""
Contains material properties that are interesting for shock
"""

class Material:
    """
    General class for materials
    """
    def __init__(self, ambient_density, unit_cell_shape):
        """
        ambient_density: float = the ambient density of the material in g/cm^3
        """
        self.ambient_density = ambient_density
        self.unit_cell_shape = unit_cell_shape

    def get_hugoniot(self):
        pass

Diamond = Material(ambient_density = 3.43)