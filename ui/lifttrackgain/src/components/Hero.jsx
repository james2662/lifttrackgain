import React from "react";
import Typed from 'react-typed';

const Hero = () => {
    return (
        <div className="text-white">
            <div className="max-w-[800px] mt-[-96px] w-full h-screen mx-auto text-center flex flex-col justify-center border-grey-600">
                <p className="text-[#00df9a] font-bold p-2">GAINS WITH LIFTING AND TRACKING PROGRESS</p>
                <h1 className="md:text-7xl sm:text-6xl text-4xl font-bold md:py-6">Train with purpose</h1>
                <div className="flex justify-center items-center ">
                    <p className="md:text-4xl sm:text-2xl text-xl font-bold">Simple, intutive tracking for</p>
                    <Typed 
                        className="md:text-4xl sm:text-2xl text-xl font-bold pl-2 text-[#00df9a]" 
                        strings={["Power lifters", "Body Builders", "Power Builders", "Anyone"]} 
                        typeSpeed={120} 
                        backSpeed={140} 
                        loop
                    />
                </div>
            </div>
        </div>
    )
}

export default Hero