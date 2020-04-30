# importing BeautifulSoup from bs4 module
from bs4 import BeautifulSoup as soup
# importing request from urlib module
from urllib.request import urlopen
# importing all from tkinter
import tkinter as tk

# creating window
root = tk.Tk()
# specifying the size  of the window
root.geometry("800x300")
# giving title to our window
root.title("Google News")

# specifying url to retrieve news
news_url = "https://news.google.com/news/rss"
# opening the url
Client = urlopen(news_url)
# reading the site
xml_page = Client.read()
# closing the client
Client.close()

# reading the data using lxml
soup_page = soup(xml_page,"lxml")
# finding news using item as key
news_list = soup_page.findAll("item")

# creating scrollbar
scroll = tk.Scrollbar(root)
scroll.pack(side = 'right', fill='y')

# creating a listbox to display the news
listbox = tk.Listbox(root, yscrollcommand = scroll.set)
for news in news_list:
    listbox.insert(tk.END, "\n"+news.title.text+" "+news.link.text)
listbox.pack(side = tk.TOP, fill = tk.BOTH)
scroll.config(command = listbox.yview)

# creating window loop
root.mainloop()
