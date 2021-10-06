from qbay.models import register, login

def test_r1_1_user_register():
    '''
    Testing R1-1: If either the email or password are empty,
    the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u1', '', '234567') is False
    assert register('u0', 'test2@test.com', '') is False
    assert register('u4', '', '') is False


def test_r1_2_user_register():
    '''
    Testing R1-2: If email has already been used, its not
    unique and the test fails
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False

    
def test_r1_4_user_register():
    '''
    Password has to meet the required complexity: minimum length 6, 
    at least one upper case, at least one lower case, and at least 
    one special character.
    '''

    assert register('user1', 'test0@test.com', '12345677') is True



def test_r1_6_user_register():
    '''
    Testing R1-6: User name has to be longer than 2 characters 
    and less than 20 characters.
    '''

    assert register('2c', 'test0@test.com', '12345677') is True
    assert register('exactly20characterss', 'test0@test.com', '12345677') is True
    assert register('within2and20char', 'test0@test.com', '12345677') is True
    assert register('longerthan20characters', 'test1@test.com', '12345677') is False
    assert register('1', 'test1@test.com', '12345677') is False

def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', '12345677') is True
    assert register('u0', 'test1@test.com', '12345677') is True
    assert register('u1', 'test0@test.com', '12345677') is False


def test_r1_8_user_register():
    '''
    Testing R1-8: Shipping address is empty at the time of registration.
    '''

    new_user = register('newuser', 'test2@test.com', '12345677')
    assert new_user.shipping_adress is None


def test_r1_9_user_register():
    '''
    Testing R1-9: Postal code is empty at the time of registration.
    '''

    new_user = register('newuser', 'test3@test.com', '12345677')
    assert new_user.postal_code is None

def test_r1_10_user_register():
    '''
    Testing R1-9: Balance should be initialized as 100 
    at the time of registration. (free $100 dollar signup bonus).
    '''

    new_user = register('newuser', 'test4@test.com', '12345677')
    assert new_user.balance == 100


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test, so we already have u0,
      u1 in database)
    '''

    user = login('test0@test.com', 12345677)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 123456777)
    assert user is None
