import React from 'react'
import { useState } from 'react'
import MNavBar from './components/MNavBar'
import Hero from './components/Hero'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <MNavBar />
      <Hero />
    </div>
  )
}

export default App
