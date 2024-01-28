
  /*
  function positionButton(rect) {
    const selectBtn = window.body.createElement('button');
    selectBtn.style.display = 'block';
    selectBtn.style.visibility = 'hidden';
    selectBtn.innerText = "לחץ כאן כדי לפשט."
    selectBtn.style.zIndex = 999;
    selectBtn.style.left = rect.left + window.pageXOffset + 'px';
    selectBtn.style.top = rect.bottom + window.pageYOffset + 'px';
     
    const selectedButton = document.getElementById('selectedButton');
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollLeft = window.pageXOffset || document.documentElement.scrollLeft;
    const buttonLeft = rect.left + scrollLeft;
    const buttonTop = rect.bottom + scrollTop;
  
    selectedButton.style.zIndex = 999;
    selectedButton.style.left = buttonLeft + 'px';
    selectedButton.style.top = buttonTop + 'px';
    
  }*/
  
  document.addEventListener('DOMContentLoaded', function () {

  });


  
  window.addEventListener('contextmenu', function(event) {
    // Prevent the default right-click behavior
    //event.preventDefault();
console.log("contextmenu event triggered, 'boutta send to localhost and that")
    const simpleText = async () => {
      let res = await fetch(`http://localhost:8000/api/v1/tasks?text=${selectedText}` ).then((response) => response.json());
      //res = res.reverse().join('');
      console.log(res);
      document.getElementById('simple').value = res;
      setsimply_text(res);

    }
    console.log('Right-click event occurred');
  });

  document.addEventListener('mouseup', async function (event) {
    const selectedText =  window.getSelection().toString().trim();
    console.log("selected now: " + selectedText)
    if (selectedText.length > 0) {
      const range = window.getSelection().getRangeAt(0);
      const rect = range.getBoundingClientRect();
      
      //positionButton(rect);
      //console.log(selectedText)
      const simpleText = async () => {
        //window.alert("...")
        let res = await fetch(`http://localhost:8000/api/v1/tasks?text=${selectedText}`).then((response) => response.json());
        //res = res.reverse().join('');
        console.log("Response is: "+res);
        //document.getElementById('simple').value = res;
        //setsimply_text(res);
        window.alert(res);
      }
      simpleText();
    

    } else {
      const selectedButton = document.getElementById('selectedButton');
      console.log("selected: " + selectedButton)
    }
    
    //const textarea = document.getElementById('text');
    //console.log("simplified: " + textarea.innerText)
  });
/*
  textarea.addEventListener('input', function(event) {
    const updatedText = event.target.value;
    console.log("updated: "+updatedText);
  });
  */
