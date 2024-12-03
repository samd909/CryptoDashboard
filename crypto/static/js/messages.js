document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
      const messageContainer = document.getElementById("message-container");
      if (messageContainer) {
        messageContainer.style.transition = "opacity 0.5s";
        messageContainer.style.opacity = "0";
        setTimeout(() => messageContainer.remove(), 500); // Remove after fading
      }
    }, 5000); // Disappear after 5 seconds
  });