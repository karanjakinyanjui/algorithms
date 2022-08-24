
from unittest import TestCase

from .primes import sieve_of_erastothenes


class PrimeTests(TestCase):
    
    def test_primes(self):
        result = sieve_of_erastothenes(7)
        self.assertEqual(result, [2, 3, 5])
        self.assertEqual(sieve_of_erastothenes(15), [2, 3, 5, 7, 11, 13])
