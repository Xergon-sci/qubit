from qubit.parsers.zmatrix import ZMatrix
from qubit.data import atomnumber
import numpy as np


class CoulombMatrix:


    def generate_coulomb_matrix(self, file):
        # parse the input z-matrix
        parser = ZMatrix()
        atoms, xyz = parser.load_zmatrix_from_file(file)

        # determine the lenght of the molecule and atomnumbers
        n = len(atoms)
        z = [atomnumber[atom] for atom in atoms]

        # create an empty matrix
        cm = np.zeros((n,n))

        # calculate the values and populate the array
        for i in range(n):
            for j in range(n):
                if i == j:
                    cm[i][j] = 0.5 * z[i] ** 2.4
                elif i < j:
                    cm[i][j] = z[i] * z[j] / (np.linalg.norm(np.array(xyz[i]) - np.array(xyz[j])))
                    cm[j][i] = cm[i][j]
        return cm

