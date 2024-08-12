<img src="\Files\BCG X logo.png" width=500 alt="BCG logo"/>
<h1>GenAI Virtual Internship</h1>
<h2>Introduction</h2>

The Gen AI team at Boston Consulting Group has been approached by Global Finance Corp (GFC) to aid in optimizing its time-consuming operations. In the ever-changing financial markets, GFC hopes to be able to quickly analyze corporate financial performance. Hence, they have identified the need for an accurate way to extract, analyze, and present key financial data.

As a junior data scientist at the Boston Consulting Group (BCG) GenAI consulting team, the primary objective is to bring fresh perspectives and innovative solutions to solving GFC’s problems. 

<h2>Project Objective</h2>
Build an efficient, accurate, user-friendly yet scalable chatbot that allows the easy retrieval and analysis of financial documents.

<h2> Data Source </h2>
10-K and 10-Q corporate filings from the SEC EDGAR website

<h2>Summary of Insights</h2>

 - Sourcing the data from the SEC EDGAR website was relatively straightforward for one company, however, for several companies it is time-consuming. The yfinance API connecting to the Yahoo Finance website solved this issue. 
 - Pandas was used to analyze the 10-K and 10-Q data pulled via the yfinance API.
 - Python was used to build the logic and the user interface, where the user will input specific queries. For example, “What is total revenue?” and the correct revenue corresponding to company and year will be returned.
 - The sample data pulled was for Microsoft, Tesla, and Apple for 2021 – 2023. 

<h2>Sample Run</h2>

 - Locate where the Python file (BCG X Chatbot.py) is saved, and ensure you have the libraries `pandas` and `yfinance` installed.

- Run BCG X Chatbot.py, and you should see:
<img src="\Files\level 0.png" width=500 alt="BCG X chatbot startup"/>

- Read the on-screen instructions, and enter one of the ticker symbols - MSFT, TSLA, or AAPL
<img src="\Files\level 1.png" width=500 alt="BCG X chatbot"/>

- Enter a year: 2021, 2022 or 2023
<img src="\Files\level 2.png" width=500 alt="BCG X chatbot startup"/>

- The chatbot was built with the following predefined queries listed below:
1. What is the total revenue?
2. What is the net income?
3. What are the total assets?
4. What are the total liabilities?
5. What is the cash flow from operating activities?
6. How has revenue changed?
7. How has net income changed?
8. How have assets changed?
9. How have liabilities changed?
10. How has cash flow from operating activities changed?

<img src="\Files\level 3.png" width=500 alt="BCG X chatbot startup"/>

- To stop the chatbot from running, enter: exit
<img src="\Files\level 4.png" width=500 alt="BCG X chatbot startup"/>

<h2>Recommendations & Next Steps</h2>

In creating this chatbot, this is a sample of what is possible using if-else logic in Python to map queries to specific answers. To optimize the chatbot, more time should be spent on sourcing company filings to be able to show longer trends. The yfinance API only contains data for three years, and the Edgar package in Python contains more years. 

The if-else logic can be changed to use regular expressions so that the queries can be optimized to look for specific words such as “revenue”, “assets”, and “change”. This will improve the user experience, as users will not have to type out complete sentences to get an accurate response. Functionality can also be introduced that allows comparing financials of multiple companies together to compare performance.

The Generative AI internship at BCG X is a great experience in combining Python, and financial data to create an innovative solution to a client’s business problem. While there are more robust packages out there for natural language processing and GenAI, this internship provides the framework to think through a problem and come up with a practical solution that works.


<img src="\Files\BCG X Certificate.png" alt="BCG certificate"/> 
