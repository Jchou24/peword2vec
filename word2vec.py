#encoding=utf8

import gensim
from gensim.models import word2vec

class word2vec_vote():
    def __init__(self):
        pass

    def load_corpus(self,filename):
        self.corpus = []
        with open(filename,'r') as op:
            for line in op:
                self.corpus.append(line.split())

    def load_model(self,filename):
        self.model = gensim.models.Word2Vec.load(filename)

    def train_model(self,workers=4,size=200,min_count=1,window=10,sample=200):
        print "Training model..."
        self.model = word2vec.Word2Vec(self.corpus, workers=workers, size=size,
            min_count = min_count, window = window, sample = sample)

        # self.model = word2vec.Word2Vec(self.corpus)

    def save_model(self,filename):
        self.model.save(filename)

    def sim(self,word,topn=10):
        return self.model.most_similar(word,topn = topn)

    def infer(self,a,b,c,topn=10):
        return self.model.most_similar(positive=[a,b], negative=[c], topn = topn)

def demo():
    documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]
    documents = [ d.lower().split() for d in documents ]

    vote = word2vec_vote()
    vote.corpus = documents
    # vote.train_model(min_count=0)
    # vote.save_model("test_model.model")
    vote.load_model("test_model.model")

    print vote.sim("user")
    print vote.infer("user","computer","system")

def training():
    vote = word2vec_vote()
    vote.load_corpus("2016PE_news_cuted.txt")
    vote.train_model()
    vote.save_model("2016PE_news_cuted.model")

def testing():
    vote = word2vec_vote()
    vote.load_model("2016PE_news_cuted.model")
    print vote.sim("蔡英文")
    print vote.infer("蔡英文","朱立倫","宋楚瑜")

if __name__ == '__main__':
    # training()
    # testing()
    pass
    vote = word2vec_vote()
    vote.load_corpus("2016PE_news_cuted.txt")
    print [vote.corpus[0][1].decode('utf8')]
