let transcript = "";

async function transcribe() {
  const file = document.getElementById("audio").files[0];
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch("http://localhost:8000/transcribe", {
    method: "POST",
    body: formData,
  });

  const data = await res.json();
  transcript = data.transcript;
  document.getElementById("transcript").innerText = transcript;
}

async function summarize() {
  const formData = new FormData();
  formData.append("text", transcript);

  const res = await fetch("http://localhost:8000/summarize", {
    method: "POST",
    body: formData,
  });

  const data = await res.json();
  document.getElementById("summary").innerText = data.summary;
}
