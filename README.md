# wikihow_scraper
This is a simple wikihow scraper. It takes in a single column CSV of wikihow urls, with first row being 'Url'. It scrapes information from those urls and outputs a csv with the following columns:
Url | Title | Views

## How to use:

### Set-up

* Download, unzip and save wikihow_scraper folder to desktop
* Go to terminal and run the following scripts
`cd Desktop/wikihow_scraper`
`chmod 755 scrape_wiki.command`
* Now you are ready to scrape

### Usage
* Create your csv file of wikihow urls you wish to scrape, and replace the *urls.csv* in the input folder with yours. (Rename your file to the same thing.)
* Once you've done this, just click scrape_wiki.command.
* The resulting table will be in the /output folder!
