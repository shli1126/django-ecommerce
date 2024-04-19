import { FaUserCircle, FaShoppingCart } from "react-icons/fa";
import { BsSearch } from "react-icons/bs";

export default function Header() {
  return (
    <header className="fixed top-0 left-0 w-full z-50 bg-slate-200 shadow-md">
      <div className="flex justify-between items-center max-w-6xl mx-auto p-3">
        {/* Logo and Title */}
        <div className="flex items-center space-x-4">
          <h1 className="font-bold text-sm sm:text-xl">
            <span className="text-slate-500">eCommerce</span>
          </h1>
        </div>

        {/* Search Bar */}
        <div className="flex items-center border px-2 py-1 bg-white border-gray-300 rounded-full">
          <input
            type="text"
            placeholder="Search products..."
            className="outline-none text-sm px-2"
          />
          <BsSearch className="text-gray-500" />
        </div>

        {/* Navigation and Icons */}
        <div className="flex items-center space-x-6">
          <nav>
            <a
              href="#products"
              className="text-gray-600 hover:text-gray-800 text-sm sm:text-base"
            >
              Products
            </a>
            <a
              href="#about"
              className="ml-4 text-gray-600 hover:text-gray-800 text-sm sm:text-base"
            >
              About Us
            </a>
          </nav>
          <FaUserCircle className="text-xl text-gray-600 hover:text-gray-800 cursor-pointer" />
          <FaShoppingCart className="text-xl text-gray-600 hover:text-gray-800 cursor-pointer" />
        </div>
      </div>
    </header>
  );
}
