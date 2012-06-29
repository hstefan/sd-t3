import sys
import re
from argparse import ArgumentParser
from twitter_api_wrapper import get_twitter_id, get_tweets
from directions_api_wrapper import get_directions_json
from util import better_print
from gui_wrapper import Gui_Wrapper
from PyQt4 import QtGui

def main_cli():
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
    
    directions_json = get_directions_json(user_adress, coordinates, travel_mode_str)
    
    display_directions(directions_json)

    
def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Gui_Wrapper()
    myapp.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
