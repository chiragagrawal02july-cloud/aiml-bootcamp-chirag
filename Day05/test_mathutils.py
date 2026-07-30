from mathutils import average, biggest, is_prime

# For average :-
def test_average_normal():
    assert average([80, 90, 100]) == 90

def test_average_empty():
    assert average([]) == 0
    
# For biggest :-
def test_biggest_normal() :
    assert biggest([4, 2, 7, 9]) == 9

def test_biggest_single():
    assert biggest([5]) == 5

def test_biggest_empty():
    assert biggest([]) is None

# For is_prime :
def test_is_prime_prime():
    assert is_prime(13) is True 

def test_is_prime_composite():
    assert is_prime(12) is False

def test_is_prime_zero():
    assert is_prime(0) is False

def test_is_prime_one():
    assert is_prime(1) is False

def test_is_prime_negative():
    assert is_prime(-11) is False

def is_prime(n):
    if n <= 1 :
        return False
    for i in range(2, int(n**0.5) + 1) :
        if n % i == 0 :
            return False
    return True
