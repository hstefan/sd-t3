import sys
from argparse import ArgumentParser
from twitter_api_wrapper import get_twitter_id, get_tweets

def setup_arguments():
    parser = ArgumentParser(description='Provides you a automated stalking tool!')
    parser.add_argument('-u', '--user', dest='user', metavar='USER', type=str, required=True,
        help='The stalking target user!')
    return parser

def display_tweets(tweets_json):
    i = 1
    for tweet in tweets_json:
        message = '(' + str(i) + ') ' + tweet['text'] + '\n'
        # Prevent a failed encode from blowing up the program
        # This is just output after all.
        sys.stdout.buffer.write(message.encode(sys.stdout.encoding, 'replace'))
        i = i + 1

def main():
    parser = setup_arguments()
    args = parser.parse_args()

    user_str = args.user
    id = get_twitter_id(user_str)

    display_tweets(get_tweets(id, 10))

if __name__ == '__main__':
    main()
