from selenium import webdriver
from bs4 import BeautifulSoup
import time
from . import maps

def is_int(input):
	try:
		int(input)
	except ValueError:
		return False
	return True

def urlCreate(brandid, modelid, gearid, year, fuelid):
	
	url = "https://www.cars.bg/?go=cars&search=1&advanced=&fromhomeu=1&currencyId=1&autotype=1&stateId=1&section=home&categoryId=0&doorId=0&brandId=" + brandid + "&modelId=" + modelid + "&fuelId=" + fuelid + "&gearId=" + gearid + "&yearFrom=" + year + "&yearTo=" + year + "&priceFrom=&priceTo=&man_priceFrom=&man_priceTo=&regionId=0&offersFor4=1&offersFor1=1&filterOrderBy=1"
	return url


def urlsCreate():
	start = time.time()
	urls = list()
	index = 0
	for brand, brandid in maps.brandId.items():
		for model, modelid in maps.globalsFromMaps[brand].items():
			for gear, gearid in maps.gearId.items():
				for fuel, fuelId in maps.fuelId.items():
					for yearid in maps.yearid:


						if yearid < 2006 and fuelId == 7:
							pass
						else:
							url = urlCreate(str(brandid), str(modelid), str(gearid), str(yearid), str(fuelId))
							info = [str(brand), str(model), str(gear), str(yearid), str(fuel)]
							urls.append([url, info])
	return urls

def scraper(url, info):
	#print(info)
	__author__ = "Engine Bai"
	driver = webdriver.Chrome(executable_path=r"C:/Users/PC-Admin/Desktop/work/projectglade/cars/carscompare/scraper/chromedriver.exe")
	driver.get(url)
	content_element = driver.find_element_by_tag_name("body")
	content_html = content_element.get_attribute("innerHTML")

	soup = BeautifulSoup(content_html, "html.parser")
	prices = soup.find_all(name = "span", attrs = {"class" : "ver20black"})

	if soup and prices:

		for i in range(len(prices)):
			prices[i] = prices[i].strong


		a = 0
		pricesList = []
		for j in range(len(prices)):
			for i in range(len(prices[j].text)):
				if is_int(prices[j].text[i]):
					a *= 10
					a += int(prices[j].text[i])
			pricesList.append(a)
			a = 0


		prices = 0
		for i in pricesList:
			prices += i

		prices //= len(pricesList)
		

	driver.close()
	return prices, info

		

	