# homedepot

For some reason making features using their small set doesn't complately clog my laptop so I'll halt trying to set it up on a remote worker. It may be needed when we try to create features from larger sets.

The project is a mess right now, but have a look if you enjoy pain and suffering.
I set it up to run on linux, but the original project was done on windows so it might be easier for you to try to run their original setup.

An incomplete list of steps to run it is:

Set up a virtual enviornment. I use conda virtual env. Use python 2. You can set this up with pycharm in project interpreter menu.

activate virtual environment in console by: source activate __your_virtual_environment_name__

run: pip install -r requirements.txt. This will install the requirements i specified in the file. if some of them won't install try installing them manually

look through scripts and see if all packages are recognized. if not pip install them

in console type:

  python
  
  import nltk
  
  nltk.download()
  
a menu will showup, download stopwords and wordnet datasets. chose default directory

download competition data to input folder

set paths to your project in config.py.

run with python (in console):

  export_tr_te.py
  
  preprocess.py
  genFeat_<feature name>.py
  
  combine_feat_[svd100_and_bow_Jun23]_[Low].py
  
  python train_model.py [Pre@solution]_[Feat@svd100_and_bow_Jun23]_[Model@reg_xgb_linear]
  
  
by no means will it be smooth :)
