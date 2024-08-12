import pandas as pd
import time
db = pd.read_csv(r'C:\Users\Fega Okwa\Desktop\Forage Internships\BCG X Generative AI\Data\10-K data aggregate update.csv')

def simple_chatbot(firm, year, user_query):
    """A function that simulates a chatbot.
    param: firm, firm that data is required on, e.g. MSFT
    param: year, the required year e.g. 2021
    param: user_query, required data e.g. 'What is the total revenue?"
    """
    if user_query == "What is the total revenue?":
        total_revenue = db.query(f"Firm == '{firm}' & Year == {year}")['Total Revenue ($)'].values[0]
        return f"The total revenue for {firm} is ${total_revenue} billion for {year}."

    elif user_query == "What is the net income?":
        net_income = db.query(f"Firm == '{firm}' & Year == {year}")['Net Income ($)'].values[0]
        return f"The net income for {firm} is ${net_income} billion for {year}."

    elif user_query == "What are the total assets?":
        total_assets = db.query(f"Firm == '{firm}' & Year == {year}")['Total Assets ($)'].values[0]
        return f"The total value of assets for {firm} are ${total_assets} billion for {year}."

    elif user_query == "What are the total liabilities?":
        total_liabilities = db.query(f"Firm == '{firm}' & Year == {year}")['Total Liabilities ($)'].values[0]
        return f"The total value of liabilities for {firm} are ${total_liabilities} billion for {year}."

    elif user_query == "What is the cash flow from operating activities?":
        cash_flows = db.query(f"Firm == '{firm}' & Year == {year}")['Cash Flow from Operating Activities ($)'].values[0]
        return f"The cash flow for operating activities for {firm} is ${total_revenue} billion for {year}."

    elif user_query == "How has revenue changed?":
        revenue_change = db.query(f"Firm == '{firm}' & Year == {year}")['Revenue Growth (%)'].values[0]
        return f"Revenue for {firm} changed by {revenue_change}% in {year}."

    elif user_query == "How has net income changed?":
        net_income_change = db.query(f"Firm == '{firm}' & Year == {year}")['Net Income Growth (%)'].values[0]
        return f"Net Income for {firm} changed by {net_income_change}% in {year}."

    elif user_query == "How have assets changed?":
        assets_change = db.query(f"Firm == '{firm}' & Year == {year}")['Change in Assets (%)'].values[0]
        return f"The assets for {firm} changed by {assets_change}% in {year}."

    elif user_query == "How have liabilities changed?":
        liability_change = db.query(f"Firm == '{firm}' & Year == {year}")['Change in Liabilities (%)'].values[0]
        return f"The liabilities for {firm} changed by {liability_change}% in {year}"

    elif user_query == "How has cash flow from operating activities changed?":
        cash_flow_change = db.query(f"Firm == '{firm}' & Year == {year}")['Change in Cash Flow (%)'].values[0]
        return f"Cash flow has changed by {cash_flow_change}% in {year}"

    else:
        return "Sorry, I can only provide information on predefined queries."

def main():
    YEARS = db['Year'].unique()
    FIRMS = db['Firm']. unique()

    while True:

        print('-'*50)
        print('BCG X Financial Chatbot v.1.0\n')
        print('-'*50)

        prompt = "\nEnter the ticker you would like data on. \n"
        prompt += "\n** NOTE: I only contain MSFT, TSLA, and AAPL data **\n"
        prompt += "\nenter 'exit' to quit chatbot: "

        firm = str(input(prompt).upper())

        try:
            if firm.lower() == 'exit':
                break

            else:
                year = int(input("\nEnter a valid year, NOTE: I only have 2021 - 2023 data: "))

            assert firm in FIRMS, 'You have entered an invalid firm'
            assert year in YEARS, 'You have entered an invalid year'

            user_query = str(input('\nEnter a query: '))

            print(f"\nlet me try and retrieve that data... \n")
            time.sleep(2)

            print(simple_chatbot(firm, year, user_query))
        except AssertionError as ErrorMessage:
            print(ErrorMessage)

    print('\nGoodbye, have a nice day!')

if __name__ == "__main__":
    main()