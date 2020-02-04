# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:11:39 2020

@author: 44773
"""

from Vectors import Vector

class MatrixException(Exception):
    """
    Matrix Exception Base Class
    """
    pass

class MatrixTypeException(MatrixException):
    """
    raised if a Matrix is created of the wrong type
    """

class Matrix():
    """
        a Matrix is a 2 dimensional collection of numbers. 
        
        in this example I'll be listing them as lists of lists
    """
    
    def __init__(self, *args):
        """
            Creates a new Matrix with the lists/tuples passed into the arguments
            
            Will raise errors if type args is not of tuple or list containing
            only ints and floats.
        """
        self.setup_matrix(*args)
        
    def __call__(self):
        pass
    
    def __repr__(self):
        return f'm{self.entries}'
    
    def __str__(self):
        new_line = '\n\t'
        return 'm: [\n\t' + new_line.join({f'v{m}' for m in self.entries}) + '\n   ]'
    
    def __getitem__(self, items):
        return items 
    
    def __iter__(self):
        self.n = 0
        return self
        
    def __next__(self):
        if self.n < len(self):
            result = self.entries[self.n]
            self.n += 1
            return result
        raise StopIteration
        
    def __len__(self):
        return len(self.entries)
        
    def setup_matrix(self, *args):
        self._columns = len(args[0])
        self._rows = len(args)
        if all(type(arg) in [list, tuple] and len(arg) == self._columns \
               for arg in args):
            if all(type(m) in [int, float] for m in Matrix._flatten(args)):
                self.entries = [arg for arg in args]
            else: 
                raise MatrixTypeException(f'{type(args)}: incorrect type found')
        else:
            raise MatrixTypeException(f'{type(args)}: incorrect type found')
    
    def overwrite(self, matrix):
        self.setup_matrix(*matrix.entries)
    
    def get_shape(self):
        return Matrix._shape_of(self)
        
    def get_row(self, row):
        """
        returns the specified row of matrix as a Vector
        """
        return Matrix._get_row(self, row)
    
    def get_number_of_rows(self):
        return Matrix._get_number_of_rows(self)
    
    def get_column(self, column):
        """
        returns the specified column of matrix as a Vector
        """
        return Matrix._get_column(self, column)
    
    def get_number_of_columns(self):
        return Matrix._get_number_of_columns(self)
    
    def transpose(self):
        t = Matrix._transpose_matrix(self)
        return self.overwrite(t)
    
    @classmethod
    def _create_identity_matrix(cls, number):
        return Matrix._make_matrix(number, number, lambda i, j: 1 if i == j else 0)
        
    @classmethod
    def _make_matrix(cls, num_rows, num_columns, builder_function):
        """
        creates a new matrix using a different methodology
        
        this method has been set as a class method to keep it as an available
        option but not to complicate the core of the package
        """
        return cls(*[[builder_function(i, j) \
                     for j in range(num_columns)] \
                     for i in range(num_rows)])
    
    @classmethod
    def _transpose_matrix(cls, matrix):
        a = []
        for i in range(matrix.get_number_of_columns()):
            a.append([new[i] for new in matrix.entries])
        return cls(*a)
    
    @staticmethod
    def _get_row(matrix, row):
        return Vector(*matrix.entries[row])
    
    @staticmethod
    def _get_column(matrix, column):
        return Vector(*[m[column] for m in matrix])
    
    @staticmethod
    def _get_number_of_rows(matrix):
        return matrix._rows
    
    @staticmethod
    def _get_number_of_columns(matrix):
        return matrix._columns
    
    @staticmethod
    def _shape_of(matrix):
        return matrix._rows, matrix._columns
    
    @staticmethod
    def _flatten(args):
        a = list()
        {a.extend(arg) for arg in args}
        return a