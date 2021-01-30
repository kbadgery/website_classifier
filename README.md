# Website Classifier

In this project I developed an NLP website classification algorithm that processes HTML code and uses it for classification.

I took a small subset of a large dataset that contained class labels for urls. Using these urls, I scraped the html from the associated websites, and used this as the input data for an NLP algorithm. I tested two algorithms, the Naive Bayes, and Support Vector Machine. After Bayesian Hyperparameter Optimization and cross validation, the best performing algorithm was the Support Vector Machine with a cross-validation accuracy of 60.7%. This algorithm went on show an accuracy of 59.0% on the test set.

Further work to improve performance could look at using a larger subset of the dataset for algorithm development, as well as using a more sophisticated algorithm such as transfer learning with a pre-trained neural network with transformer architecture.

# Files in the Repository

This repo contains two python files. 

"Website Classifier Notebook.ipynb" is a Jupyter notebook that contains and explains the entire development process for prototyping and implementing the final website classifier.

"Data_subset_generation.py" is a short script used to downsample the larger dataset I began with. 