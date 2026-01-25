from chonkie import TokenChunker  

products_database = [
   {
       "id": 1,
       "name": "Dell XPS 15",
       "category": "laptop",
       "brand": "Dell",
       "price": 1299,
       "currency": "EUR",
       "stock": True,
       "description": "Laptop gaming professionnel Dell XPS 15. Processeur Intel Core i7-11800H 8 cœurs, 16GB RAM DDR4, carte graphique NVIDIA GeForce RTX 3050 4GB VRAM. Écran 15.6 pouces Full HD anti-reflet, SSD NVMe 512GB ultra-rapide. Clavier rétroéclairé, webcam HD, batterie 6 cellules longue durée. Idéal pour gaming, programmation, montage vidéo. Paiement en 3x sans frais disponible.",
       "specs": {
           "processor": "Intel i7-11800H",
           "ram": "16GB",
           "storage": "512GB SSD",
           "gpu": "RTX 3050",
           "screen": "15.6 inch Full HD"
       },
       "payment_options": ["1x", "3x", "6x", "12x"]
   }
]

def product_to_text(product):
    """Convertit un produit en texte simple pour tester le chunker."""
    
    text = f"{product['name']} - {product['brand']}\n"
    text += f"Prix: {product['price']} {product['currency']}\n"
    text += f"{product['description']}\n"
    text += f"Specs: {product['specs']}\n"
    text += f"Paiement: {product['payment_options']}"
    
    return text


def chunkie(text: str):
    chunker = TokenChunker(
        chunk_size=200,
        chunk_overlap=50
    )
    chunks = chunker.chunk(text)
    return [chunk.text for chunk in chunks]


def process_products(products_database):
    result = {}
    
    for product in products_database:
        product_text = product_to_text(product)
        chunks = chunkie(product_text)
        result[product['id']] = chunks
    
    return result

print(process_products(products_database))