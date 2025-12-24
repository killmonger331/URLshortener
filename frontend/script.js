// IMPORTANT:
// Set this to your Elastic Beanstalk backend base URL once deployed.
// Example: "https://my-urlshortener-env.us-west-2.elasticbeanstalk.com"
const BACKEND_BASE_URL = "https://api.richard-morales.com";

const form = document.getElementById("shorten-form");
const input = document.getElementById("url");
const statusEl = document.getElementById("status");
const output = document.getElementById("output");
const shortUrlEl = document.getElementById("short-url");
const copyBtn = document.getElementById("copy");
const errorEl = document.getElementById("error");

function setStatus(text) {
  statusEl.textContent = text;
}

function showError(msg) {
  errorEl.textContent = msg;
  errorEl.classList.remove("hidden");
}

function clearError() {
  errorEl.textContent = "";
  errorEl.classList.add("hidden");
}

function showOutput(shortUrl) {
  shortUrlEl.textContent = shortUrl;
  shortUrlEl.href = shortUrl;
  output.classList.remove("hidden");
}

function hideOutput() {
  output.classList.add("hidden");
  shortUrlEl.textContent = "";
  shortUrlEl.href = "#";
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  clearError();
  hideOutput();

  const longUrl = input.value.trim();
  if (!longUrl) return;

  try {
    setStatus("Shortening…");

    const res = await fetch(`${BACKEND_BASE_URL}/shorten`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: longUrl }),
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(text || `Request failed (${res.status})`);
    }

    const data = await res.json();
    showOutput(data.short_url);
    setStatus("Done");
  } catch (err) {
    setStatus("Error");
    showError(
      `Could not shorten URL. ${
        err && err.message ? err.message : "Unknown error"
      }`
    );
  }
});

copyBtn.addEventListener("click", async () => {
  const value = shortUrlEl.textContent;
  if (!value) return;
  try {
    await navigator.clipboard.writeText(value);
    setStatus("Copied!");
    setTimeout(() => setStatus("Done"), 900);
  } catch {
    setStatus("Copy failed");
  }
});
