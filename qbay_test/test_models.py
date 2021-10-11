from qbay.models import register, login, update_user


def test_r1_1_user_register():
    '''
    Both the email and password cannot be empty.
    '''

    assert register('user', 'good@test.com', '@Password') is True
    assert register('user', '', '@Password') is False
    assert register('user', 'badpassword@test.com', '') is False
    assert register('user', '', '') is False


def test_r1_2_user_register():
    '''
    Testing R1-2: A user is uniquely identified by his/her email address.
    '''

    register('FoundUser', 'find.user@test.com', '@Password')
    user = login('find.user@test.com', '@Password')
    assert user.username == 'FoundUser'
    assert user.password == '@Password'


# NEEDS TO GET DONE
def test_r1_3_user_register():
    '''
    The email has to follow addr-spec defined in RFC 5322
    '''
    
    assert register('testEmail', 'testemail@com', '@Password') is False
    assert register('testEmail', 'te..st@mail.com', '@Password') is False
    assert register('testEmail', '.test@mail.com', '@Password') is False
    assert register('testEmail', 'test.@mail.com', '@Password') is False
    assert register('testEmail', 'test.gg@mail.com', '@Password') is True
    assert register('u5', '''yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyys@test.com''', '@Password') is False
    assert register('user', '', '@Password') is False
    assert register('testEmail', 't!est.gg@mail.com', '@Password') is True
    assert register('testEmail', 't*est.gg@mail.com', '@Password') is True
    assert register('testEmail', '#est.gg@mail.com', '@Password') is True
    assert register('testEmail', '{t_est}.gg@mail.com', '@Password') is True
    assert register('testEmail', '"t!st.gg"@mail.com', '@Password') is True
    assert register('testEmail', '\" \"@mail.com', '@Password') is True
    assert register('testEmail', '"t!e"st.gg@mail.com', '@Password') is False
    assert register('testEmail', '"t!e"st.gg@mail.com', '@Password') is False
    assert register('testEmail', '"t!e"st" ".gg@ma.com', '@Password') is False
    assert register('testEmail', '""@mail.com', '@Password') is False
    
    assert register('testEmail', 'test@-mail.com', '@Password') is False
    assert register('testEmail', 'test.@mail.com-', '@Password') is False
    assert register('u5', '''test@yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
    yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.com''', '@Password') is False
    assert register('testEmail', 'test.@ma..il.com', '@Password') is False


def test_r1_4_user_register():
    '''
    Password has to meet the required complexity: minimum length 6,
    at least one upper case, at least one lower case, and at least
    one special character.
    '''

    assert register('user', 'TestPassword@test.com', '@Password') is True
    assert register('user', 'lowercasePassword@test.com', '@password') is False
    assert register('user', 'uppercasePassword@test.com', '@PASSWORD') is False
    assert register('user', 'specialPassword@test.com', 'Password') is False


def test_r1_5_user_register():
    '''
    User name has to be non-empty, alphanumeric-only,
    and space allowed only if it is not as the prefix or suffix.
    '''

    assert register('user', 'ValidUser@test.com', '@Password') is True
    assert register(' ', 'SpaceUser@test.com', '@Password') is False
    assert register('user@', 'SpecialPassword@test.com', '@PASSWORD') is False
    assert register(' user', 'SpaceFirst@test.com', '@Password') is False
    assert register('user ', 'SpaceLast@test.com', '@Password') is False
    assert register('us er', 'SpaceMiddle@test.com', '@Password') is True


def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters
    and less than 20 characters.
    '''

    assert register('2c', '2characters@test.com',
                    '@Password') is True
    assert register('exactly20characterss', '20characters@test.com',
                    '@Password') is True
    assert register('within2and20char', 'lessthan20and2@test.com',
                    '@Password') is True
    assert register('longerthan20characters', 'morethan20@test.com',
                    '@Password') is False
    assert register('1', '1character@test.com', '@Password') is False


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('user', 'same.email@test.com', '@Password') is True
    assert register('user', 'unique@test.com', '@Password') is True
    assert register('user', 'same.email@test.com', '@Password') is False


def test_r1_8_user_register():
    '''
    Testing R1-8: Shipping address is empty at the time of registration.
    '''

    register('user', 'shipping@test.com', '@Password')
    user = login('shipping@test.com', '@Password')
    assert user.shipping_address is None


def test_r1_9_user_register():
    '''
    Testing R1-9: Postal code is empty at the time of registration.
    '''

    register('user', 'postal@test.com', '@Password')
    user = login('postal@test.com', '@Password')
    assert user.postal_code is None


def test_r1_10_user_register():
    '''
    Testing R1-9: Balance should be initialized as 100
    at the time of registration. (free $100 dollar signup bonus).
    '''

    register('BalanceUser', 'Balance.Test@test.com', '@Password')
    user = login('Balance.Test@test.com', '@Password')
    assert user.balance == 100


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the test_r1_10_user_register test, so we
    already have BalanceUser in database)
    '''

    user = login('Balance.Test@test.com', '@Password')
    assert user is not None
    assert user.username == 'BalanceUser'

    user = login('Balance.Test@test.com', '@BadPassword')
    assert user is None

    user = login('notemail@test.com', '@Password')
    assert user is None


