const fetchBtn = document.getElementById("fetchBtn");
const statusBox = document.getElementById("statusBox");

fetchBtn.addEventListener("click", () => {
  const city = document.getElementById("city").value;

  statusBox.className = "status";
  statusBox.classList.remove("hidden");
  statusBox.innerText = "Fetching events...";

  fetch(`/fetch-events?city=${city}`)
    .then(res => res.json())
    .then(data => {
      if (data.status === "success") {
        statusBox.classList.add("success");
        statusBox.innerText =
          `✅ ${data.events_processed} events fetched for ${data.city}`;
      } else {
        statusBox.classList.add("error");
        statusBox.innerText = `❌ ${data.message}`;
      }
    })
    .catch(() => {
      statusBox.classList.add("error");
      statusBox.innerText = "❌ Backend error occurred";
    });
});
