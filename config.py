import os
import numpy as np


class Config:
    def __init__(self,
                 feat_folder,
                 drop_html_flag=True,
                 basic_tfidf_ngram_range=(1, 3),
                 basic_tfidf_vocabulary_type="common",
                 cooccurrence_tfidf_ngram_range=(1, 1),
                 cooccurrence_word_exclude_stopword=False,
                 stemmer_type="snowball",
                 count_feat_transform=np.sqrt):

        self.drop_htlm_flag = False
        self.n_classes = 3
        self.stemmer_type = 'porter'

        ##

        self.n_classes = 3  # 4

        # CV params
        self.n_runs = 3
        self.n_folds = 3
        self.stratified_label = "query"

        # path
        self.root = '/home/stan/Documents/dev/homedepot/'

        self.data_folder = self.root + 'raw_data/'
        self.data_path = self.data_folder
        self.feat_folder = self.root + 'Feat/'
        self.original_train_data_path = self.data_path + 'train.csv'
        self.original_test_data_path = self.data_path + 'test.csv'
        self.processed_train_data_path = "%s/train.processed.csv.pkl" % self.feat_folder
        self.processed_test_data_path = "%s/test.processed.csv.pkl" % self.feat_folder
        self.pos_tagged_train_data_path = "%s/train.pos_tagged.csv.pkl" % self.feat_folder
        self.pos_tagged_test_data_path = "%s/test.pos_tagged.csv.pkl" % self.feat_folder

        # nlp related
        self.drop_html_flag = drop_html_flag
        self.basic_tfidf_ngram_range = basic_tfidf_ngram_range
        self.basic_tfidf_vocabulary_type = basic_tfidf_vocabulary_type
        self.cooccurrence_tfidf_ngram_range = cooccurrence_tfidf_ngram_range
        self.cooccurrence_word_exclude_stopword = cooccurrence_word_exclude_stopword
        self.stemmer_type = stemmer_type

        # transform for count features
        self.count_feat_transform = count_feat_transform

        # create feat folder
        if not os.path.exists(self.feat_folder):
            os.makedirs(self.feat_folder)

        # creat folder for the training and testing feat
        if not os.path.exists("%s/All" % self.feat_folder):
            os.makedirs("%s/All" % self.feat_folder)

        # create folder for each run and fold
        for run in range(1, self.n_runs + 1):
            for fold in range(1, self.n_folds + 1):
                path = "%s/Run%d/Fold%d" % (self.feat_folder, run, fold)
                if not os.path.exists(path):
                    os.makedirs(path)


config = Config(feat_folder='/home/stan/Documents/dev/homedepot/Feat/')
