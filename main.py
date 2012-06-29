import sys
from argparse import ArgumentParser
from twitter_api_wrapper import get_twitter_id, get_tweets
from directions_api_wrapper import get_directions

def setup_arguments():
    parser = ArgumentParser(description='Provides you with an automated stalking tool!')
    parser.add_argument('-u', '--user', dest='user', metavar='USER', type=str, required=True,
        help='The stalking target user!')
    parser.add_argument('-n', '--num_tweets', dest='num_tweets', metavar='NUM_TWEETS', type=int,
        help='Number of tweets to retrieve', default=10)
    parser.add_argument('-t', '--travel_mode', dest='travel_mode', metavar='TRAVEL_MODE', type=int,
        help='Travel modes (1 - driving, 2 - walking, 3 - bicycling(if you need silence and speed), 4 - transit (public transit routes)',
        default=1)
    return parser

def display_tweets(tweets_json):
    with_location = []
    for i, tweet in enumerate(tweets_json):
        geo_enabled = tweet['user']['geo_enabled']
        coordinates = tweet['coordinates']
        if geo_enabled and  coordinates:
            message = '(' + str(i+1) + ') ' + tweet['text'] + '\n'
            # Prevent a failed encode from blowing up the program
            # This is just output after all.
            sys.stdout.buffer.write(message.encode(sys.stdout.encoding, 'replace'))
            with_location.append((message, coordinates))
    return with_location

def main():
    parser = setup_arguments()
    args = parser.parse_args()

    user_str = args.user
    id = get_twitter_id(user_str)

    with_location = display_tweets(get_tweets(id, args.num_tweets))
    
    tweet_selected = None
    while not tweet_selected:
        try:
            tweet_selected = with_location[eval(input('Numero do tweet a ser seguido: ')) -1]
        except IndexError:
            print('Indice invalido.')
    
    coordinates = tweet_selected[1]['coordinates']
    user_adress = input('Endereco de origem: ')
    print(get_directions(user_adress, coordinates))
if __name__ == '__main__':
    main()
