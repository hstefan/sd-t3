from argparse import ArgumentParser
from twitter_api_wrapper import get_twitter_id

def setup_arguments():
	parser = ArgumentParser(description='Provides you a automated stalking tool!')
	parser.add_argument('-u', '--user', dest = 'user', metavar='USER', type=str, 
		help='The stalking target user!')
	return parser
	
def main():
	parser = setup_arguments()
	args = parser.parse_args()	
	user_str = args.user
	print(get_twitter_id(user_str))
	
if __name__ == '__main__':
	main()