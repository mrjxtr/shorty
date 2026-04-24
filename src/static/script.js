
const base_url = "http://127.0.0.1:8000" // just for practice
const api_url = `${base_url}/api/v1`




// Defining a function
function shortenURL() {
    // Defiing var
    const url = document.getElementById("url-input").value;
    const input = document.getElementById("url-input");
    const error = document.getElementById("empty-error");

    // check if empty
    if (!url) {
        input.classList.add("error");
        error.style.display = "block"
        return;
    }

     // hide error if previously shown
    input.classList.remove("error");
    error.style.display = "none";
    
    // Defining a fetch
    fetch(api_url + "/shorten",  // send reqiest to this URL
        {
            method: "POST",  // what method
            headers: { "Content-Type": "application/json" },  // specify type of body -> JSON
            body: JSON.stringify({ long_url: url })  // convert to str
        }
    )  // pass down value

    // .then() -> run when previous step succeeds
    .then(response => response.json()) // read body -> convert to JS obj -> pass to next .then()

    .then(data => {
        const result = document.getElementById("result"); // get div
        const short_code_header = document.getElementById("short-url-header");
        const copy_btn = document.getElementById("copy-btn");

        copy_btn.style.display = "block"
        short_code_header.style.display = "block"
        result.style.display = "block";  // show div when code is available
        result.innerText = `${base_url}/${data.short_code}`;  // put code inside div
    })

     // .catch() -> error exception
    .catch(error => console.error(error))
}

function copyURL() {
    const result = document.getElementById("result").innerText;
    navigator.clipboard.writeText(result)

}