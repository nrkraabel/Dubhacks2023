/**
=========================================================
* Material Kit 2 React - v2.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-kit-react
* Copyright 2023 Creative Tim (https://www.creative-tim.com)

Coded by www.creative-tim.com

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/
// react-router components
import { Routes, Route, Navigate, useLocation } from "react-router-dom";

// @mui material components
import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

// Material Kit 2 React themes
import theme from "assets/theme";
import Home from "layouts/pages/home";
import FindForm from "layouts/pages/find-form";
import UploadForm from "layouts/pages/upload-form";
import Author from "layouts/pages/author";
import AboutUs from "layouts/pages/about-us";

export default function App() {


  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Routes>
        <Route path="/" element={<AboutUs />} />
        <Route path="/find-form" element={<FindForm />} />
        <Route path="/upload-form" element={<UploadForm />} />
        <Route path="/upload" element={<Home />} />
        <Route path="/author" element={<Author />} />
        {/* <Route path="/about-us" element={<Home/>} /> */}
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </ThemeProvider>
  );
}
