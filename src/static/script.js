
const base_url = "http://127.0.0.1:8000"



// Defining a function
function shortenURL() {
    // Defiing var
    const url = document.getElementById("url-input").value;

    // Defining a fetch
    fetch(base_url + "/shorten",  // send reqiest to this URL
        {
            method: "POST",  // what method
            headers: { "Content-Type": "application/json" },  // specify type of body -> JSON
            body: JSON.stringify({ long_url: url })  // convert to str
        }
    )  // pass down value

    // .then() -> run when previous step succeeds
    // .catch() -> error exception
    .then(response => response.json()) // read body -> convert to JS obj -> pass to next .then()
    .then(data => {
        const result = document.getElementById("result"); // get div
        const short_code_header = document.getElementById("short-url-header");
        
        short_code_header.style.display = "block"
        result.style.display = "block";  // show div when code is available
        result.innerText = `${base_url}/${data.short_code}`;  // put code inside div
    }


    )
    .then(data => document.getElementById("result").innerText = data.short_code)  // pass down value
    .catch(error => console.error(error))
}

