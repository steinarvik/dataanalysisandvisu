import pdfkit

# Define the URL and the output file path
url = 'https://en.wikipedia.org/wiki/Elephant'
output_file = 'output.pdf'

# Convert the URL to a PDF
pdfkit.from_url(url, output_file)

print(f'Webpage saved as PDF: {output_file}')