from qdrant_client import QdrantClient
import FasterTextEmb as f
from pathlib import Path  
from qdrant_client.models import PointStruct

#!!!!!!!!!!!!!!!!!!!!!!!the data to insert should contain "id" "vector" and finally the "infos or payload" !!!!!!!!!!!!!!!

#connect to qdrant ***************
client = QdrantClient(
    url="https://4797bc27-a78a-4d46-bb0d-9d87dc8ca35e.us-east4-0.gcp.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.gV1YzLbyVuElAfkgKVXRPkNLTZVUzADB_TPa7L29AgI"
)
#prepare product**************** (example of a product)
products = [
    {
        "id": 1,
        "text": "Red running shoes for men",
        "image": "images/shoes1.jpg",
        "price": 120,
        "category": "shoes"
    },
    {
        "id": 2,
        "text": "Wireless noise cancelling headphones",
        "image": "images/headphones.jpg",
        "price": 250,
        "category": "electronics"
    }
]











#insertion*******************
points=[]
for p in products:
    v=f.embed(p["text"]+" "+p["category"])

    v1 = v.squeeze(0).tolist()
    print(len(v1))
    

    points.append(
        PointStruct(
            id=p["id"],
            vector=v1,
            payload={
                "title": p["text"],
                "price": p["price"],
                "category": p["category"]
            }
        )
    )
client.upsert(
    collection_name="finmatch",
    points=points
)
count = client.count(collection_name="finmatch")
print(count)