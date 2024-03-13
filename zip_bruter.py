import pyzipper
import os
from time import time
import argparse

parser = argparse.ArgumentParser(
	prog='zip_bruter',
	description='this is zip password bruter that support AES',
	#epilog='Test'
)

parser.add_argument('-f', metavar='zipfile', action='store', required=True)
parser.add_argument('-p', metavar='password_list: /usr/share/john/password.lst (default)', action='store')
parser.add_argument('-e', metavar='encode: utf-8 (default)', action='store')


def main():
	args = parser.parse_args()

	file_path = args.zipfile

	if args.password_list != '':
		password_list = args.password_list
	else:
		password_list = '/usr/share/john/password.lst'

	if args.encode != '':
		encode = args.encode
	else:
		encode = 'utf-8'

	print('zipfile: {}'.format(file_path))
	print('password_list: {}'.format(password_list))
	print('encode: {}'.format(encode))

	try:
		zip_ = pyzipper.AESZipFile(file_path)
	except zipfile.BadZipfile:
		print (" [!] Please check the file's Path. It doesn't seem to be a ZIP file.")
		quit()

	password = None 
	i = 0 
	c_t = time()
	with open(password_list, "r") as f: 
		passes = f.readlines() 
		for x in passes:
			i += 1
			password = x.split("\n")[0]  
			print(password)
			try:
				zip_.extractall(pwd=password.encode(encode))
				t_t = time() - c_t 
				print("\n [*] Password Found :)\n" + " [*] Password: "+password+"\n" )
				print(" [***] Took %f seconds to Srack the Password. That is, %i attempts per second." % (t_t,i/t_t))
				quit()
			except Exception:
				pass
		print(" [X] Sorry, Password Not Found :(")
		quit()

main()
