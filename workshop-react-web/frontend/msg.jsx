import React from 'react';
import { TextField, Grid, Button, Container } from '@mui/material';

const MyPage = () => {
  const [text1, setText1] = React.useState('');
  const [text2, setText2] = React.useState('');
  const [selectedButton, setSelectedButton] = React.useState('');

  const handleText1Change = (event) => {
    setText1(event.target.value);
  };

  const handleText2Change = (event) => {
    setText2(event.target.value);
  };

  const handleButtonClick = (button) => {
    setSelectedButton(button);
  };

  return (
    <Container>
      <h1>דף אינטרנט עם תיבות טקסט וכפתורים</h1>

      <Grid container spacing={2}>
        <Grid item xs={6}>
          <TextField
            label="תיבה טקסט 1"
            value={text1}
            onChange={handleText1Change}
            fullWidth
          />
        </Grid>
        <Grid item xs={6}>
          <TextField
            label="תיבה טקסט 2"
            value={text2}
            onChange={handleText2Change}
            fullWidth
          />
        </Grid>
      </Grid>

      <Button variant="contained" onClick={() => handleButtonClick('כפתור 1')}>
        כפתור 1
      </Button>
      <Button variant="contained" onClick={() => handleButtonClick('כפתור 2')}>
        כפתור 2
      </Button>
      <Button variant="contained" onClick={() => handleButtonClick('כפתור 3')}>
        כפתור 3
      </Button>

      {selectedButton && (
        <p>הכפתור שנבחר הוא: {selectedButton}</p>
      )}
    </Container>
  );
}

export default MyPage;
