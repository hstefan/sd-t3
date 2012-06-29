from PyQt4 import QtCore, QtGui
from app_gui import Ui_MainWindow
from util import list_tweets_with_location
from twitter_api_wrapper import get_twitter_id, get_tweets

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
        if len(self.ui.le_user.text()) > 0 and len(self.ui.le_user.text()) > 0:
            self.tweet_list = list_tweets_with_location(get_tweets(get_twitter_id(self.ui.le_user.text()), 
                int(self.ui.le_tweets_number.text())))
            self.ui.lv_tweets.clear()
            for tweet, coord in self.tweet_list:
                self.ui.lv_tweets.addItem(tweet)
                
    def get_route_callback(self):
        pass