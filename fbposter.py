
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def main():

	# Your Facebook account user and password
	usr = ""
	pwd = ""
	message = "Queremos invitarlos a la 5ta Reunion de Python Pereira. En esta ocasion contaremos con una interesante charla: Optimizacion Mediante Algoritmos Geneticos por Jonatan Gutierrez. Link Inscripcion: https://www.meetup.com/es/pythonpereira/events/251029709/"
	attach_image = False
	image_path = ""
	group_links = [
		# Your Facebook Groups links.
		# IMPORTANT: You must be a member of the group, being ADMIN nor required.
		"https://www.facebook.com/groups/pythonco/", # A group of python
	]

	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False)

	# Path to geckodriver executable
	driver = webdriver.Firefox(executable_path=r'/home/caro/selenium-fb-group-poster/geckodriver')
	driver.implicitly_wait(15) # seconds

	# Login to Facebook
	driver.get("http://www.facebook.org")
	elem = driver.find_element_by_id("email")
	elem.send_keys(usr)
	elem = driver.find_element_by_id("pass")
	elem.send_keys(pwd)
	c = driver.find_element_by_id('loginbutton')
	c.click()

	for group in group_links:

		# Go to the Facebook Group
		driver.get(group)

		# Click the post box
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		sleep(10)
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")
		post_box=driver.find_element_by_xpath("//*[@name='xhpc_message_text']")

		# Enter the text we want to post to Facebook
		post_box.send_keys(message)
		sleep(15)

		if attach_image:
			# Click on the add media button
			addMedia = driver.find_element_by_xpath("//*[@data-testid='media-attachment-selector']")
			addMedia.click()

			# Provide picture file path
			driver.find_element_by_xpath("//div[text()='Upload Photos/Video']/following-sibling::div/input").send_keys(image_path)

		# Get the 'Post' button and click on it
		post_button = driver.find_element_by_xpath("//*[@data-testid='react-composer-post-button']")
		post_button.click()
		sleep(5)

	# driver.close()

if __name__ == '__main__':
  main()
