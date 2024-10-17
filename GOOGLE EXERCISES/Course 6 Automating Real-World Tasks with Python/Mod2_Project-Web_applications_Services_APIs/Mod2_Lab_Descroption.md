### Processing Text Files with Python Dictionaries and Uploading to Running Web Service
#### Task: 
You're working at a company that sells second-hand cars. Your company constantly collects feedback in the form of customer reviews. Your manager asks you to display those reviews (saved as .txt files) on your company's website. To do this, you'll need to write a script to convert those .txt files and process them into Python dictionaries, then upload the data onto your company's website (currently using Django).
#### What you'll do
Use the Python OS module to process a directory of text files
Manage information stored in Python dictionaries
Use the Python requests module to upload content to a running Web service
Use the basic operations for Python requests like GET and POST methods
Is that clear?
More details will follow.
……………………………………………………………………………………….
For this task, a Django web server corpweb is already configured under the “/projects/corpweb” directory.
The whole website is stored in “/projects/corpweb”.
You'll find a few .txt files with customer reviews for the company in the “/data/feedback” directory.
The files are written in the same format (i.e. title, name, date, and feedback).
Please write a Python script that uploads all the feedback stored in this folder to the company's website, without having to turn it into a dictionary one by one.
Is that clear?
More details will follow.
…………………………………………………………………………….

### The script should now follow the structure:

- List all .txt files under the “/data/feedback” directory that contains the actual feedback to be displayed on the company's website.
Hint: Use the  “ os.listdir()” method for this, which returns a list of all files and directories in the specified path.
You should now have a list that contains all of the feedback files from the path “/data/feedback”. Traverse over each file and, from the contents of these text files, create a dictionary by keeping “title”, “name”, “date”, and “feedback” as keys for the content value, respectively.
Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
Use the Python requests module to post the dictionary to the company's website. Use the “request.post()” method to make a POST request to “http://34.70.157.116/feedback”. Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on. You can also use the response status_code 201 for created a success status response code that indicates the request has succeeded.
………………………………………………………
