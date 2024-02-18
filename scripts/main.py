import pickle
import requests
import argparse
from bs4 import BeautifulSoup

    
def get_quotes(url: str):
    '''
        - The function to scrape data from a given URL.
        - Extract data from the current page.
        - Process and store the data
    '''
    
    req = requests.get(url=url)
    bs = BeautifulSoup(req.text, 'lxml')

    # list tags
    main_div = bs.find(name='div', attrs={'class': 'row large-columns-3 medium-columns- small-columns-1 has-shadow row-box-shadow-1'})
    div_list = bs.find_all(name='div', attrs={'class': 'col post-item'})
    
    if div_list is None:
        return None
    
    quotes_list = []
    for idx, item in enumerate(div_list):

        quote_url = item.find(name='a', attrs={'class': 'plain'})['href']
        
        # quote page
        quotes_page_req = requests.get(url=quote_url)
        quotes_page_bs = BeautifulSoup(quotes_page_req.text, 'lxml')

        # quotes list
        quotes = quotes_page_bs.find_all(name='blockquote')

        # get etch quote
        for idx, quote in enumerate(quotes):

            quote = str(quote.text).strip()
            
            character = quote.split('」 – ')[-1].strip()

            anime = quotes_page_bs.find(name='div', attrs={'class': 'entry-content single-page'})
            anime = anime.find(name='a')['href'].split('.')[0].split('//')[-1].strip()

            result = {
                'Quote': quote,
                'url': quote_url,
                'Character': character,
                'Anime': anime,
            }

            quotes_list.append(result)

    return quotes_list


def get_next_url(url: str):
    '''
        - The function get next page url from current url page and return the get next page url.
    '''
    
    req = requests.get(url=url)
    bs = BeautifulSoup(req.text, 'lxml')

    # get next page url
    try:
        next_page_url = bs.find(name='a', attrs={'class': 'next page-number'})['href']
    except:
        next_page_url = None
    return next_page_url


def main(start_url='https://ja.animemotivation.com/category/quotes/'):
    '''
        - The main function
    '''
    current_url = start_url

    quotes_list = []
    while current_url:

        # Process the data as needed
        data = get_quotes(url=current_url)
        print(f'Length data from {current_url}: {len(data)}')
        quotes_list += data

        # get next url
        next_page_link = get_next_url(url=current_url)

        if next_page_link:
            current_url = next_page_link
        else:
            print("No more pages (-_-)")
            break
    
    return quotes_list


def save(data):
    print(f'save {len(data)} Quotes!')
    with open(f'data/{args.output_file}', 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output-file', type=str, default='AnimeQuotes.pkl', help='output file and ext')
    args = parser.parse_args()
    print(args)

    quotes_info = main()
    save(data=quotes_info)

