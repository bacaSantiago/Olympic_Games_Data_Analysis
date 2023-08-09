# Olympic Games Data Analysis

Welcome to the Olympic Games Data Analysis project! This Python code processes and analyzes data from the Summer Olympic Games using a CSV file. The code provides various interactive options to retrieve information about disciplines, sports, medals, athletes, and countries involved in the Olympics between the years 1896 to 2012.

## How it Works

1. **Data Loading**: The code reads data from a CSV file containing information about Olympic events, athletes, medals, and more.

2. **Data Conversion**: The `dataConverter(database)` function processes the raw data from the CSV file into a more accessible format.

3. **Options**: The code offers multiple options for interacting with the data:

   - **Option 1**: Get a list of disciplines participated in the Olympics between two given years.
   - **Option 2**: Get a list of sports (without duplicates) in the Olympics between two given years.
   - **Option 3**: Display the total medals won by sport in a given year.
   - **Option 4**: Display a list of Mexican medal winners based on medal type (Gold, Silver, Bronze).
   - **Option 5**: Calculate the athlete with the most wins in Olympic history and display their achievements.
   - **Option 6**: Generate a bar graph of the top 7 countries with the highest number of medals.
   - **Option 7**: Create a pie chart of the top 7 countries with the most Olympic medalists in Boxing.

4. **Main Function**: The `main()` function provides an interactive menu to select and execute desired options.

## How to Use

1. Ensure you have the required libraries (`csv`, `matplotlib`, `collections`) installed.
2. Copy and paste the provided code into your Python environment.
3. Update the `file` variable with the correct path to your CSV file containing Olympic data.
4. Run the code and follow the on-screen prompts to explore the available options.
5. Select an option by entering the corresponding number.

## Dependencies

- [CSV Library](https://docs.python.org/3/library/csv.html)
- [Matplotlib](https://matplotlib.org/stable/contents.html)
- [Collections Library](https://docs.python.org/3/library/collections.html)

## Resources

The data used for this analysis is assumed to be stored in a CSV file named `3_summer_olympics.csv`. Modify the file path in the script if necessary.

Feel free to modify and extend this code to perform more in-depth analyses of the Olympic data or to integrate it with other sources for a comprehensive understanding of Olympic history.