import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const ItemPage = () => {

  const { id } = useParams(); 
  const [item, setItem] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchItem = async () => {
      setIsLoading(true);
      try {
        const response = await axios.get(`http://127.0.0.1:8000/item/${id}/`);
        setItem(response.data); 
        setIsLoading(false);
      } catch (err) {
        setError(err.message);
        setIsLoading(false);
      }
    };

    if (id) {
      fetchItem();
    }
  }, [id]); 

  if (isLoading) return (<div>Loading...</div>);
  if (error) return (<div>Error: {error}</div>);
  if (!item) return (<div>No item found</div>);


  return (
    <div className="bg-white">
      <div className="pt-6">
        {/* Product info */}
        <div className="mx-auto max-w-2xl px-4 pb-16 pt-10 sm:px-6 lg:grid lg:max-w-7xl lg:grid-cols-3 lg:grid-rows-[auto,auto,1fr] lg:gap-x-8 lg:px-8 lg:pb-24 lg:pt-16">
          <div className="lg:col-span-2 lg:border-r lg:border-gray-200 lg:pr-8">
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
              {item.name}
            </h1>
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
              {item.discount}
            </h1>
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
              {item.stock}
            </h1>
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
              {item.retailer}
            </h1>
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
              {item.category}
            </h1>
            <h1 className="text-2xl font-bold tracking-tight text-gray-900 sm:text-3xl">
              {item.return_policy}
            </h1>
          </div>

          {/* Options */}
          <div className="mt-4 lg:row-span-3 lg:mt-0">
            <h2 className="sr-only">Product information</h2>
            <p className="text-3xl tracking-tight text-gray-900">
              {item.price}
            </p>
            <form className="mt-10">
              <button
                type="submit"
                className="mt-10 flex w-full items-center justify-center rounded-md border border-transparent bg-indigo-600 px-8 py-3 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
              >
                Add to bag
              </button>
            </form>
          </div>

          <div className="py-10 lg:col-span-2 lg:col-start-1 lg:border-r lg:border-gray-200 lg:pb-16 lg:pr-8 lg:pt-6">
            {/* Description and details */}
            <div>
              <h3 className="sr-only">Description</h3>

              <div className="space-y-6">
                <p className="text-base text-gray-900">
                  This is the default description
                </p>
              </div>
            </div>

            <div className="mt-10">
              <h2 className="text-sm font-medium text-gray-900">Details</h2>

              <div className="mt-4 space-y-6">
                <p className="text-sm text-gray-600">
                  This is the default detail
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ItemPage;
