from re import findall
from json import dump

# Define the name of the input file and Assume every line is a different tweet
INPUT_FILE = 'tweets.txt'

# Assume the known racial slurs are in a set and lowercase
racial_slurs = {}


# Define a function that takes a list of tweets as input and calculates the degree of racial slur within
def slur_calc(tweets:list):
    """
    Calculate the degree of racial slur in each tweet and save the results to a JSON file.

    Parameters:
    tweets (list): A list of tweets, where each tweet is a string.

    Returns:
    None
    """
    tweet_dict = {}
    # Loop over each tweet or line
    for tweet in tweets:
        # Tokenize the tweet into words and get the total
        tokenized_words = findall(r'\b\w+\b', tweet.lower())
        # Count all the words in the tweet that are racial slurs
        slur = sum([1 for i in tokenized_words if i in racial_slurs])
        # Assume that degree of profanity of a tweet is number of profane words / number of total words
        deg = round(slur/len(tokenized_words), 2)
        # Append to dictionary with key as tweet and degree as value
        tweet_dict[tweet] = deg
    # Create output JSON file to dump above dictionary
    with open('output.json', 'w') as f:
        dump(tweet_dict, f)


# Read from the input file and run the slur_calc function
if __name__=='__main__':
    with open(INPUT_FILE, 'r') as f:
        # Remove whitespace characters after opening file
        tweets = [line.strip() for line in f.readlines()]
    # Run the above created function
    slur_calc(tweets)