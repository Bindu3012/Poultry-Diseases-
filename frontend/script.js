function previewImage() {
    const file = document.getElementById("imageInput").files[0];
    const preview = document.getElementById("preview");

    if (file) {
        preview.src = URL.createObjectURL(file);
        preview.style.display = "block";
    }
}
function predict() {
    const fileInput = document.getElementById("imageInput");
    const resultDiv = document.getElementById("result");

    if (fileInput.files.length === 0) {
        alert("Please upload an image");
        return;
    }

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    fetch("http://localhost:5000/predict", {
        method: "POST",
        body: formData
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        resultDiv.innerHTML =
            "Disease: " + data.disease + "<br>" +
           "Confidence: " + (data.confidence * 100).toFixed(2) + "%<br>"
            "Treatment: " + data.treatment;
    })
    .catch(function(error) {
        console.error("Error:", error);
        resultDiv.innerHTML = "Error connecting to server";
    });
}