import urllib.request
import bibtexparser
from urllib.error import HTTPError

def main(doi):
	BASE_URL = 'http://dx.doi.org/'

	url = BASE_URL + doi
	req = urllib.request.Request(url)
	req.add_header('Accept', 'application/x-bibtex')
	try:
		with urllib.request.urlopen(req) as f:
			bibtex = f.read().decode()
			# The round-trip through bibtexparser adds line endings.
			bibtex = bibtexparser.loads(bibtex)
			bibtex = bibtexparser.dumps(bibtex)
		print(bibtex)
		with open('test.bib', 'w') as f:
			f.write(bibtex)
	except HTTPError as e:
		if e.code == 404:
			print('DOI not found.')
		else:
			print('Service unavailable.')

if __name__ == '__main__':
	main('10.1145/3366423.3380203')