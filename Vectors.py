import math

class VectorException(Exception):
    """
    Vector Exception Base Class
    """
    pass

class VectorLengthException(VectorException):
    """
    raised if vectors supplied to argument are not found to be equal
    """
    
class VectorTypeException(VectorException):
    """
    raised if a vector is created of the wrong type
    """
    
class VectorAdditionError(VectorException):
    """
    raised if a vector addition fails
    """

class Vector():
    def __init__(self, *args):
        self.type = type(args[0])
        if all(type(arg) in Vector.allowed_types() for arg in args):
            self.indices = [arg for arg in args]
        else:
            raise VectorTypeException
            
        self.magnitude()
        self.sos()
        
    def __call__():
        pass

    def __add__(self, v):
        """
            Adds two vectors together
        """
        if len(v) != len(self):
            raise VectorLengthException("Vectors are of different Lengths")
        return Vector(*[v_index + w_index for v_index, w_index in zip(self, v)])
    
    def __sub__(self, v):
        """
        subtracts two vectors self and v
        """
        if len(v) != len(self):
            raise VectorLengthException("Vectors are of different Lengths")
        return Vector(*[v_index - w_index for v_index, w_index in zip(self, v)])
        
    def __mul__(self, multiplier):
        """
            multiplier can either be a scalar or another vector
            
            if multiplying by another vector it calls the dot of;
                    self * multiplier
        """
        if type(multiplier) is Vector:
            return Vector.dot_of_(self, multiplier)
        if type(multiplier) not in Vector.allowed_types(): 
            raise VectorTypeException("Please use an int or float for multiplication")
        return Vector.scalar_multiplication(self, multiplier)
        
    def __iter__(self):
        self.n = 0
        return self
        
    def __next__(self):
        if self.n < len(self):
            result = self.indices[self.n]
            self.n += 1
            return result
        raise StopIteration
    
    def __repr__(self) -> str:
        return f'v{self.indices}'
    
    def __len__(self) -> int:
        return len(self.indices)
    
    def __getitem__(self, items):
        return items
    
    def magnitude(self):
        self.v_magnitude = Vector.magnitude_of_(self)
        
    def sos(self):
        """
         short for sum of squares 
        """
        self.v_sos = Vector.sum_of_squares(self)
    
    @staticmethod
    def as_list(vector):
        return vector.indices
    
    @staticmethod
    def allowed_types():
        return [float, int]
    
    @staticmethod
    def sum_of_(vectors):
        if not vectors:
            raise VectorException("No vector list provided")
        
        v_length = len(vectors[0])
        if not all(len(v) == v_length for v in vectors):
            raise VectorLengthException("Vectors are of different Lengths")
        
        return Vector(*[sum(vector[i] for vector in vectors) for i in range(v_length)])
    
    @staticmethod
    def mean_of_(vectors):
        """
        Calculates the element-wise average of the vectors
        """
        n = len(vectors)
        return Vector.sum_of_(vectors) * (1/n)
    
    @staticmethod
    def scalar_multiplication(vector, scalar: float):
        return Vector(*[scalar * v_index for v_index in vector])
    
    @staticmethod
    def dot_of_(vector1, vector2) -> float:
        """
            Dot product of two vectors is seen as;
                (where v = vector1 and w = vector2)
            v_i * w_i + ... + v_n * w_n
            
            basically the sum of the indices multiplied by one another
        """
        if len(vector2) != len(vector1):
            raise VectorLengthException("Vectors are of different Lengths")
        return sum(v1_index * v2_index for v1_index, v2_index in zip(vector1, vector2))
    
    @staticmethod
    def sum_of_squares(vector) -> float:
        return vector * vector
    
    @staticmethod
    def magnitude_of_(vector) -> float:
        return math.sqrt(Vector.sum_of_squares(vector))
    
    @staticmethod
    def squared_distance(vector1, vector2) -> float:
        """
            The squared distance between two vectors calculates 
            (v1_index - v2_index) ** 2 + ... + (v1_n - v2_n) ** 2
        """
        return Vector.sum_of_squares(vector1 - vector2)
    
    @staticmethod
    def distance_between(vector1, vector2) -> float:
        return Vector.magnitude_of_(vector1 - vector2)
    # Parallel vectors are multiples of one another
    
    
        
    
    
    
