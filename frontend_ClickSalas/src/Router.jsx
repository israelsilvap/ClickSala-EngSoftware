import { Routes, Route } from "react-router-dom";

import { Home } from "./pages/Home";
import { About } from "./pages/About";
import { BdPage } from "./pages/Bdpage";
import { Campus } from "./pages/Campus";
import { Index } from "./pages/Index";

export function Router() {
  return (
    <Routes>
      <Route path="/index" element={<Index />} />
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/bdpage" element={<BdPage />} />
      <Route path="/campus" element={<Campus />} />
    </Routes>
  );
}