def test_r2_2_login():
    '''
    Testing R2-2: The login function should check if the supplied 
    inputs meet the same email/password requirements in the register 
    function, before checking the database.
    '''

    assert login('', '@Password') is None
    assert login('badpassword@test.com', '') is None
    assert login('', '') is None

    assert login('lowercasePassword@test.com', '@password') is None
    assert login('uppercasePassword@test.com', '@PASSWORD') is None
    assert login('specialPassword@test.com', 'Password') is None

    user = login('Balance.Test@test.com', '@Password')
    assert user is not None
    assert user.username == 'BalanceUser'


def test_r3_1_update():
    '''
    Testing R3-1: A user is only able to update his/her user name, 
    shipping_address, and postal_code.
    '''

    register('RandomUser', 'update.Test@test.com', '@Password')
    user = login('update.Test@test.com', '@Password')
    assert user.username == 'RandomUser'
    assert user.shipping_address is None
    assert user.postal_code is None
    assert update_user('update.Test@test.com', 'ModifiedUser', 
                       'ModifiedShipping', 'K7L 2H9') is True
    user2 = login('update.Test@test.com', '@Password')
    assert user2.username == 'ModifiedUser'
    assert user.shipping_address == 'ModifiedShipping'
    assert user.postal_code == 'K7L 2H9'

    assert update_user('nonexsitant.user@test.com', 'ModifiedUser', 
                       'ModifiedShipping', 'K7L 2H9') is False

def test_r3_2_update():
    '''
    Testing R3-2: Shipping_address should be non-empty, alphanumeric-only, 
    and no special characters such as !
    '''

    assert update_user('update.Test@test.com', 'alphanumeric12only') is True
    assert update_user('update.Test@test.com', '',) is False
    assert update_user('update.Test@test.com', 'specialchars!@}') is False


def test_r3_3_update():
    '''
    Testing R3-3: Postal code must be a valid Canadian postal code
    '''

    assert update_user('update.Test@test.com', None, None, 'M1C 8X3') is True
    assert update_user('update.Test@test.com', None, None, 'm1C 8X3') is False
    assert update_user('update.Test@test.com', None, None, 'D1C 8X3') is False
    assert update_user('update.Test@test.com', None, None, 'F1C 8X3') is False
    assert update_user('update.Test@test.com', None, None, 'I1C 8X3') is False
    assert update_user('update.Test@test.com', None, None, 'O1C 8X3') is False
    assert update_user('update.Test@test.com', None, None, 'Q1C 8X3') is False
    assert update_user('update.Test@test.com', None, None, 'U1C 8X3') is False
    assert update_user('update.Test@test.com', None, None, 'Z1C 8X3') is False


def test_r3_4_update():
    '''
    Testing R3-4: User name has to be non-empty, alphanumeric-only, 
    and space allowed only if it is not as the prefix or suffix.
    User name also has to be longer than 2 characters and less 
    than 20 characters.
    '''

    assert update_user('update.Test@test.com', 'ValidName') is True
    assert update_user('update.Test@test.com', '',) is False
    assert update_user('update.Test@test.com', 'user@}') is False
    assert update_user('update.Test@test.com', ' user',) is False
    assert update_user('update.Test@test.com', 'user ',) is False
    assert update_user('update.Test@test.com', 'us er',) is True
    assert update_user('update.Test@test.com', '2c') is True
    assert update_user('update.Test@test.com', 
                       'exactly20characterss') is True
    assert update_user('update.Test@test.com',
                       'within2and20char') is True
    assert update_user('update.Test@test.com',
                       'longerthan20characters') is False
    assert update_user('update.Test@test.com',
                       '1') is False
