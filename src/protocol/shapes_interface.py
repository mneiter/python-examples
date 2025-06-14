from typing import Protocol


class Shape(Protocol):
    """Interface for geometric shapes."""

    def area(self) -> float:
        """Calculate area of the shape."""
        ...

    def perimeter(self) -> float:
        """Calculate perimeter of the shape."""
        ...
