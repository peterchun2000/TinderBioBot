import tinder_api.session
import itertools
from datetime import datetime
from datetime import datetime
import time


sess = tinder_api.session.Session() # inits the session

print("Starting Bot...")
while(1):
    current_time = datetime.now().strftime("%I:%M %p")
    sess.update_profile(bio=f"It is {current_time} and you're on Tinder instead of being with me")
    time.sleep(30) 


