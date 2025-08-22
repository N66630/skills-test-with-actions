# System Modules
import sys
import os
import pytest
import pytest

# Installed Modules
# None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    def test_area_of_circle_negative_radius():
        """Test area_of_circle with a negative radius (should raise ValueError)."""
        with pytest.raises(ValueError):
            # System Modules

            # Installed Modules
            # None

            # Project Modules
            sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
            from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


            def test_area_of_circle_positive_radius():
                """Test with a positive radius."""
                radius = 1
                result = area_of_circle(radius)
                assert abs(result - 3.14159) < 1e-5


            def test_area_of_circle_zero_radius():
                """Test with a radius of zero."""
                radius = 0
                result = area_of_circle(radius)
                assert result == 0


            def test_area_of_circle_negative_radius():
                """Test area_of_circle with a negative radius (should raise ValueError)."""
                with pytest.raises(ValueError):
                    area_of_circle(-1)


            def test_area_of_circle_large_radius():
                """Test area_of_circle with a large radius."""
                radius = 1000
                result = area_of_circle(radius)
                expected = 3_141_592.653589793
                assert abs(result - expected) < 1e-5


            def test_area_of_circle_float_radius():
                """Test area_of_circle with a float radius."""
                radius = 2.5
                result = area_of_circle(radius)
                expected = 19.634954084936208
                assert abs(result - expected) < 1e-8


            def test_get_nth_fibonacci_zero():
                """Test with n=0."""
                n = 0
                result = get_nth_fibonacci(n)
                assert result == 0


            def test_get_nth_fibonacci_one():
                """Test with n=1."""
                n = 1
                result = get_nth_fibonacci(n)
                assert result == 1


            def test_get_nth_fibonacci_two():
                """Test get_nth_fibonacci with n=2."""
                assert get_nth_fibonacci(2) == 1


            def test_get_nth_fibonacci_five():
                """Test get_nth_fibonacci with n=5."""
                assert get_nth_fibonacci(5) == 5


            def test_get_nth_fibonacci_ten():
                """Test with n=10."""
                n = 10
                result = get_nth_fibonacci(n)
                assert result == 55


            def test_get_nth_fibonacci_negative():
                """Test get_nth_fibonacci with negative n (should raise ValueError)."""
                with pytest.raises(ValueError):
                    get_nth_fibonacci(-5)


            def test_get_nth_fibonacci_large():
                """Test get_nth_fibonacci with a large n."""
                n = 30
                result = get_nth_fibonacci(n)
                assert result == 832040
        expected = 3_141_592.653589793
        assert abs(result - expected) < 1e-5


    def test_get_nth_fibonacci_two():
        """Test get_nth_fibonacci with n=2."""
        assert get_nth_fibonacci(2) == 1


    def test_get_nth_fibonacci_five():
        """Test get_nth_fibonacci with n=5."""
        assert get_nth_fibonacci(5) == 5
