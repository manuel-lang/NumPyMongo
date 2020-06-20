from bson.binary import Binary
import numpy as np
import pickle as pkl

def from1d(array: np.ndarray) -> list:
    """Converts a one-dimensional NumPy ndarray to a list object that can be stored in MongoDB

    Args:
        array (np.ndarray): one-dimensional ndarray

    Returns:
        list: list representation of the ndarray
    """
    return array.tolist()

def from2d(array: np.ndarray) -> Binary:
    """Converts a two-dimensional NumPy ndarray to a list object that can be stored in MongoDB

    Args:
        array (np.ndarray): two-dimensional ndarray

    Returns:
        Binary: pickled binary representation of the 2d ndarray
    """
    return Binary(pkl.dumps(array, protocol=2), subtype=128)

def to1d(list: list) -> np.ndarray:
    """Converts a list to a one-dimensional NumPy ndarray

    Args:
        list (list): list of numbers

    Returns:
        np.ndarray: ndarray representation of the list
    """
    return  np.fromiter(list)

def to2d(binary: Binary) -> np.ndarray:
    """Converts a pickled binary to a one-dimensional NumPy ndarray

    Args:
        binary (Binary): pickled binary

    Returns:
        np.ndarray: ndarray representation of the pickled binary
    """
    return pkl.loads(binary)

def fromFloat(num: np.float) -> float:
    """Converts a NumPy float that it can be stored in MongoDB

    Args:
        num (np.float): NumPy float value

    Returns:
        float: casted value
    """
    return float(num)

def fromInt(num: np.int) -> int:
    """Converts a NumPy int that it can be stored in MongoDB

    Args:
        num (np.int): NumPy int value

    Returns:
        int: casted value
    """
    return int(num)
