import React from 'react'
import { useState } from 'react'
import { BrowserRouter, Routes, Route, Link, NavLink } from 'react-router-dom'
import MNavBar from './components/MNavBar'
import Hero from './components/Hero'
import Home from './pages/Home'
import About from './pages/About'
import { Signup } from './pages/Signup'

function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
    <header>
      <nav>
        <MNavBar />
      </nav>
    </header>
      <main>
        <Routes>
          <Route index element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="signup" element={<Signup />} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}

export default App
