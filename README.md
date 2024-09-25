# POTATO - Twitter Data Analysis

## Assignment Overview

The POTATO assignment involves analyzing Twitter data using Python, Elasticsearch, and Streamlit. The goal is to ingest, index, and query tweet data, allowing users to explore various metrics related to specific search terms. This project demonstrates the ability to handle data ingestion, indexing, and building an interactive user interface for data analysis.

## Approach to the Solution

### 1. Data Ingestion and Indexing
- **Loading Data:** We begin by loading a TSV file containing tweet data into a Pandas DataFrame.
- **Indexing with Elasticsearch:** The tweet data is indexed in an Elasticsearch instance to facilitate efficient querying. Each tweet is stored with relevant fields such as user ID, tweet text, timestamp, like count, and place ID.

### 2. Querying the Data
We defined several functions to perform specific queries on the indexed data:
- **Tweets per Day:** Aggregates the count of tweets containing a specific term, grouped by date.
- **Unique Users:** Counts the number of unique users who posted tweets with the specified term.
- **Average Likes:** Calculates the average number of likes for tweets containing the term.
- **Place Distribution:** Analyzes the distribution of tweets by location.

### 3. Building the Streamlit User Interface
A user-friendly interface was created using Streamlit, allowing users to:
- Input a search term.
- Display the results for various metrics, including tweets per day, unique users, average likes, place distribution, time of day distribution, and the top user.

## Installation

### Prerequisites
Before running the application, ensure you have the following installed:

- **Docker:** To run Elasticsearch locally.
- **Python:** Version 3.7 or higher.

### Setting Up Elasticsearch
1. Pull the Elasticsearch Docker image:
   ```bash
   docker pull elasticsearch:7.10.1
