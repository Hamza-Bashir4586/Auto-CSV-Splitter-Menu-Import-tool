# Auto-CSV-Splitter-Menu-Import-tool
The project centered around processing large CSV files into the right format when customers uploaded their products to their Epos Now Account, using Python for processing, and PyGUI for graphical interface

##Customers using the EposNow platform somtimes used our Bulk Import tool in order to upload the products that they wanted to sell to our POS software. 
- But, our Legacy Bulk Import tool only accepted a certain format and upto a certain number of rows (4,000), with each file needing certain headers in order to be recognized by our system.
  - so in my spare time I made this tool to help me and some of my peers work with these customer imports

- The tool I made allows you to upload an existing, filled out product import csv file that is over 4,000 rows and splits the content in intervals of 4,000 each, and also ensures that the correct headers are placed on the first row of each file

- the tools creates a new folder within the downloads area of file explorer and puts all the new split files in there

- and then agents can just upload each file one after another into the the legacy bulk import tool
