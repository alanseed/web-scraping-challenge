# web-scraping-challenge  
This challenge scapes images and data on Mars off a number of sites, saves the data in a database and renders the data on an HTML page.   
The source of the data is  
* NASA Mars News https://redplanetscience.com/ 
* JPL Mars Space Images - Featured Image https://spaceimages-mars.com/ 
* Galaxy Facts on mars https://galaxyfacts-mars.com/ 
* Astropedia images of the hemispheres https://marshemispheres.com/  

## Dependencies  
* mongoDB 1.28.1 
* PyMongo 3.12.0  
* Flask 2.0.x
* Pandas 1.3.1
* Splinter 0.14.0
* Beautiful Soup 4.9.0 
* webdriver-manager 3.4.2
* Bootstrap 5.0

## Usage  
Open a bash terminal and run ```python app.py``` to start the API server   
Open a web browser page at http://127.0.0.1:5000/ to view the latest data    
Click on the "Scrape new data" button to get the latest news and images   

## Files  
The following files are found in the project
* ```app.py``` The application that runs the api to serve the data
* ```scrape_mars.py``` The python script to scape the data 
* ```mission_to_mars.piynb``` The jupyter notebook used to test the scraping code 
* ```.gitignore``` Ignore the temporary files in the directory 
* ```/templates/index.html``` The template for the web page to display the data 

## Design Considerations  
The scraping for each web site is a separate function and all are called by the update button. The only volatile data comes from the NASA web stite and the mars image from JPL is updated from time to time. It would be more effiecient to redesign the database so that the NASA data can be updated only, since the scraping takes some time to complete.  

The database includes the time of the last update and returns the most recent data, or the web sites are scraped if the database is found to be empty.  

The HTML is based entirely on the bootstrap 5 library and uses cards for all the elements on the page so the page has a consistent look and feel. 


