import { useState, useEffect } from 'react' // Cleaned up imports
import './App.css'

function App() {
  // 1. FIXED: Changed let products to React State
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/products')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setProducts(data); 
      })
      .catch((err) => {
        alert(err.message);
      });
  }, []);

  return (
    <div>
      <section id="center">
        <div className="hero">
          <span>Welcome to my first react page</span>
          <h2>Products</h2>
          <ul>
            {products.map((product) => (
              <li key={product.id}>{product.name}, Quantity: {product.quantity}, Final Price: Quantity: {product.quantity * product.price}</li>
            ))}
          </ul>
        </div>
      </section>
    </div>
  )
}

export default App
