document.getElementById("upload-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("audio");
   const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  const audioPlayer = document.getElementById("audio-player");
  audioPlayer.src = URL.createObjectURL(file);
  audioPlayer.style.display = "block";
  
  const res = await fetch("http://localhost:8000/transcribe", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("transcript").value = data.transcript || "エラーが発生しました";
});

document.getElementById("summarize-btn").addEventListener("click", async () => {
  const text = document.getElementById("transcript").value;
  const formData = new FormData();
  formData.append("text", text);

  const res = await fetch("http://localhost:8000/summarize", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("summary").value = data.summary || "要約できませんでした";
});

document.getElementById("translate-btn").addEventListener("click", async () => {
  const text = document.getElementById("transcript").value;
  const formData = new FormData();
  formData.append("text", text);

  const res = await fetch("http://localhost:8000/translate", {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  document.getElementById("translate").value = data.summary || "翻訳できませんでした";
});
