import json
from argparse import ArgumentParser
from urllib.request import urlopen

def setup_arguments():
	parser = ArgumentParser(description='Provides you a automated stalking tool!')
	parser.add_argument('-u', '--user', dest = 'user', metavar='USER', type=str, 
		help='The stalking target user!')
	return parser

def get_twitter_id(username):
	twitter_api_url = 'https://api.twitter.com/1/users/show.json?screen_name=' + username
	response = urlopen(twitter_api_url)
	raw_data = response.read()
	dec_raw_data = raw_data.decode('utf-8')
	json_output = json.loads(dec_raw_data)
	return json_output['id']
	
def main():
	parser = setup_arguments()
	args = parser.parse_args()	
	user_str = args.user
	print(get_twitter_id(user_str))
	
if __name__ == '__main__':
	main()