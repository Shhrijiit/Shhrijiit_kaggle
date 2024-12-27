EDA      ~Mayur Khade
1. As my contribution in this group project I  helped with dataset loading, checking missing values and duplicate values.
2. I worked on EDA part by visualizing the target column and checked if there was any imbalance data.
3. Visualised Target distribution in Keywords and plotted a histogram with respect to length of words in disastrous and non-disastrous tweets.


Preprocessing       ~Shhrijiit Laware
 1. Initially checked examples of the tweets in both target categories.
 2. Performed comprehensive text cleaning (URL/special character removal, stopwords filtering), tokenization.
 3. Tried stemming and lemmatization; it was found that lemmatization worked better so went ahead with lemmatization and dropped stemming.
 4. Plotted a word cloud with respect to both categories i.e. disastrous and non-disastrous tweets and it gave an overview of the
    most frequent words in the tweets respectively.


Model Training using TF-IDF        ~Swapnajeet Harne
1. I used TF-IDF for converting text to array.
2. Trained RandomForest, XGBoost, Multinomial Naive Bayes and Logistic Regression models on the data.
3.Most models were found to overfit the data
4.The highest accuracy with minimum variance (8%) between training and testing was given by Logistic Regression model:
 Logistic Regression                              Train Accuracy: 0.87
                                                  Test Accuracy: 0.79




Model Training using Word2vec       ~Satish Ghodke
1. I used Word2vec approach for converting text to array.
2. Performed Min-Max Scaler on the data.
3. Trained RandomForest, XGBoost, Multinomial Naive Bayes and Logistic Regression models on the data.
4. All models were overfitting on the data



Models trained using TF-IDF were found to be performing better than the word2vec so we chose to use Logistic Regression with TF-IDF to predict the test values.



Preprocessing test data and predicting Test-Target           ~Himanshu Waghmare
1. Preprocessed Test data
2. Trained Logistic Regression with 100% Train data
3. Predicted the target variable
4. Saved the target values to .csv
   
 
