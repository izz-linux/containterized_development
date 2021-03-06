import onetimepass as otp
import subprocess

my_secret=input("Enter your seed secret: ")
my_token=otp.get_totp(my_secret,token_length=6)

print("your current OTP is {}".format(my_token))
