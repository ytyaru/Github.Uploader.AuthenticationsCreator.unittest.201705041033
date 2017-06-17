import unittest
#from AuthenticationsCreator import AuthenticationsCreator
from web.service.github.api.v3.AuthenticationsCreator import AuthenticationsCreator
class TestAuthenticationsCreator_TDD(unittest.TestCase):
    def test_HasAttribute(self):
        self.assertTrue(hasattr(AuthenticationsCreator, 'Create'))
        
