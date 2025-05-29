import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [data, setData] = useState("Click below to generate a story")

const handleOnClick = () => {fetch("http://localhost:5000/api/request")
  .then(res => res.json())
  .then(data => setData(data.output));
};


  return (
  

    <>
      <div >
        <input if="file" type="file"/>
        <button className='submit'>Upload</button>
        
      </div>
      <h1 className="text-3xl font-bold underline">{data}</h1>
      <div className="card">
        <button onClick={handleOnClick}>
          New Story
        </button>
       
      </div>
    
    </>
  )
}

export default App
