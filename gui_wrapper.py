from PyQt4 import QtCore, QtGui
from app_gui import Ui_MainWindow
from util import tweet_has_location, get_directions_list
from twitter_api_wrapper import TwitterError, get_twitter_id, get_tweets
from directions_api_wrapper import get_directions_json

class Gui_Wrapper(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setup_callbacks()
        
    def setup_callbacks(self):
        QtCore.QObject.connect(self.ui.bt_search, QtCore.SIGNAL("clicked()"), self.search_tweets_callback)
        QtCore.QObject.connect(self.ui.bt_route, QtCore.SIGNAL("clicked()"), self.get_route_callback)
        
    def search_tweets_callback(self):
        if len(self.ui.le_user.text()) > 0:
            try:
                user_id = get_twitter_id(self.ui.le_user.text())
                all_tweets = get_tweets(user_id, self.ui.le_tweets_number.value())
            except TwitterError as e:
                QtGui.QMessageBox.critical(self, "Twitter Error", str(e))
                return

            self.tweet_list = [(tweet['text'], tweet['coordinates']) for tweet in all_tweets if tweet_has_location(tweet)]
            self.ui.lv_tweets.clear()
            for tweet, coord in self.tweet_list:
                self.ui.lv_tweets.addItem(tweet)

    def get_route_callback(self):
        selected_index = self.ui.lv_tweets.indexFromItem(self.ui.lv_tweets.selectedItems()[0]).row()

        if len(self.ui.le_address.text()) > 0 and self.tweet_list:
            coord = self.tweet_list[selected_index][1]['coordinates'][:]
            coord.reverse()
            directions_json = get_directions_json(self.ui.le_address.text(), coord, self.ui.cb_mode.currentText)
            directions_list = get_directions_list(directions_json)
            self.ui.lv_directions.clear()
            for direction in directions_list:
                self.ui.lv_directions.addItem(direction)
