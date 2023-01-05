import React, { useState, useEffect } from 'react'
import Form from './Pages/Form';
import Navbar from './components/Navbar';

function App() {
  //all the value from form is sent to below data
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data);
      }
    )
  }, [])
  return (
    <div>
      <Navbar />
      <Form />
      {/* used this just to see the connection, not needed */}
      {/* {(typeof data.members === 'undefined') ? (
        <p></p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )} */}

    </div>
  )

}

export default App

