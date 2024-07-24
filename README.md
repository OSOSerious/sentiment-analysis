# Sentiment Analysis Project

This project implements a simple sentiment analysis model using Python and scikit-learn. It classifies text into three categories: positive, negative, or neutral.

## Features

- Text preprocessing (lowercasing, punctuation removal, tokenization, stopword removal)
- Sentiment classification using Multinomial Naive Bayes
- Easy-to-use interface for classifying new text

## Requirements

- Python 3.6+
- pandas
- numpy
- scikit-learn
- nltk

## Installation

1. Clone this repository or download the `sentiment_analysis.py` file.

2. Install the required packages:

   ```
   pip install pandas numpy scikit-learn nltk
   ```

3. Download the required NLTK data:

   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage

1. Run the script:

   ```
   python sentiment_analysis.py
   ```

2. The script will output:
   - Model accuracy
   - Classification report
   - Sentiment prediction for a sample sentence

3. To use the `classify` function in your own code:

   ```python
   from sentiment_analysis import classify

   sentiment = classify("Your text here")
   print(f"The sentiment is: {sentiment}")
   ```

## Customization

- To use your own dataset, modify the `data` dictionary in the script.
- Adjust the `test_size` parameter in the `train_test_split` function to change the ratio of training to testing data.
- Experiment with different classifiers from scikit-learn by replacing `MultinomialNB()`.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/sentiment-analysis/issues) if you want to contribute.

## Author

[Your Name]

## Acknowledgments

- scikit-learn team for their excellent machine learning library
- NLTK project for natural language processing tools
