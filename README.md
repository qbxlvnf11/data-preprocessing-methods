
It is posted by Yong (예비개발자).

Blog URL: https://blog.naver.com/qbxlvnf11

LinkedIn: https://www.linkedin.com/in/taeyong-kong-016bb2154


- Upload data processing methods
- Upload code as a Jupiter Notebook file (.ipynb) for immediate understanding


Contents
=============

- Image Processing
  - Gamma Encoding
  - TORCHVISION.TRANSFORMS (Resize, Center Crop, Normalize)
- NLP
  - Preprocessing (Lemmatization, Stemming, POS Tagging ...), TF-IDF, Graphization etc.
    - Graphization: representing language as graph structure
      - Node: 1-gram TF-IDF
      - Edge: 2-gram counting
  - Usage of TorchText in Pytorch
  
Datasets
=============

- UCSD Anomaly Detection Dataset

http://www.svcl.ucsd.edu/projects/anomaly/dataset.htm

- MetaLWOz (Multi-Domain Dialogs for the Fast Adaptation of Conversation Models)

https://www.microsoft.com/en-us/research/project/metalwoz/

- Sentiment-Analysis-Dataset

http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip

References
=============

- Gamma_encoding

https://docs.opencv.org/3.4/d3/dc1/tutorial_basic_linear_transform.html

- NLTK

https://www.nltk.org/

- TorchText

https://medium.com/@sonicboom8/sentiment-analysis-torchtext-55fb57b1fab8

https://simonjisu.github.io/nlp/2018/07/18/torchtext.html

Code correction
=============

- News_classifier_recurrent_convolution.ipynb

[29] block: 

y_train = np.expand_dims(X_train, -1) -> y_train = np.expand_dims(y_train, -1)

y_test = np.expand_dims(X_test, -1) -> y_test = np.expand_dims(y_test, -1)


- News_classifier_bidirectional_LSTM.ipynb

[29] block: 

y_train = np.expand_dims(X_train, -1) -> y_train = np.expand_dims(y_train, -1)

y_test = np.expand_dims(X_test, -1) -> y_test = np.expand_dims(y_test, -1)
