# Job Scraping Project

## Overview
This project scrapes job listings from [TimesJobs](https://www.timesjobs.com/) based on a user-provided job title. The script collects information such as the company name, job title, location, published date, and a link for more info. All results are saved into a CSV file (`Jobs.csv`).

---

## Features
- Scrape jobs for a specific keyword/job title.
- Filters for recent jobs (posted "few days ago").
- Saves all job listings into a CSV file.
- Error handling for robust web scraping.
- Easy to modify for scraping more pages.

---

## Technologies Used
- Python 3.x
- `requests` for HTTP requests.
- `BeautifulSoup4` for HTML parsing.
- `lxml` parser for speed and reliability.
- `csv` for saving the output data.

---

## Installation

1. Clone this repository:
```bash
git clone <repository_link>
cd job-scraping-project
```

2. Install the required dependencies:
```bash
pip install requests beautifulsoup4 lxml
```

Or using a requirements file:
```bash
pip install -r requirements.txt
```

---

## Project Structure

```
job-scraping-project/
│
├── Main.py              # Entry point of the application
├── Scraper.py           # Handles web scraping logic
├── Parser.py            # Parses HTML content and extracts job data
├── Export_CSV.py        # Manages CSV file operations with deduplication
├── Jobs.csv             # Output file (generated after running)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

---

## Output Format

The CSV file contains the following columns:
- **Company Name**: Name of the hiring company
- **Job Title**: Position title
- **Location**: Job location (when available)
- **Published Date**: When the job was posted
- **More Info**: Direct link to the job posting

Sample output:
```csv
Company Name,Job Title,Location,Published Date,More Info
Adobe Systems Ltd,Machine Learning Engineer,Bangalore,few days ago,https://www.timesjobs.com/job-detail/...
Microsoft India,Senior ML Engineer,Hyderabad,few days ago,https://www.timesjobs.com/job-detail/...
```

---

## Configuration

### Extending Functionality
- **Add more data fields**: Modify `Parser.py` to extract information.
- **Change output format**: Modify `Export_CSV.py` to save in CSV File.
- **Add filters**: Implement additional filtering logic in `Parser.py`.

---

## Error Handling

The script includes robust error handling for:
- Network connectivity issues
- Missing HTML elements
- Invalid user input
- File I/O operations
- Duplicate job entries

---

## Requirements

### Python Dependencies
```txt
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
```

### System Requirements
- Python 3.7 or higher
- Internet connection
- 50MB free disk space (for moderate scraping)

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request


---

## Acknowledgments

- [TimesJobs](https://www.timesjobs.com/) for providing job listings
- BeautifulSoup4 developers for the excellent HTML parsing library
- Python community for the robust ecosystem

---

## Contact

If you have questions or suggestions, please:
- Open an issue on GitHub
- Contact: [mennaabdelgawaad26@gmail.com]
- LinkedIn: [www.linkedin.com/in/menna-abdelgawad-bb19b0279]

---

**⚠️ Disclaimer:** This scraper is for educational purposes. Always check and comply with website terms of service before scraping.
