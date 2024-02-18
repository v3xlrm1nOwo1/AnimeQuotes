




# Anime Quotes Dataset – アニメの名言データセット 🌸

> Welcome to Anime Quotes Dataset

<div align="center">
    <picture>
        <source 
        srcset="assets/Hachiman Hikigaya.jpg"
        media="(prefers-color-scheme: dark)"
        />
        <source
        srcset="assets/Hachiman Hikigaya.jpg"
        media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"
        />
        <img src="assets/Hachiman Hikigaya.jpg" width="100%" height="350px" />
    </picture>
</div>

## Overview
This dataset contains a curated collection of inspiring and memorable quotes from various anime series, sourced from the [Anime Motivation](https://ja.animemotivation.com) website. The quotes are stored as a list of dictionaries and can be easily accessed for analysis, research, or personal enjoyment.
<p>Can you find this dataset in my Huggingface account <a href="https://huggingface.co/v3xlrm1nOwo1">v3xlrm1nOwo1</a>.</p>


## Data Format

Each entry in the dataset is represented by a dictionary with the following fields:

- `Quote`: The text of the quote.
- `Character`: The name of the character who said the quote.
- `URL`: The source URL of the quote.


## Usage

```python
import pickle
import random

# Load the dataset
with open('data/AnimeQuotes.pkl', 'rb') as file:
    anime_quotes = pickle.load(file)

# Access a random quote
random_quote = random.choice(anime_quotes)

print(f'Quote: {random_quote["Quote"]}')
print(f'Character: {random_quote["Character"]}')
print(f'URL: {random_quote["URL"]}')
```


## Contributions
We welcome contributions and feedback to make the Anime Quotes Dataset even more fantastic! Whether you're adding new quotes, enhancing existing ones, or providing valuable feedback, your input is highly appreciated.


## Acknowledgments
A special thanks to [Anime Motivation](https://ja.animemotivation.com) for the inspiration and quotes that make this dataset truly special.


## License
This dataset is provided under the [Apache License 2.0](LICENSE). Feel free to use, modify, and share it.


> Dive into the Anime Quotes Dataset and let the enchanting magic of anime wisdom unfold! 🌌✨🚀


