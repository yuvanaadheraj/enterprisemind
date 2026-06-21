import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from "react-router-dom";

import ChatPage from "./pages/ChatPage";
import UploadPage from "./pages/UploadPage";

function App() {

  return (

    <BrowserRouter>

      <nav
        style={{
          padding: "20px",
          background: "#eee"
        }}
      >

        <Link to="/">
          Chat
        </Link>

        {" | "}

        <Link to="/upload">
          Upload
        </Link>

      </nav>

      <Routes>

        <Route
          path="/"
          element={<ChatPage />}
        />

        <Route
          path="/upload"
          element={<UploadPage />}
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App;