function mathildeClicked(){
    // document.body.style.backgroundColor = "pink"

    const color1 = "pink"
    const color2 = "yellow"

    //const colors = ["red", "green", "blue", "yelloe", "orange", "pink"]
    
    const image = document.getElementsByClassName ("my-img")[0]

    //if (document.body.style.backgroundColor == color1){
        //document.body.style.backgroundColor = color2;
    //} else {
        //document.body.style.backgroundColor = color1;
    //}

     if (image.style.display ==="none"){
         image.style.display = "block"; // Make it visible again
    } else {
        image.style.display = "none"; // Hide it
    }


 
}