import pdfkit
from urllib.parse import urlparse
import re

# Function to create a safe filename from a URL
def create_safe_filename(url):
    # Replace '://' with '__' and other unsafe characters with '_'
    safe_filename = re.sub(r'[^a-zA-Z0-9]', '_', url)
    return safe_filename + '.pdf'

# Read URLs from a text file
def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return urls

# Convert each URL to a PDF and save with a safe filename derived from the URL
def convert_urls_to_pdfs(urls):
    for url in urls:
        output_file = create_safe_filename(url)
        try:
            pdfkit.from_url(url, output_file)
            print(f'Successfully saved {url} as {output_file}')
        except Exception as e:
            print(f'Failed to convert {url} to PDF: {e}')


# Path to the file containing URLs
input_file_path = 'urls.txt'  # Update this with the actual path to your URLs file

# Read URLs from the file
urls = read_urls_from_file(input_file_path)

# Convert URLs to PDFs
convert_urls_to_pdfs(urls)
