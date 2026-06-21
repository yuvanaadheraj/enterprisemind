import { useState } from "react";
import { Send, Brain } from "lucide-react";
import API from "../services/api";

function ChatPage() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    try {
      setLoading(true);

      const response = await API.post("/chat", {
        question,
      });

      setAnswer(response.data.answer);
    } catch (error) {
      console.log(error);
      alert("Error contacting backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">

      <div className="bg-slate-900 text-white p-5 shadow">
        <div className="max-w-6xl mx-auto flex items-center gap-3">
          <Brain size={32} />
          <h1 className="text-3xl font-bold">
            EnterpriseMind
          </h1>
        </div>
      </div>

      <div className="max-w-5xl mx-auto p-8">

        <div className="bg-white rounded-2xl shadow p-6">

          <h2 className="text-2xl font-semibold mb-4">
            Ask EnterpriseMind
          </h2>

          <textarea
            rows="5"
            className="w-full border rounded-xl p-4"
            placeholder="Ask a question..."
            value={question}
            onChange={(e) =>
              setQuestion(e.target.value)
            }
          />

          <button
            onClick={askQuestion}
            className="mt-4 bg-slate-900 text-white px-6 py-3 rounded-xl flex items-center gap-2"
          >
            <Send size={18} />
            Ask
          </button>

        </div>

        <div className="mt-8 bg-white rounded-2xl shadow p-6">

          <h2 className="text-2xl font-semibold mb-4">
            Response
          </h2>

          {loading ? (
            <p>Thinking...</p>
          ) : (
            <pre className="whitespace-pre-wrap">
              {answer}
            </pre>
          )}

        </div>

      </div>
    </div>
  );
}

export default ChatPage;