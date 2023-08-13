import React from 'react'

export const Signup = () => {
  return (
    <div className='w-full py-16 text-white px-4'>
        <div className='max-w-[1240px mx-auto'>
            <h1 className='ltg-h1-green py-3'>Signup</h1>
            <div className='flex flex-row sm:flex-col md:text-right text-bottom w-full grid sm:grid-cols-1 md:grid md:grid-cols-3'>
                <lable className="font-bold col-span-1 pr-4">Email Address</lable>
                <input className='ltg-input-email col-span-2' type='email' placeholder='Enter Email' />
                
                <lable className="font-bold col-span-1 pr-4">Password</lable>
                <input className='ltg-input-std col-span-2' type='password' placeholder='Enter Password' />

                <lable className="font-bold col-span-1 pr-4">Confirm Password</lable>
                <input className='ltg-input-std col-span-2' type='password' placeholder='Re-enter Password' />

                <lable className="font-bold col-span-1 pr-4">First Name</lable>
                <input className='ltg-input-std col-span-2' type='text' placeholder='First Name' />
                
                <lable className="font-bold col-span-1 pr-4">Last Name</lable>
                <input className='ltg-input-std col-span-2' type='text' placeholder='Last Name/Surname' />
                
                
                <lable className="font-bold col-span-1 pr-4">Street Address</lable>
                <input className='ltg-input-std col-span-2' type='text' placeholder='Streeet Address' />

                <lable className="font-bold col-span-1 pr-4">City</lable>
                <input className='ltg-input-std col-span-2' type='text' placeholder='City' />

                <lable className="font-bold col-span-1 pr-4">State/Province</lable>
                <input className='ltg-input-std col-span-2' type='text' placeholder='State/Province' />
                
                <lable className="font-bold col-span-1 pr-4">Zip Code</lable>
                <input className='ltg-input-std col-span-2' type='text' placeholder='Zip Code' />
            </div>
            <button className='ltg-button-green'>Signup</button>
        </div>
    </div>
  )
}
