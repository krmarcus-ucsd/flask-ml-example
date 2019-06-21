import gzip
from collections import defaultdict


class SimilarItemsMlModel:

    def __init__(self):
        path = "datasets/amazon_reviews_us_Musical_Instruments_v1_00.tsv.gz"
        f = gzip.open(path, 'rt', encoding="utf8")

        header = f.readline()
        header = header.strip().split('\t')
        self.dataset = []

        for line in f:
            fields = line.strip().split('\t')
            d = dict(zip(header, fields))
            d['star_rating'] = int(d['star_rating'])
            d['helpful_votes'] = int(d['helpful_votes'])
            d['total_votes'] = int(d['total_votes'])
            self.dataset.append(d)

        self.usersPerItem = defaultdict(set)
        self.itemsPerUser = defaultdict(set)

        self.itemNames = {}

        for d in self.dataset:
            user, item = d['customer_id'], d['product_id']
            self.usersPerItem[item].add(user)
            self.itemsPerUser[user].add(item)
            self.itemNames[item] = d['product_title']

    def jaccard(self, s1, s2):
        numer = len(s1.intersection(s2))
        denom = len(s1.union(s2))
        return numer / denom

    def most_similar_fast(self, item_id):
        similarities = []
        users = self.usersPerItem[item_id]
        candidate_items = set()
        for user in users:
            candidate_items = candidate_items.union(self.itemsPerUser[user])
        for candidate_item in candidate_items:
            if candidate_item == item_id:
                continue
            sim = self.jaccard(users, self.usersPerItem[candidate_item])
            similarities.append((sim, candidate_item))
        similarities.sort(reverse=True)
        return similarities[:10]

    def get_similar_items(self, id):
        similar_items = [self.itemNames[x[1]] for x in self.most_similar_fast(id)]
        data = {'id': id, 'name': self.itemNames[id], 'similar': similar_items}
        return data

    def get_items(self, start_index, count):
        data = []
        for i in range(count):
            item = self.dataset[start_index + i]
            data.append(dict((k, item[k]) for k in ('product_id', 'product_title')))
        return data
