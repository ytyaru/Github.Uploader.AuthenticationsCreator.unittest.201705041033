import unittest
from database.src.Database import Database
from web.service.github.api.v3.AuthenticationsCreator import AuthenticationsCreator
from web.service.github.api.v3.authentication.Authentication import Authentication
from web.service.github.api.v3.authentication.NonAuthentication import NonAuthentication
from web.service.github.api.v3.authentication.BasicAuthentication import BasicAuthentication
from web.service.github.api.v3.authentication.TwoFactorAuthentication import TwoFactorAuthentication
from web.service.github.api.v3.authentication.OAuthAuthentication import OAuthAuthentication
from web.service.github.api.v3.authentication.OAuthTokenFromDatabaseAuthentication import OAuthTokenFromDatabaseAuthentication
from web.service.github.api.v3.authentication.OAuthTokenFromDatabaseAndCreateApiAuthentication import OAuthTokenFromDatabaseAndCreateApiAuthentication
class TestAuthenticationsCreator_BlackBox(unittest.TestCase):
    def test_Create_OAuthAuthentication_BasicAuthentication(self):
        db = Database()
        db.Initialize()
        username = 'ytyaru' # 存在するユーザ名。Token登録済み。TwoFactorSecretなし。
        creator = AuthenticationsCreator(db, username)
        authentications = creator.Create() # [OAuthAuthentication, BasicAuthentication]
        self.assertEqual(list, type(authentications))
        self.assertEqual(2, len(authentications))
        self.assertEqual(OAuthAuthentication, type(authentications[0]))
        self.assertEqual(BasicAuthentication, type(authentications[1]))        
    def test_Create_OAuthAuthentication_TwoFactorAuthentication(self):
        db = Database()
        db.Initialize()
        username = 'csharpstudy0' # 存在するユーザ名。Token登録済み。TwoFactorSecretあり。
        creator = AuthenticationsCreator(db, username)
        authentications = creator.Create() # [OAuthAuthentication, TwoFactorAuthentication]
        self.assertEqual(list, type(authentications))
        self.assertEqual(2, len(authentications))
        self.assertEqual(OAuthAuthentication, type(authentications[0]))
        self.assertEqual(TwoFactorAuthentication, type(authentications[1]))
    def test_Create_UnregisteredException_ConstractorParameter(self):
        db = Database()
        db.Initialize()
        username = 'NoneExistUsername' # 存在しないユーザ名
        creator = AuthenticationsCreator(db, username)
        with self.assertRaises(Exception) as e:
            creator.Create()
            self.assertEqual(e.msg, '指定したユーザ {0} はDBに未登録です。登録してから実行してください。'.format(username))
    def test_Create_UnregisteredException_MethodParameter(self):
        db = Database()
        db.Initialize()
        username = 'ytyaru' # 存在するユーザ名
        creator = AuthenticationsCreator(db, username) # 
        with self.assertRaises(Exception) as e:
            username = 'NoneExistUsername' # 存在しないユーザ名
            creator.Create(username=username)
            self.assertEqual(e.msg, '指定したユーザ {0} はDBに未登録です。登録してから実行してください。'.format(username))
            
