function askAI() {
    let input = document.getElementById("input").value;

    if (input === "") {
        alert("Please type something!");
        return;
    }

    fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: input })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("response").innerText = data.reply;
    })
    .catch(error => {
        document.getElementById("response").innerText = "Error: " + error;
    });
}