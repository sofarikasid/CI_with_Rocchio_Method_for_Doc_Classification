The dataset consists of an already processed set of 2225 documents from the BBC news website corresponding to stories in different topical areas from 2004-2005. Each document belongs to one of 5 classes (business, entertainment, politics, sport, tech).

Each document is represented as a feature vector over a set of 6167 features (after tokenization, stop word removal, stemming, and frequency filtering). The data has already been randomly split (80%, 20%) into training and test data both of which are provided in document-by-term matrix format containing a row for each document and a column for each  feature in the vocabulary (note, however, that the first column of each row in the train and test files represents the document id in the original dataset, and this column should be removed to get the doc-term frequency matrices). The class labels for instances (documents) in the training and the test data are provided in separate files. Also, the set of features used in the data (representing the columns in the train and test matrices) is provided as a separate file 

The files contained in the zip archive are as follows:

1. BBC_News_5_Train.csv: This file contains the document-term frequency matrix for the training documents. The first value in each row corresponds to the document id in the original data and is not part of the document-term matrix. Once the document id column is removed, each row of the matrix corresponds to one document and each column corresponds to one feature and the (i,j)th element of the matrix shows the raw frequency of the jth feature in the ith document. This matrix contains 1780 rows (80% of the full document set) and 6167 columns (representing features).

2. BBC_News_5_Test.csv: This file contains the document-term frequency matrix for the test documents. The format is as in the training file, but containing 445 rows (20% of the full document set) and 6167 columns (representing features).

3. BBC_News_5_Train_Labels.csv: This file contains the category/class labels associated with each training document. Each line contains a class label (on of ) for a document in the corresponding row in BBC_News_5_Train.csv. For example, the class label "business" in the 4th row is the label for the document in the 4th row of the training data (document with id 320. 

4. BBC_News_5_Test_Labels.csv: Similar to the training labels, but in this case the lines contain class labels for the 445 test documents in the file BBC_News_5_Test.csv. 

5. BBC_News_5_Features.csv: This file contains the set of 6167 features in the vocabulary. Each line contains a feature and corresponds to the corresponding columns in training and test document-term frequency matrices. 

6. bbc-5categories.csv: This file contains the full unprocessed data, including the document and category ids, the titles and the full text of the articles. The document ids in this file correspond to the document ids in the first columns of the training and test files (BBC_News_5_Train.csv and BBC_News_5_Test.csv). Note that this file is not needed for the assignment (neither are the document ids in the training and test files). However, it is made available for your reference in case you are interested in exploring the actual documents before they were preprocessed.

