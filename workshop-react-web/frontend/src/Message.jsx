
import React, { useState } from 'react';
import "./messageCss.css"
import { createRoutesFromChildren } from 'react-router-dom';

export function Message() {


  const [inputText, setInput_text] = useState("");
  const [simplyText, setsimply_text] = useState('');

  const simpleText = async () => {
    console.log("testtss")
    const simplyText = inputText.split('');
    console.log("Got :" + inputText);
    let res = await fetch(`http://localhost:8000/api/v1/tasks?text=${inputText}`).then((response) => response.json());
    //res = res.reverse().join('');
    console.log(res);
    // setsimply_text = res;
    // document.getElementById('simple').value = simplyText;
    setsimply_text(res);
  };

  // useEffect(() => {
  //   document.title = 'kallikro';
  // }, []);


  return (
    
    <div className='containerMessage'>
      <img src={'/icon.ico'} alt="icon"></img>
      <br />
      <div style={{width:'630px',height:'4px',backgroundColor:'red',position:'absolute', top:'89px', right:'0px' }}></div>
      <div style={{width:'650px',height:'4px',backgroundColor:'red',position:'absolute', top:'63px', right:'780px' }}></div>
      <textarea
      dir='rtl'
      type="text"
      placeholder='הזן טקסט כאן:'
      id="inputText"
      style={{padding: '10px',position:'absolute',top:'180px',right:'260px',width:'450px',height:'350px',borderRadius:'40px',fontSize:'20x',outlineColor:'lightgray'}}
      onChange={(e) => setInput_text(e.target.value)}
      />
      <button style={{borderColor:'#5757ff',color:'#5757ff',borderRadius:'50px',background:'white',width:'200px',height:'50px',position:'absolute',top:'560px',right:'630px'}} onClick={simpleText}> לחץ כאן כדי לפשט </button>
      <label style={{}} htmlFor=""> </label>
      <textarea
        dir='rtl'
        type="text"
        placeholder='המתן...'
        id="inputText"
        style={{padding:'10px',position:'absolute',top:'180px',left:'200px',width:'450px',height:'350px',borderRadius:'40px',fontSize:'20px',outlineColor:'lightgray'}}
        readOnly
        value={simplyText}
      />

    </div>

  );
}

