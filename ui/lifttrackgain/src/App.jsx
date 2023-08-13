import React from 'react'
import { useState } from 'react'
import './App.css'
import MNavBar from './components/MNavBar'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <MNavBar />
    </div>
  )
}

export default App
