
# Amazon Product Data Scraper

## Description
This Python script retrieves detailed product data using the Amazon Standard Identification Number (ASIN) from Amazon's website. It is capable of extracting information such as the title, subtitle, description, price, and other product details.

## Installation
Ensure you have Python installed on your system. You will also need the `requests` and `beautifulsoup4` libraries.

To install the dependencies, run:
```
pip install requests beautifulsoup4
```

## Usage
The script can be executed with Python. You need to provide the product's ASIN and the language code of the Amazon site (e.g., "fr" for Amazon France).

Example of use:
```python
asin = "B00IKI352E"
language = "fr"
result = asinResolver(asin, language)
print(result)
```

The script will extract the product information and print it in JSON format.

## Features
- Extracting product details from Amazon using ASIN.
- Supports different Amazon domains based on language.
- Retrieves various information such as title, description, price, etc.

## Warnings
- This script is intended for educational and research purposes only.
- Web scraping may be against the terms of use of the website, use this script responsibly.

## License
This project is under a free license. You are free to use and modify it for your personal needs.

## Requirements
This project requires the following libraries:

- requests==2.31.0
- beautifulsoup4==4.12.2

Make sure to install these with the command:
```
pip install -r requirements.txt
```
