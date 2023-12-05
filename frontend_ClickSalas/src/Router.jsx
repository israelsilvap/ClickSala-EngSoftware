import { Routes, Route } from "react-router-dom";

import { Home } from "./pages/Home";
import { About } from "./pages/About";
import { BdPage } from "./pages/Bdpage";
import { Campus } from "./pages/Campus";

export function Router() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/bdpage" element={<BdPage />} />
      <Route path="/campus" element={<Campus />} />
    </Routes>
  );
}
