# <p align="center">Recommender System</p>
<p align="center"> 
<a href="https://www.linkedin.com/in/roy-ashish">
<img alt="linkedin" src="https://img.shields.io/badge/-Ashish Roy-blue?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/roy-ashish"></a>
<img src="https://img.shields.io/badge/Version-1.0.0-blue" />
<img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />
<img src="https://img.shields.io/badge/Python-100%25-yellow?style=flat&logo=python&logoColor=yellow" />
</p>

## Motivation

To learn about statistical concepts for recommending top products for a customer based on purchase trends of all customers.

## Goal

To recommend top 10 products by using 3 data points i.e customer_id, item_id and purchased.

Uses cosine_similarity and csr_matrix to find the similarity between customer's behavior and recommend the next relevent product that other customers have also purchased. The script can be used to recommend together bought items based on the customer's purchase in real-time. 

Additional accomoditions can be made based on different use cases.

## Packages Used

```python
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
```

## How to Use

Can work with any data set where we have purchased history of customers with the respective product or item IDs.
Simply clone and run .py file with appropriate column names.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
