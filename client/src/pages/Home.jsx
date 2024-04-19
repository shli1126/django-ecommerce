import { useState, useEffect } from "react";
import axios from "axios";
import ItemCard from "../components/ItemCard";

const Home = () => {
  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const getAllItemsUrl = "http://127.0.0.1:8000/items/";
    const fetchData = async () => {
      try {
        const response = await axios.get(getAllItemsUrl);
        console.log(response.data.items);
        setData(response.data.items);
        setIsLoading(false);
      } catch (error) {
        setError(error);
        setIsLoading(false);
      }
    };
    fetchData();
  }, []);

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div>
      <h1>List All Items</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>
            <ItemCard id={item.id} title={item.title} price={item.price} />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
