import pickle
import datetime

# now = datetime.datetime.utcnow()
# pickled = pickle.dumps(now)
# now_2 = pickle.loads(pickled)
# print(now_2)


class Human:
    def __str__(self):
        return "This is Humans"


human = Human()
human_pickle = pickle.dumps(human)
human_2 = pickle.loads(human_pickle)
print(human_2)
