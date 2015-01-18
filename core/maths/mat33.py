"""Kraken - maths.matrix module.

Classes:
Mat33 -- Matrix 3 transform object.
"""

from math_object import MathObject
from kraken.core.objects.kraken_system import KrakenSystem as KS
from vec3 import Vec3


class Mat33(MathObject):
    """3x3 Matrix object."""

    def __init__(self, row0=None, row1=None, row2=None):
        """Initialize and set values in the 3x3 matrix."""

        super(Mat33, self).__init__()

        if row0 is not None and self.getTypeName(row0) == 'Mat33':
            self.rtval = row0
        else:
            self.rtval = KS.inst().rtVal('Mat33')
            if row0 is not None and row1 is not None and row2 is not None:
                self.setRows(row0, row1, row2)


    def __str__(self):
        """Return a string representation of the 3x3 matrix."""

        return "Mat33(" + str(self.row0) + "," + str(self.row1) + "," + str(self.row2) + ")"

    @property
    def row0(self):
        """Gets row 0 of this matrix.

        Return:
        Vec3, row 0 vector.

        """

        return Vec3(self.rtval.row0)


    @row0.setter
    def row0(self, value):
        """Sets row 0 as the input vector.

        Arguments:
        value -- Vec3, vector to set row 0 as.

        Return:
        True if successful.

        """

        self.rtval.row0 = KS.inst().rtVal('Scalar', value)

        return True


    @property
    def row1(self):
        """Gets row 1 of this matrix.

        Return:
        Vec3, row 1 vector.

        """

        return Vec3(self.rtval.row1)


    @row1.setter
    def row1(self, value):
        """Sets row 1 as the input vector.

        Arguments:
        value -- Vec3, vector to set row 1 as.

        Return:
        True if successful.

        """

        self.rtval.row1 = KS.inst().rtVal('Scalar', value)

        return True


    @property
    def row2(self):
        """Gets row 2 of this matrix.

        Return:
        Vec3, row 2 vector.

        """

        return Vec3(self.rtval.row2)


    @row2.setter
    def row2(self, value):
        """Sets row 2 as the input vector.

        Arguments:
        value -- Vec3, vector to set row 2 as.

        Return:
        True if successful.

        """

        self.rtval.row2 = KS.inst().rtVal('Scalar', value)

        return True

    def clone(self):
        """Returns a clone of the Mat33.

        Return:
        The cloned Mat33

        """

        mat33 = Mat33();
        mat33.row0 = self.row0.clone();
        mat33.row1 = self.row1.clone();
        mat33.row2 = self.row2.clone();
        return mat33

    def setRows(self, row0, row1, row2):
        """Setter from vectors, row-wise.

        Arguments:
        row0 -- Vec3, vector to use to set row 0.
        row1 -- Vec3, vector to use to set row 1.
        row2 -- Vec3, vector to use to set row 2.

        Return:
        True if successful.

        """

        self.rtval.setRows('', KS.inst().rtVal('Vec3', row0), KS.inst().rtVal('Vec3', row1), KS.inst().rtVal('Vec3', row2))

        return True


    def setColumns(self, col0, col1, col2):
        """Setter from vectors, column-wise.

        Arguments:
        col0 -- Vec3, vector to use to set column 0.
        col1 -- Vec3, vector to use to set column 1.
        col2 -- Vec3, vector to use to set column 2.

        Return:
        True if successful.

        """

        self.rtval.setColumns('', KS.inst().rtVal('Vec3', col0), KS.inst().rtVal('Vec3', col1), KS.inst().rtVal('Vec3', col2))

        return True


    def setNull(self):
        """Setting all components of the matrix to 0.0.

        Return:
        True if successful.

        """

        self.rtval.setNull('')

        return True


    def setIdentity(self):
        """Sets this matrix to the identity matrix.

        Return:
        True if successful.

        """

        self.rtval.setIdentity('')

        return True


    def setDiagonal(self, v):
        """Sets the diagonal components of this matrix to a scalar.

        Arguments:
        v -- Scalar, value to set diagonals to.

        Return:
        True if successful.

        """

        self.rtval.setDiagonal('', KS.inst().rtVal('Scalar', v))

        return True


    def setDiagonal(self, v):
        """Sets the diagonal components of this matrix to the components of a
        vector.

        Arguments:
        v -- Vec3, vector to set diagonals to.

        Return:
        True if successful.

        """

        self.rtval.setDiagonal('', KS.inst().rtVal('Vec3', v))

        return True


    def equal(self, other):
        """Checks equality of this Matrix33 with another.

        Arguments:
        other -- Mat33, other matrix to check equality with.

        Return:
        True if equal.

        """

        return self.rtval.equal('Boolean', KS.inst().rtVal('Mat33', other))


    def almostEqual(self, other, precision=None):
        """Checks almost equality of this Matrix33 with another.

        Arguments:
        other -- Mat33, other matrix to check equality with.
        precision -- Scalar, precision value.

        Return:
        True if almost equal.

        """
        if precision is not None:
            return self.rtval.almostEqual('Boolean', KS.inst().rtVal('Mat33', other), KS.inst().rtVal('Scalar', precision))
        else:
            return self.rtval.almostEqual('Boolean', KS.inst().rtVal('Mat33', other))


    # # Equals operator
    # def Boolean == (Mat33 a, Mat33 b):


    # # Not equals operator
    # def Boolean != (Mat33 a, Mat33 b):


    # # Returns the addition of two matrices
    # def Mat33 + (Mat33 a, Mat33 b):


    # # Adds another matrix to this one
    # def  += (Mat33 other):


    # # Returns the subtraction of two matrices
    # def Mat33 - (Mat33 a, Mat33 b):


    # # Subtracts another matrix from this one
    # def  -= (Mat33 other):


    # # Returns the product of two matrices
    # function Mat33 * (Mat33 left, Mat33 right):


    # # Returns the product of a matrix and a Vec3
    # def Vec3 * (Mat33 mat33, Vec3 vec3):


    # # Returns the product of a matrix and a scalar
    # def Mat33 * (Mat33 mat33, Scalar s):


    # # Returns the product of a scalar and a matrix
    # def Mat33 * (Scalar s, Mat33 mat33):


    # # Multiplies this matrix with another one
    # def  *= (Mat33 other):


    # # Multiplies this matrix with a scalar
    # def  *= (Scalar other):


    # # Returns the division of a matrix and a scalar
    # def Mat33 / (Mat33 mat33, Scalar s):


    # # Divides this matrix by a scalar
    # def  /= (Scalar other):


    def add(self, other):
        """Overload method for the add operator.

        Arguments:
        other -- Mat33, other matrix to add to this one.

        Return:
        Mat33, new Mat33 of the sum of the two Mat33's.

        """

        return Mat33(self.rtval.add('Mat33', KS.inst().rtVal('Mat33', other)))


    def subtract(self, other):
        """Overload method for the subtract operator.

        Arguments:
        other -- Mat33, other matrix to subtract from this one.

        Return:
        Mat33, new Mat33 of the difference of the two Mat33's.

        """

        return Mat33(self.rtval.subtract('Mat33', KS.inst().rtVal('Mat33', other)))


    def multiply(self, other):
        """Overload method for the multiply operator.

        Arguments:
        other -- Mat33, other matrix to multiply from this one.

        Return:
        Mat33, new Mat33 of the product of the two Mat33's.

        """

        return Mat33(self.rtval.multiply('Mat33', KS.inst().rtVal('Mat33', other)))


    def multiplyScalar(self, other):
        """Product of this matrix and a scalar.

        Arguments:
        other -- Scalar, scalar value to multiply this matrix by.

        Return:
        Mat33, product of the multiplication of the scalar and this matrix.

        """

        return Mat33(self.rtval.multiplyScalar('Mat33', KS.inst().rtVal('Scalar', other)))


    def multiplyVector(self, other):
        """Returns the product of this matrix and a vector.

        Arguments:
        other -- Vec3, vector to multiply this matrix by.

        Return:
        Vec3, product of the multiplication of the Vec3 and this matrix.

        """

        return Vec3(self.rtval.multiplyVector('Vec3', KS.inst().rtVal('Vec3', other)))


    def divideScalar(self, other):
        """Divides this matrix and a scalar.

        Arguments:
        other -- Scalar, value to divide this matrix by.

        Return:
        Mat33, quotient of the division of the matrix by the scalar.

        """

        return Mat33(self.rtval.divideScalar('Mat33', other))


    def determinant(self):
        """Gets the determinant of this matrix.

        Return:
        Scalar, determinant of this matrix.

        """

        return self.rtval.determinant('Scalar')


    def adjoint(self):
        """Gets the adjoint matrix of this matrix.

        Return:
        Mat33, adjoint of this matrix.

        """

        return Mat33(self.rtval.adjoint('Mat33'))


    def inverse(self):
        """Get the inverse matrix of this matrix.

        Return:
        Mat33, inverse of this matrix.

        """

        return Mat33(self.rtval.inverse('Mat33'))


    def inverse_safe(self):
        """Get the inverse matrix of this matrix, always checking the
        determinant value.

        Return:
        Mat33, safe inverse of this matrix.

        """

        return Mat33(self.rtval.inverse_safe('Mat33'))


    def transpose(self):
        """Get the transposed matrix of this matrix.

        Return:
        Mat33, transpose of this matrix.

        """

        return Mat33(self.rtval.transpose('Mat33'))