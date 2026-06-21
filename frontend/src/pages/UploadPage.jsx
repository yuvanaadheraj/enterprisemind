import { useState } from "react";
import { Upload } from "lucide-react";
import API from "../services/api";

function UploadPage() {

  const [file, setFile] = useState(null);

  const uploadFile = async () => {

    if (!file) return;

    const formData = new FormData();

    formData.append(
      "file",
      file
    );

    try {

      const response =
        await API.post(
          "/upload",
          formData
        );

      alert(
        "Upload Successful!"
      );

      console.log(
        response.data
      );

    } catch (error) {

      console.log(error);

      alert(
        "Upload Failed"
      );
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">

      <div className="max-w-4xl mx-auto p-10">

        <div className="bg-white rounded-2xl shadow p-8">

          <h1 className="text-3xl font-bold mb-6">
            Upload Document
          </h1>

          <input
            type="file"
            onChange={(e) =>
              setFile(
                e.target.files[0]
              )
            }
          />

          <br />
          <br />

          <button
            onClick={uploadFile}
            className="bg-slate-900 text-white px-6 py-3 rounded-xl flex items-center gap-2"
          >
            <Upload size={18} />
            Upload
          </button>

        </div>

      </div>
    </div>
  );
}

export default UploadPage;