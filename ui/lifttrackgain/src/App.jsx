import React from 'react'
import { useState } from 'react'
import MNavBar from './components/MNavBar'
import Hero from './components/Hero'
import Analytics from './components/Analytics'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <MNavBar />
      <Hero />
      <Analytics />
    </div>
  )
}

export default App
