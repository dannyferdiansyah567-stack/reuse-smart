const fotoInput = document.getElementById("foto");

const previewContainer =
    document.getElementById("previewContainer");

const previewImage =
    document.getElementById("previewImage");

const fileName =
    document.getElementById("fileName");

const removeImage =
    document.getElementById("removeImage");


fotoInput.addEventListener("change", function () {

    const file = this.files[0];

    if (!file) {
        return;
    }

    fileName.textContent = file.name;

    const reader = new FileReader();

    reader.onload = function (event) {

        previewImage.src =
            event.target.result;

        previewContainer.style.display =
            "flex";
    };

    reader.readAsDataURL(file);

});


removeImage.addEventListener("click", function () {

    fotoInput.value = "";

    previewImage.src = "";

    previewContainer.style.display =
        "none";

});