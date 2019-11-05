my_rating = 8#(6+3+6)/3

import json
import matplotlib.pyplot as plt

data = []
for line in open('iclr20_metadata.jsonl', 'r'):
    data.append(json.loads(line))
    ra = data[-1]['review_ratings']
    if sum([int(r[0]) for r in ra])/len(ra)==8:
        import ipdb; ipdb.set_trace()


print("Num of submissions: {}".format(len(data)))

ratings = []
for d in range(len(data)):
    ra = data[d]['review_ratings']
    ratings.append( sum([int(r[0]) for r in ra])/len(ra) )
ratings.sort()
print('Your papar beats {:.2f}% of submission '.format(  sum([r<my_rating for r in ratings])/len(ratings) ))
print('Your papar belows {:.2f}% of submission '.format(  sum([r>my_rating for r in ratings])/len(ratings) ))
_ = plt.hist(ratings, bins='auto')
plt.show()
