class Vector2D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y, self.z + other.z)

first = Vector2D(5, 7, 1)
second = Vector2D(3, 9, 0)
result = first + second

print(result.x , result.y, result.z)
