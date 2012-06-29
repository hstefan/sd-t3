from argparse import ArgumentParser
from twitter_api_wrapper import get_twitter_id, get_tweets

def setup_arguments():
	parser = ArgumentParser(description='Provides you a automated stalking tool!')
	parser.add_argument('-u', '--user', dest = 'user', metavar='USER', type=str, 
		help='The stalking target user!')
	return parser
	
def main():
	parser = setup_arguments()
	args = parser.parse_args()	
	user_str = args.user
	id = get_twitter_id(user_str)
	print(get_tweets(id, 10))
	
if __name__ == '__main__':
	main()