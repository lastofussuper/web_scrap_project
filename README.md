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
