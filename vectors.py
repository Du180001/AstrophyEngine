# Para representações de dimensões não definidas
class IVector():
    def __init__(self, dims:list): self._dims = dims
    def __repr__(self): return f"IVector({", ".join([f"dim{i}: {self._dims[i]}" for i in range(len(self._dims))])})"
    def __iter__(self): 
        for dim in self._dims: yield dim

    @property
    def dims(self): return self._dims

    def __add__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i + j for i, j in zip(self._dims, other._dims)]
        else: return [i * j for i, j in zip(self, other)]
    def __radd__(self, other): self.__add__(other)

    def __mul__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i * j for i, j in zip(self._dims, other._dims)]
        else: return [i * j for i, j in zip(self, other)]
    def __rmul__(self, other): self.__mul__(other)

    def __sub__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i - j for i, j in zip(self._dims, other._dims)]
        else: return [i - j for i, j in zip(self, other)]
    def __rsub__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i - j for i, j in zip(other._dims, self._dims)]
        else: return [i - j for i, j in zip(other, self)]

    def __truediv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i / j for i, j in zip(self._dims, other._dims)]
        else: return [i / j for i, j in zip(self, other)]
    def __rtruediv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i / j for i, j in zip(other._dims, self._dims)]
        else: return [i / j for i, j in zip(other, self)]
    
    def __floordiv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i // j for i, j in zip(self._dims, other._dims)]
        else: return [i // j for i, j in zip(self, other)]
    def __rfloordiv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return [i // j for i, j in zip(other._dims, self._dims)]
        else: return [i // j for i, j in zip(other, self)]

    def dot_product(self, other:"IVector"|list[float]|tuple[float]) -> float:
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return sum((self.__mul__()).dims)

# Variações Finitas Específicas.

# Para representações simples e bidimensionais, como a tela onde a simulação é executada
class Vector2D(IVector):
    ...

# Para representações tridimensionais, como posição espaçial, escala espacial e momento (velocidade).
class Vector3D(IVector):
    ...

# Para representações complexas e quadridimensionais, como o conjunto espaço tempo ou sistemas que nescessitam de todos os três ao mesmo tempo.
class Vector4D(IVector):
    def __init__(self, x:float, y:float, z:float, t:float):
        self._x, self._y, self._z, self._t = x, y, z, t
    

print(IVector([3,2,3,1,3,2,4,5,2,2]))