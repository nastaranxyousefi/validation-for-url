import validators

with open('urls.txt') as file:
    lines = file.readlines()
    
    for line in lines:
        url = line.strip()
        if validators.url(url):
            print(f'valid url {url}')
        else:
            print(f'invalid url {url}')

    