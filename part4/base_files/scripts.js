/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

/*document.addEventListener('DOMContentLoaded', () => {
     DO SOMETHING 
  });*/

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const errorMessage = document.getElementById("error-message");

  loginForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    errorMessage.textContent = ""; // Clear previous errors

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
      const response = await fetch("http://127.0.0.1:5000/api/v1/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
      });

      if (!response.ok) {
        const errorData = await response.json();
        errorMessage.textContent = errorData.message || "Invalid credentials";
        return;
      }

      const data = await response.json();

      // ✅ Store the token in a cookie (valid for 7 days)
      document.cookie = `authToken=${data.token}; path=/; max-age=${7 * 24 * 60 * 60}; SameSite=Strict; Secure`;

      // Optional: store user info in localStorage
      localStorage.setItem("userEmail", data.user.email);

      // ✅ Redirect to main page
      window.location.href = "index.html";

    } catch (error) {
      console.error("Login error:", error);
      errorMessage.textContent = "Something went wrong. Please try again.";
    }
  });
});
