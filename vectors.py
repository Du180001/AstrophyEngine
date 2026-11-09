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
        if isinstance(other, IVector): return IVector([i + j for i, j in zip(self._dims, other._dims)])
        else: return IVector([i + j for i, j in zip(self, other)])
    def __radd__(self, other): self.__add__(other)

    def __mul__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return IVector([i * j for i, j in zip(self._dims, other._dims)])
        else: return IVector([i * j for i, j in zip(self, other)])
    def __rmul__(self, other): self.__mul__(other)

    def __sub__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return IVector([i - j for i, j in zip(self._dims, other._dims)])
        else: return IVector([i - j for i, j in zip(self, other)])
    def __rsub__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return IVector([i - j for i, j in zip(other._dims, self._dims)])
        else: return [i - j for i, j in zip(other, self)]

    def __truediv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return IVector([i / j for i, j in zip(self._dims, other._dims)])
        else: return IVector([i / j for i, j in zip(self, other)])
    def __rtruediv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return IVector([i / j for i, j in zip(other._dims, self._dims)])
        else: return [i / j for i, j in zip(other, self)]
    
    def __floordiv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return IVector([i // j for i, j in zip(self._dims, other._dims)])
        else: return IVector([i // j for i, j in zip(self, other)])
    def __rfloordiv__(self, other) -> "IVector":
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return IVector([i // j for i, j in zip(other._dims, self._dims)])
        else: return IVector([i // j for i, j in zip(other, self)])

    def dot_product(self, other:"IVector"|list[float]|tuple[float]) -> float:
        if not isinstance(other, (tuple, list, IVector)): return NotImplemented
        if isinstance(other, IVector): return sum((self.__mul__()).dims)

# Variações Finitas Específicas.

# Para representações simples e bidimensionais, como a tela onde a simulação é executada
class Vector2D():
    def __init__(self, x:float, y:float): self._x, self._y, self._z = x, y
    def __repr__(self): return f"Vector2D(x: {self._x,}, y: {self.y})"
    def __iter__(self):
        for dim in [self._x, self._y]: yield dim

    def __add__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(self.x + other.x, self.y + other.y)
        if len(other) >= 2: return Vector2D(self.x + other[0], self.y + other[1])
        else: return NotImplemented
    def __radd__(self, other): self.__add__(other)

    def __mul__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(self.x * other.x, self.y * other.y)
        if len(other) >= 2: return Vector2D(self.x * other[0], self.y * other[1])
        else: return NotImplemented
    def __rmul__(self, other): self.__mul__(other)

    def __sub__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(self.x - other.x, self.y - other.y)
        if len(other) >= 2: return Vector2D(self.x - other[0], self.y - other[1])
        else: return NotImplemented
    def __rsub__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(other.x - self.x, other.y - self.y)
        if len(other) >= 2: return Vector2D(other[0] - self.x, other[1] - self.y)
        else: return NotImplemented

    def __truediv__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(self.x / other.x, self.y / other.y)
        if len(other) >= 2: return Vector2D(self.x / other[0], self.y / other[1])
        else: return NotImplemented
    def __rtruediv__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(other.x / self.x, other.y / self.y)
        if len(other) >= 2: return Vector2D(other[0] / self.x, other[1] / self.y)
        else: return NotImplemented

    def __floordiv__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(self.x // other.x, self.y // other.y)
        if len(other) >= 2: return Vector2D(self.x // other[0], self.y // other[1])
        else: return NotImplemented
    def __rfloordiv__(self, other):
        if not isinstance(other, (Vector2D, list, tuple)): return NotImplemented
        if isinstance(other, Vector2D): return Vector2D(other.x // self.x, other.y // self.y)
        if len(other) >= 2: return Vector2D(other[0] // self.x, other[1] // self.y)
        else: return NotImplemented
        

# Para representações tridimensionais, como posição espaçial, escala espacial e momento (velocidade).
class Vector3D():
    def __init__(self, x:float, y:float, z:float): self._x, self._y, self._z = x, y, 
    def __repr__(self): return f"Vector3D(x: {self._x,}, y: {self.y}, z: {self.z})"
    def __iter__(self):
        for dim in [self._x, self._y, self._z]: yield dim

    def __add__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        if len(other) >= 3: return Vector3D(self.x + other[0], self.y + other[1], self.z + other[2])
        else: return NotImplemented
    def __radd__(self, other): self.__add__(other)

    def __mul__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
        if len(other) >= 3: return Vector3D(self.x * other[0], self.y * other[1], self.z * other[2])
        else: return NotImplemented
    def __rmul__(self, other): self.__mul__(other)

    def __sub__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        if len(other) >= 3: return Vector3D(self.x - other[0], self.y - other[1], self.z - other[2])
        else: return NotImplemented
    def __rsub__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(other.x - self.x, other.y - self.y)
        if len(other) >= 3: return Vector3D(other[0] - self.x, other[1] - self.y)
        else: return NotImplemented

    def __truediv__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(self.x / other.x, self.y / other.y, self.z / other.z)
        if len(other) >= 3: return Vector3D(self.x / other[0], self.y / other[1], self.z / other[2])
        else: return NotImplemented
    def __rtruediv__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(other.x / self.x, other.y / self.y, other.z / self.z)
        if len(other) >= 3: return Vector3D(other[0] / self.x, other[1] / self.y, other[2] / self.z)
        else: return NotImplemented

    def __floordiv__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(self.x // other.x, self.y // other.y, self.z // other[2])
        if len(other) >= 3: return Vector3D(self.x // other[0], self.y // other[1], self.z // other[2])
        else: return NotImplemented
    def __rfloordiv__(self, other):
        if not isinstance(other, (Vector3D, list, tuple)): return NotImplemented
        if isinstance(other, Vector3D): return Vector3D(other.x // self.x, other.y // self.y, other[2] // self.z)
        if len(other) >= 3: return Vector3D(other[0] // self.x, other[1] // self.y, other[2] // self.z)
        else: return NotImplemented

# Para representações complexas e quadridimensionais, como o conjunto espaço tempo ou sistemas que nescessitam de todos os três ao mesmo tempo.
class Vector4D():
    def __init__(self, x:float, y:float, z:float, t:float): self._x, self._y, self._z, self._t = x, y, z, t
    def __repr__(self): return f"Vector4D(x: {self._x,}, y: {self.y}, z: {self.z}, t: {self.t})"
    def __iter__(self):
        for dim in [self._x, self._y, self._z, self._t]: yield 

    def __add__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(self.x + other.x, self.y + other.y)
        if len(other) >= 2: return Vector4D(self.x + other[0], self.y + other[1])
        else: return NotImplemented
    def __radd__(self, other): self.__add__(other)

    def __mul__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(self.x * other.x, self.y * other.y)
        if len(other) >= 2: return Vector4D(self.x * other[0], self.y * other[1])
        else: return NotImplemented
    def __rmul__(self, other): self.__mul__(other)

    def __sub__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(self.x - other.x, self.y - other.y)
        if len(other) >= 2: return Vector4D(self.x - other[0], self.y - other[1])
        else: return NotImplemented
    def __rsub__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(other.x - self.x, other.y - self.y)
        if len(other) >= 2: return Vector4D(other[0] - self.x, other[1] - self.y)
        else: return NotImplemented

    def __truediv__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(self.x / other.x, self.y / other.y)
        if len(other) >= 2: return Vector4D(self.x / other[0], self.y / other[1])
        else: return NotImplemented
    def __rtruediv__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(other.x / self.x, other.y / self.y)
        if len(other) >= 2: return Vector4D(other[0] / self.x, other[1] / self.y)
        else: return NotImplemented

    def __floordiv__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(self.x // other.x, self.y // other.y)
        if len(other) >= 2: return Vector4D(self.x // other[0], self.y // other[1])
        else: return NotImplemented
    def __rfloordiv__(self, other):
        if not isinstance(other, (Vector4D, list, tuple)): return NotImplemented
        if isinstance(other, Vector4D): return Vector4D(other.x // self.x, other.y // self.y)
        if len(other) >= 2: return Vector4D(other[0] // self.x, other[1] // self.y)
        else: return NotImplemented