import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Home from "./pages/Home"
import ItemPage from "./pages/ItemPage";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="item/:id" element={<ItemPage/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
