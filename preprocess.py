import pandas as pd
from config import config
import cPickle  # import pickle as cPickle
import numpy as np
from nlp_utils import clean_text, pos_tag_text

# from cloud.serialization.cloudpickle import dumps as cPickle


##
# Load Data #
##

print("Load data...")
dfTrain = pd.read_csv(filepath_or_buffer=str(config.original_train_data_path), encoding="utf-8").fillna("")  # TODO: !!!
dfTest = pd.read_csv(filepath_or_buffer=str(config.original_test_data_path), encoding="utf-8").fillna("")# !!!
num_train, num_test = dfTrain.shape[0], dfTest.shape[0]
print("Done.")

###
# Pre-process Data #
###
print("Pre-process data...")

print("insert fake label for test")
dfTest["median_relevance"] = np.ones(num_test)
dfTest["relevance_variance"] = np.zeros(num_test)

print("insert arbitrary index to dataframes")
dfTrain["index"] = np.arange(num_train)
dfTest["index"] = np.arange(num_test)

print("one-hot encode the median_relevance")
for i in range(config.n_classes):
    dfTrain["median_relevance_%d" % (i + 1)] = dfTrain["median_relevance"].map(lambda x: 1 if x == (i + 1) else 0)

print("create query ids dict")
qid_dict = dict()
for i, q in enumerate(np.unique(pd.concat([dfTrain["query"], dfTest["query"]], axis=0, ignore_index=True)), start=1):
    qid_dict[q] = i

print("insert query id")
dfTrain["qid"] = map(lambda q: qid_dict[q], dfTrain["query"])
dfTest["qid"] = map(lambda q: qid_dict[q], dfTest["query"])

print("clean text")
clean = lambda line: clean_text(line, drop_html_flag=config.drop_html_flag)
dfTrain = dfTrain.apply(clean, axis=1)
dfTest = dfTest.apply(clean, axis=1)

print("Done.")

##
# Save Data #
##
print("Save data...")

with open(config.processed_train_data_path, "wb") as f:
    cPickle.dump(dfTrain, f, -1)
with open(config.processed_test_data_path, "wb") as f:
    cPickle.dump(dfTest, f, -1)

print("Done.")

"""
# pos tag text
dfTrain = dfTrain.apply(pos_tag_text, axis=1)
dfTest = dfTest.apply(pos_tag_text, axis=1)
with open(config.pos_tagged_train_data_path, "wb") as f:
    cPickle.dump(dfTrain, f, -1)
with open(config.pos_tagged_test_data_path, "wb") as f:
    cPickle.dump(dfTest, f, -1)
print("Done.")
"""
