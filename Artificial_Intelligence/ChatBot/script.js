const chatbox = document.getElementById("chatbox");
const input = document.getElementById("input");
const send = document.getElementById("send");
const chatToggle = document.getElementById("chat-toggle");
const chatWidget = document.getElementById("chat-widget");
const closeBtn = document.getElementById("close-btn");
const preChatInfo = document.getElementById("pre-chat-info");

// Hide the toggle button initially
chatToggle.style.display = "none";

// Show it after pre-info animation
setTimeout(() => {
  chatToggle.style.display = "block";
}, 6000); // after animations complete

// On click, show chatbot and hide toggle + info
chatToggle.addEventListener("click", () => {
  chatWidget.style.display = "flex";
  chatToggle.style.display = "none";
  if (preChatInfo) preChatInfo.style.display = "none"; // hide pre-chat info
});


// Close chat
closeBtn.addEventListener("click", () => {
  chatWidget.style.display = "none";
  chatToggle.style.display = "flex";
  if (preChatInfo) preChatInfo.style.display = "block"; // show it again
});

// Add message to chatbox
function addMessage(message, sender) {
  const div = document.createElement("div");
  div.classList.add("message", sender);
  div.innerText = message;
  chatbox.appendChild(div);
  chatbox.scrollTop = chatbox.scrollHeight;
}

// Show welcome message
window.onload = () => {
  addMessage("🤖: Ready to chat? I'm your friendly bot here to make things easy!", "bot");
};

// Simulate bot reply
async function getBotReply(userMessage) {
  const response = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await response.json();
  return data.reply;
}

// Send button click
send.addEventListener("click", async () => {
  const userMsg = input.value.trim();
  if (userMsg === "") return;

  addMessage("🙍‍♀️: " + userMsg, "user");
  input.value = "";

  const botReply = await getBotReply(userMsg);
  addMessage("🤖: " + botReply, "bot");
});

// Enter key to send
input.addEventListener("keypress", (e) => {
  if (e.key === "Enter") send.click();
});
