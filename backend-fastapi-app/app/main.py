
from fastapi import FastAPI
from models.products import Products
from fastapi.middleware.cors import CORSMiddleware

# 2. Initialize the app
app = FastAPI()

# 3. Define allowed origins (your React frontend URL)
origins = [
    "http://localhost:3000", # Vite/CRA default local port
    "http://localhost:5173", # Vite alternative port
]

# 4. ADD THE MIDDLEWARE HERE (Right after initialization)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)


@app.get("/greeting")
def read_root():
    return {"app": "family tree project"}

products = [Products(1, 'phone', 'android', 15000, 1),
            
            Products(2, 'tab', 'ois', 150000, 2),
            Products(3, 'laptop', 'ois', 150000, 1),
            Products(4, 'Game Device', 'android', 50000, 2),
            Products(5, 'tab', 'ois', 40000, 4)]

@app.get('/products')
def getAllProducts():
    return products
    