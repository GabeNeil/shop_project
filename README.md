# shop_project

Welcome to your new job at Gabetars, Scotland's newest guitar retailer!

You will be using our proprietory inventory app developed by our IT division Gabeabytes. This app allows you to view, add to and edit our current stock and manufacturers. 

The home page gives you general information about the app, the guitar page gives you a list of all our stock and the manufacturers page gives a list of our current manufactuer stockists. 

You can add to both manufacturers and guitars on their respective pages, and and edit or delete each entry individually. 

Best of luck in your new role and please keep drinking at work to a 5 unit maximum. Also don't let any customers play Stairway. 


In order to run this app, you will need to install Flask in the terminal using: 

pip3 install flask 

Then make sure you have psql installed and run it from the terminal at the root folder, and create db guitar_shop. 

Then in the terminal at the root folder: 

psql -d guitar_shop -f db/guitar_shop.sql

Then again in terminal at the root folder: 

python3 console.py

Then at the root folder:

flask run 

The terminal will then give you the url to paste into your browser to view the app. 
