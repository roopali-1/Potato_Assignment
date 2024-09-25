import pandas as pd
from elasticsearch import Elasticsearch
from dateutil import parser
from tqdm import tqdm

# Connect to the local Elasticsearch instance
es = Elasticsearch(['http://localhost:9201']).options(headers={'Content-Type': 'application/json'})

# Define index name
index_name = 'twitter_data'

# Load the TSV File into a Pandas DataFrame
tweet_file = 'correct_twitter_201904.tsv'  # Update with the actual file path
tweets_df = pd.read_csv(tweet_file, sep='\t')

# Convert timestamp and like count columns
tweets_df['created_at'] = tweets_df['created_at'].apply(parser.parse)
tweets_df['like_count'] = tweets_df['like_count'].fillna(0).astype(int)

# Create an index in Elasticsearch (ignore error if index already exists)
es.indices.create(index=index_name, ignore=400)

# Index the data in Elasticsearch
for _, tweet in tqdm(tweets_df.iterrows(), total=tweets_df.shape[0]):
    doc = {
        'id': tweet['id'],
        'text': tweet['text'],
        'created_at': tweet['created_at'],
        'like_count': tweet['like_count'],
        'place_id': tweet.get('place_id', None),
    }
    # Add explicit document ID if present (tweet['id']) or let Elasticsearch generate one
    es.index(index=index_name, id=tweet['id'], body=doc)

def get_tweets_per_day(term):
    query = {
        "query": {
            "match": {"text": term}
        },
        "aggs": {
            "tweets_per_day": {
                "date_histogram": {
                    "field": "timestamp",
                    "calendar_interval": "day"
                }
            }
        }
    }
    result = es.search(index=index_name, body=query)
    return result['aggregations']['tweets_per_day']['buckets']

def get_unique_users(term):
    query = {
        "query": {
            "match": {"text": term}
        },
        "aggs": {
            "unique_users": {
                "cardinality": {
                    "field": "user_id.keyword"
                }
            }
        }
    }
    result = es.search(index=index_name, body=query)
    return result['aggregations']['unique_users']['value']

def get_avg_likes(term):
    query = {
        "query": {
            "match": {"text": term}
        },
        "aggs": {
            "avg_likes": {
                "avg": {"field": "like_count"}
            }
        }
    }
    result = es.search(index=index_name, body=query)
    return result['aggregations']['avg_likes']['value']

def get_place_distribution(term):
    query = {
        "query": {
            "match": {"text": term}
        },
        "aggs": {
            "places": {
                "terms": {"field": "id.keyword"}
            }
        }
    }
    result = es.search(index=index_name, body=query)
    return result['aggregations']['places']['buckets']


