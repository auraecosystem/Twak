const API = "http://localhost:8000";

async function createWallet() {
  const res = await fetch(API + "/wallet/create", {
    method: "POST"
  });

  document.getElementById("out").textContent =
    JSON.stringify(await res.json(), null, 2);
}

async function checkBalance() {
  const addr = document.getElementById("addr").value;

  const res = await fetch(API + "/wallet/balance/" + addr);

  document.getElementById("out").textContent =
    JSON.stringify(await res.json(), null, 2);
}
