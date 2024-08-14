# SafeSurf
Empowering Digital Safety

![image](https://github.com/user-attachments/assets/e9ccda12-d548-4bda-b22e-bc796f8b7951)

Innovative-product-Development- We have developed a machine learning-powered browser extension to clarify website data collection practices. By analysing and simplifying complex privacy policies, our tool helps users understand data collection, storage, sharing, and risks, empowering them to make informed decisions and control their online privacy.

To create a detailed workflow pipeline showing the connections and interactions between your code files along with line references where these connections occur, I will analyze the content of the key Python files (main.py, fire_db.py, scraper.py, and others) that you uploaded. This analysis will outline how data flows through these files, which files are responsible for input, processing, and output, and the exact lines where these interactions are coded.

Code Files for Detailed Analysis:
main.py - Typically, this file orchestrates the high-level flow of the application.
fire_db.py - Manages database operations.
scraper.py - Handles the scraping of web content.
utils.py - Provides utility functions, possibly for data processing.
report.py - Likely generates reports or summaries.
score.py - Responsible for scoring, possibly evaluating the data or results.
stream.py - Manages streaming or real-time data updates.
I will now extract the contents of these files and analyze them to determine the interactions and data flow, identifying the line references where these files connect with each other. Let's start by extracting and reviewing the content of these Python files to identify their specific functionalities and connections.

Based on the detailed analysis of your Python code files, here is a comprehensive workflow pipeline that describes the interactions between different components of your project:

Workflow Pipeline Overview:
main.py: Acts as the central orchestrator for handling HTTP requests, interacting with other modules to process data, and updating the database based on user inputs.
fire_db.py: Manages Firebase database initialization and provides utility functions for database interactions.
scraper.py: Responsible for scraping data from websites using HTTP requests.
utils.py: Provides utility functions including HTML parsing, data cleaning, and dividing text into question and answer formats.
report.py: Uses data processed by utils.py to generate reports and applies scores using score.py.
score.py: Computes readability and other text-based scores.
stream.py: Handles real-time data fetching and updates using Streamlit.
Detailed Workflow with Code Interactions:
HTTP Request Handling (main.py):

Receives user input via HTTP GET requests.
Invokes scraper.py to scrape data based on URL.
Uses utils.py to process the scraped HTML.
Generates reports using report.py which in turn utilizes score.py for scoring.
Updates the Firebase database using methods defined in fire_db.py.
Firebase Database Operations (fire_db.py):

Initializes Firebase connection and provides a function to get database references【37:1†source】.
Web Scraping (scraper.py):

Scrapes website data using requests and BeautifulSoup【37:2†source】.
Processes HTML content to extract required information【37:2†source】.
Utility Functions (utils.py):

divideIntoQnA: Divides HTML content into a structured format of questions and answers【37:3†source】.
getHTML: Fetches HTML content for a given URL【37:17†source】.
Report Generation (report.py):

Calls utils.summarize to summarize content and uses score.py to assign readability scores【37:4†source】.
Scoring (score.py):

Calculates various readability scores and returns them to report.py for inclusion in the final report【37:5†source】.
Real-time Data Streaming (stream.py):

Fetches and displays data in real-time using Streamlit, directly interacting with Firebase to retrieve data【37:6†source】.
Code Line References:
main.py interacts with Firebase through fire_db.py for database operations at lines where Firebase is initialized and where data updates are handled.
scraper.py is invoked from main.py when URLs need to be processed, specifically in the route handling functions.
utils.py functions are called from main.py to process the scraped HTML.
report.py and score.py are linked where report.py calls scoring functions from score.py to evaluate the text.
stream.py operates independently for real-time updates but fetches data from Firebase initialized in fire_db.py.
This detailed pipeline connects your project's components based on their functionality and code interactions. If you need the exact line numbers for these interactions or further details on any part, please let me know!

Output at Firebase

![image](https://github.com/user-attachments/assets/f0aa199b-ad10-4875-a7a9-7ae4b7aa664e)
Final Outputs These below outputs are for various websites
![image](https://github.com/user-attachments/assets/27a53f93-688e-4b50-9b66-75422f3a5125)
![image](https://github.com/user-attachments/assets/3bf20861-3c27-49d4-aeef-f9e18b6ff74c)



