// VerificationPage.jsx
import { useEffect, useState } from "react";

export default function VerificationPage() {
  const [status, setStatus] = useState("Verifying...");
  
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const token = params.get("token");
    
    if (!token) {
      setStatus("No token provided.");
      return;
    }

    fetch("http://localhost:5555/users/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token }),
    })
    .then(res => res.json())
    .then(data => {
      if (data.message) setStatus(data.message);
      else if (data.error) setStatus(data.error);
    })
    .catch(() => setStatus("An error occurred."));
  }, []);

  return <div>{status}</div>;
}
