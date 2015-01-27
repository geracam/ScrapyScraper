# ScrapyScraper

## Overview

**ScrapyScraper**, a website scraper to return lots of info on the charities hosted on CharityNavigator.


## Technologies Used 

**1.** Scrapy

**2.** Python


## Prerequisites

1. Download all the Scrapy dependencies [here] (<http://scrapy.org/download/>).



## Usage / Features

######ScrapyScraper scrapes over 10,000 websites to attain a charity's:

1. Name
2. Homepage link
3. Overall rating
4. Phone number
5. Address
6. Similar charities
7. Twitter handle



## Installation / Development

To run as-is:

	git clone https://github.com/geracam/ScrapyScraper.git
	
Go to the top level directory and run:

	scrapy crawl initialspider
	
To output to csv run:

	scrapy crawl initialspider -o nameoffileyouwant.csv
	
Read the [documentation] (<http://doc.scrapy.org/en/0.24/>) to learn how to make your own scraper to get data for you easily and quickly.


### Thanks

Thanks to [Charitweet] (<https://www.charitweet.com/>) for letting me do awesome work for this awesome startup.

#### Links and Email

Questions? Email <geracam@mit.edu>. 


> We're entering a new world in which data may be more important than software. -Tim O'Reilly

![data](http://info.discoverelementthree.com/Portals/131252/images/picard-data-meme.png)
