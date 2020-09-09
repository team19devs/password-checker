import requests, hashlib, sys

def request_api_data(query_sign):	
	url = "https://api.pwnedpasswords.com/range/"+ query_sign
	request = requests.get(url)
	if request.status_code != 200:
		raise RuntimeError(f"An error occured. Please check password again")
	return request

def check_response(hashes, check_hash):
	hashes = (line.split(":") for line in hashes.text.splitlines())
	for hash, count in hashes:
		if hash == check_hash:
			return count
	return 0

def check_api_pwned(password):
	sha1_password = hashlib.sha1(password.encode("UTF-8")).hexdigest().upper()
	first5_char, left_char = sha1_password[:5], sha1_password[5:]
	response = request_api_data(first5_char)
	return check_response(response, left_char )

def main(args):
	for password in args:
		count = check_api_pwned(password)
		if count:
			print(f"Your password was found {count}. I highly recommend to alter it")
		else:
			print(f"{len(password)*'*'} was NOT found on our database, Continue!")
	return 'endep-up process'

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))