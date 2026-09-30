WE SHALL UPLOAD OUR PROJECT WORK ONCE WE ARE DONE WITH OUT PROTOTYPE.
AS OF NOW, WE HAVE UPLOADED THE FILES OF CONCEPTS RELATED TO MONGO SKILLS AND ALSO ATTACHED A PPT RELATED TO OUR PROJECT.
# MongoDB Advanced Concepts Hackathon

A hands-on demonstration of MongoDB and its advanced database capabilities using Python and PyMongo.

## Overview

This repository demonstrates fundamental and advanced MongoDB concepts through practical Python programs.

The project uses a MongoDB database named:

`mongodb_hackathon_db`

The examples cover CRUD operations, advanced queries, aggregation pipelines, collection joins, indexing, text search, schema validation, and transactions.

## Technologies Used

- MongoDB
- Python
- PyMongo
- MongoDB Query Language
- MongoDB Aggregation Framework

## MongoDB Concepts Demonstrated

### 1. CRUD Operations

Demonstrates:

- `insert_one()`
- `find()`
- `find_one()`
- `update_one()`
- `delete_one()`

File:

`crud_operations.py`

### 2. Advanced Queries

Demonstrates MongoDB query operators:

- `$gt`
- `$lt`
- `$gte`
- `$in`
- `$and`
- `$or`
- `$exists`
- Sorting
- Projection

File:

`advanced_queries.py`

### 3. Aggregation Pipeline

Demonstrates:

- `$match`
- `$group`
- `$sum`
- `$avg`
- `$sort`

File:

`aggregation_pipeline.py`

### 4. Collection Joins

Demonstrates:

- `$lookup`
- `$unwind`
- `$project`

The examples join orders with customers and products.

File:

`lookup_operations.py`

### 5. Indexing

Demonstrates:

- Unique indexes
- Single-field indexes
- Compound indexes
- `list_indexes()`
- `explain()`
- Query execution plans

File:

`indexing.py`

### 6. Text Search

Demonstrates:

- Text indexes
- `$text`
- `$search`
- Text relevance scores

File:

`text_search.py`

### 7. Schema Validation

Demonstrates:

- `$jsonSchema`
- Required fields
- BSON data types
- Value constraints
- Validation levels
- Validation actions

File:

`schema_validation.py`

### 8. Transactions

Demonstrates:

- MongoDB sessions
- Multi-operation transactions
- Commit
- Automatic rollback on failure

File:

`transactions.py`

## Project Structure

```text
MongoDBHackathon/
│
├── connection.py
├── sample_data.py
├── crud_operations.py
├── advanced_queries.py
├── aggregation_pipeline.py
├── lookup_operations.py
├── indexing.py
├── text_search.py
├── schema_validation.py
├── transactions.py
├── requirements.txt
├── README.md
└── .gitignore
