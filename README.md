# Sentiment Analysis Tool for Beginners

## What is this?
This is a computer program that can read a sentence and guess if it's happy, sad, or neutral.

## Why is it useful?
It can help you understand how people feel about your product or service by looking at their comments.

## What do I need to use it?
- A computer
- Python (a type of computer language) installed on your computer
- Some extra Python tools (we'll show you how to get them)

## How do I set it up?
1. Download all the files from this project to your computer
2. Open a program called "Command Prompt" or "Terminal"
3. Type this and press Enter: `pip install -r requirements.txt`
4. Type these two lines (press Enter after each):
   ```
   python -c "import nltk; nltk.download('punkt')"
   python -c "import nltk; nltk.download('stopwords')"
   ```

## How do I use it?
1. Open "Command Prompt" or "Terminal" again
2. Go to the folder where you saved the files
3. Type `python sentiment_analysis.py` and press Enter
4. The program will run and show you how well it's working

## What if I want to analyze my own text?
At the end of the `sentiment_analysis.py` file, you'll see this:
```python
new_text = 'I really enjoy using this service!'
print(f'Sentiment: {predict_sentiment(new_text)}')
```
Change the text inside the quotes to whatever you want to analyze.

## Need help?
If you're stuck, don't worry! Contact us at [Your Email/Contact Info] and we'll help you out.
