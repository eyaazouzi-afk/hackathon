from chonkie import TokenChunker
import products_database  

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