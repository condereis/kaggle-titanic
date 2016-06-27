# Titanic: Machine Learning from Disaster

> The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.

> One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

> In this challenge, we ask you to complete the analysis of what sorts of people were likely to survive. In particular, we ask you to apply the tools of machine learning to predict which passengers survived the tragedy.


This repository contains a suggested solution code for the [Titanic: Machine Learning from Disaster competition](https://www.kaggle.com/c/titanic), hosted by [Kaggle](https://www.kaggle.com/).


## Requirements

To run the project scripts it is required Python 3.5 along with the following packages:
* numpy 1.11.0
* pandas 0.18.1
* scikit-learn 0.17.1
* fancyimpute 0.0.18

To run the project notebooks you should also have the following packages:
* jupyter 4.1.0
* matplotlib 1.5.1
* seaborn 0.7.0


## Setup (Linux, OS X)

### Enviroment
Create an enviroment using [conda](http://conda.pydata.org/docs/) and activate it:
```
$ conda env create -f environment.yml
$ source activate titanic
```

### Files
* Download the [data](https://www.kaggle.com/c/titanic/data).
* Modify SETTINGS.json to point to the training and test data on your system, as well as a place to save the trained model and a place to save the submission.
