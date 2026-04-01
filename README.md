# Vinted Data Extraction Pipeline

## Overview

This project implements a configuration-driven web scraping pipeline designed to extract structured data (images, titles, and descriptions) from semi-structured e-commerce web pages.

The pipeline focuses on robust data extraction and processing rather than large-scale crawling, with an emphasis on handling real-world HTML inconsistencies and filtering noisy data.

---

## Features

- **Configuration-driven input**
  - Accepts a list of URLs via JSON input
  - Easily extendable to new datasets without code changes

- **Structured data extraction**
  - Extracts:
    - Image URLs
    - Item titles
    - Descriptions

- **Hybrid parsing strategy**
  - Combines:
    - DOM parsing (BeautifulSoup)
    - Regex-based URL extraction
  - Handles cases where structured tags are missing or inconsistent

- **Data cleaning and filtering**
  - Filters relevant image URLs based on:
    - Domain
    - Path structure
    - File type
  - Deduplicates results
  - Selects consistent image sets via pattern matching

- **Automated output generation**
  - Saves:
    - Images locally
    - Title and description as text files
  - Organizes outputs into structured directories
---

## Project Structure
├── web_scrap_project.py # main processing pipeline
├── input_file.json # input URLs
├── read_html.py # HTML parsing experiments
├── download_foto.py # helper scripts
├── test_response.html # sample HTML for debugging

## Project Structure

---

## How It Works

1. Load URLs from a configuration file (JSON)
2. Fetch HTML content using HTTP requests with custom headers
3. Parse HTML using BeautifulSoup
4. Extract candidate URLs via regex
5. Filter and normalize relevant image URLs
6. Extract metadata (title, description)
7. Save structured outputs locally

---

## Challenges & Learnings

- Encountered **anti-bot protection (Cloudflare)** when scraping at scale  
- Observed that modern web platforms often:
  - Obfuscate content
  - Require JavaScript rendering
- Highlighted the importance of:
  - Request headers tuning
  - Retry strategies
  - Alternative extraction approaches

---

## Limitations

- Currently uses synchronous requests (no parallelization)
- No proxy rotation or anti-bot bypass
- Not optimized for large-scale scraping

---

## Future Improvements

- Introduce async scraping (e.g., aiohttp)
- Add retry & rate-limiting mechanisms
- Implement proxy rotation
- Extend to distributed scraping pipelines
- Extract structured data from embedded JSON (e.g., __NEXT_DATA__)

---

## Tech Stack

- Python
- requests
- BeautifulSoup
- regex
- JSON

---
