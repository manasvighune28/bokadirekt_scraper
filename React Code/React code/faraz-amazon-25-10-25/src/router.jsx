
  import { BrowserRouter, Routes, Route } from "react-router-dom";
  import Login_now from "./pages/Login_now";
import Signup_email from "./pages/Signup_email";
import Products_listing from "./pages/Products_listing";
import Product_detail from "./pages/Product_detail";
import Add_to_cart from "./pages/Add_to_cart";
import Product_category_filter from "./pages/Product_category_filter";
import Checkout_page from "./pages/Checkout_page";
import Payment_page from "./pages/Payment_page";
import Login_phone from "./pages/Login_phone";
  
  export default function AppRouter() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/login-now" element={<Login_now />} />
        <Route path="/signup-email" element={<Signup_email />} />
        <Route path="/products-listing" element={<Products_listing />} />
        <Route path="/product-detail" element={<Product_detail />} />
        <Route path="/add-to-cart" element={<Add_to_cart />} />
        <Route path="/product-category-filter" element={<Product_category_filter />} />
        <Route path="/checkout-page" element={<Checkout_page />} />
        <Route path="/payment-page" element={<Payment_page />} />
        <Route path="/login-phone" element={<Login_phone />} />
        </Routes>
      </BrowserRouter>
    );
  }
  