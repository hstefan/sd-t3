import sys
from argparse import ArgumentParser
from twitter_api_wrapper import get_twitter_id, get_tweets
from directions_api_wrapper import get_directions
from util import better_print
import re

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
    
def display_directions(directions_json):
    route = directions_json['routes'][0];
    copyright_route = 'Os direitos de copia desta rota são reservados a: ' + route['copyrights'] + '\n'
    better_print(copyright_route)
    legs_info = route['legs'][0]
    msg = 'Distância: {0}, Duração: {1}'.format(legs_info['distance']['text'], legs_info['duration']['text']) + '\n'
    better_print(msg)
    msg = 'Endereço inicial: {0} \n Endereço final: {1}'.format(legs_info['start_address'], legs_info['end_address'])
    better_print(msg)
    
    steps = legs_info['steps']
    for step in steps:
        better_print(re.sub('<[^<]+?>', '', step['html_instructions']))
    
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
    coordinates.reverse() #maps API receives coordinates(lat, long), while twitter api retrieves (long,lat)
   
    travel_mode_str = 'driving'
    if args.travel_mode == 2:
        travel_mode_str == 'walking'
    elif args.travel_mode == 3:
        travel_mode_str = 'bicycling'
    elif args.travel_mode == 4:  
        travel_mode_str = 'transit'
    
    directions_json = get_directions(user_adress, coordinates, travel_mode_str)
    
    display_directions(directions_json)
    
if __name__ == '__main__':
    main()
