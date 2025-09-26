async function pickFileAndUpload() {
    console.log("start");
    try{
        const dirHandle = await window.showDirectoryPicker();
        const formData = new FormData();

        for await (const[name, handle] of dirHandle.entries()) {
            if(handle.kind === "file"){
                const file = await handle.getFile();
                formData.append("files", file, file.name)
            }
        }

        const response = await fetch('http://localhost:5000/cryp',
            {method: 'POST',
            body: formData}
        );

        console.log(response);

    } catch(err) {
        console.error(err)
        alert("Error: " + err.message)
    }
}

document.getElementById('sendButton').addEventListener('click', pickFileAndUpload);