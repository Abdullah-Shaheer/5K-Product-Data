# H&M Product Scraper

This project was developed to scrape H&M's product data from their API, extracting information about products such as names, prices, sizes, and other relevant details. The data was scraped from 150 pages, retrieving up to 5,000 product records.

---

## 🚀 Project Overview  
- **API Endpoint:** `https://api.hm.com/search-services/v1/en_us/search/resultpage`  
- **Objective:** To scrape product details from H&M and compile the data into CSV, Excel, and JSON formats.  
- **Total Pages Scraped:** 150  
- **Total Records:** 5,000  

---

## 🛠️ Technologies Used  
- **Programming Language:** Python 🐍  
- **Libraries & Tools:**  
  - `requests`: For sending HTTP requests to the H&M API.  
  - `pandas`: For handling and processing the scraped data.  
  - `json`: For parsing and saving the response data.  
  - `csv`: For saving the scraped data in CSV format.  
  - `openpyxl`: For working with Excel files.  

---

## ⚙️ Features  
- **Efficient API Scraping:** Scraped data directly from the H&M API using asynchronous requests.  
- **Data Formats:** Provided the final data in **CSV**, **Excel (XLSX)**, and **JSON** formats.  
- **Pagination Support:** Handled the 150 pages of product listings for large-scale data extraction.  
- **Data Filtering:** Cleaned and filtered the data to extract the most relevant fields like product name, price, availability, and size.  

---

## 📊 Data Fields Scraped  
The following product details were scraped from the API:  
- **Product Name**  
- **Price**  
- **Availability**  
- **Size Information**  
- **Product Category**  
- **Product Description**
- **And many more**

---

## 📝 Steps Followed  
1. **API Request:** Sent requests to the H&M API, passing the required parameters to retrieve product data.  
2. **Pagination Handling:** Iterated over 150 pages using a loop to scrape all product records.  
3. **Data Extraction:** Parsed the JSON response to extract the relevant product information.  
4. **Data Cleaning:** Removed any unnecessary or redundant data and ensured the scraped data was accurate.  
5. **Output:** Saved the final data in **CSV**, **Excel (XLSX)**, and **JSON** formats for easy use by the client.  

---

## 🏆 Client Feedback  
- **Result:** 5,000 product records delivered on time.  
- **Client’s Reaction:** *"The scraper worked as expected, and the data was exactly what we needed in multiple formats. Great work!"*  

---

## 📂 File Structure  
- `main.py`: Main script for scraping H&M product data.  
- `products.csv`: Final CSV file with the scraped data.  
- `products.xlsx`: Excel file containing the scraped product details.  
- `products.json`: JSON file with the product data.
---

## 💬 Connect with Me  

If you need help with similar projects or have any custom scraping requirements, feel free to reach out:  
📧 Email: abdullahshaheer17398@gmail.com  
🌐 GitHub: [Abdullah Shaheer](https://github.com/Abdullah-Shaheer)

