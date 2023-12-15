import numpy as np


def E(x: np.array, y: np.array, n: int = 3, mu: int = 1) -> np.array:
    """Green function E(x,y) as described in Hsiao and Wendland 2008 (p.64)

    Args:
        x  (np.array): vector x
        y  (np.array): vector y
        n  (int): dim of vectors
        mu (int): dynamic viscosity of the fluid

    Returns:
        np.array: result of green function (associated with velocity)
    """
    r = np.linalg.norm(x - y)
    if n == 2:
        gamma = -np.log(r)
    elif n == 3:
        gamma = 1 / r
    return (
        1
        / (4 * (n - 1) * np.pi * mu)
        * (np.identity(n) * gamma + np.outer(x - y, x - y) / r**n)
    )


def Q(x: np.array, y: np.array, n: int = 3, mu: int = 1) -> np.array:
    """Green function Q(x,y) as described in Hsiao and Wendland 2008 (p.64)

    Args:
        x  (np.array): vector x
        y  (np.array): vector y
        n  (int): dim of vectors
        mu (int): dynamic viscosity of the fluid

    Returns:
        np.array: result of green function (associated with pressure)
    """
    if n == 2:
        return 1 / (2 * (n - 1) * np.pi) * 1 / (x - y)
    elif n == 3:
        return 1 / (2 * (n - 1) * np.pi) * 1 / (np.linalg.norm(x - y) * (x - y))
