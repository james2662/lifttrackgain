import React, {useState} from "react";
import {AiOutlineClose, AiOutlineMenu} from 'react-icons/ai'
import { Link, NavLink } from "react-router-dom";

const MNavBar = () => {
    const [nav, setNav] = useState(true)

    const handleNav = () => {
        setNav(!nav)
    }
    return (
        <div className="flex fustify-between items-center h-24 max-w-[1240px] mx-auto px-4 text-white">
            <h1 className="w-full text-3xl font-bold text-[#00df98ee]">LiftTrackGain.</h1>
            <ul className="hidden md:flex">
                <li className="p-4"><Link to="/">Home</Link></li>
                <li className="p-4"><Link to="about">About</Link></li>
                <li className="p-4"><Link to="signup">Signup</Link></li>
                <li className="p-4">Content</li>
            </ul>
            <div onClick={handleNav} className="block md:hidden">
                {!nav ? <AiOutlineClose size={20} /> : <AiOutlineMenu size={20}/>}
                
            </div>
            <div className={!nav ? "fixed left-0 top-0 w-[60%] h-full border-r border-r-gray-900 bg-[#000300] ease-in-out duration-500 md:left-[-100%]" : "fixed left-[-100%]"}>
                <h1 className="w-full text-3xl font-bold text-[#00df98ee] m-4">LiftTrackGain.</h1>
                <ul className="p-4 uppercase">
                    <li className="p-4 border-b border-grey-600"><Link to="/">Home</Link></li>
                    <li className="p-4 border-b border-grey-600"><Link to="about">About</Link></li>
                    <li className="p-4 border-b border-grey-600"><Link to="signup">Signup</Link></li>
                    <li className="p-4 ">Content</li>
                </ul>
            </div>
        </div>
    )
}

export default MNavBar
// 00df9a