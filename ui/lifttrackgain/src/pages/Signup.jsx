import React from 'react'

export const Signup = () => {
  return (
    <div className='w-full py-16 text-white px-4'>
        <div className='max-w-[1240px mx-auto'>
            <h1 className='ltg-h1-green py-3'>Signup</h1>
            <form>
              <div className='flex flex-row sm:flex-col md:text-right text-bottom w-full grid sm:grid-cols-1 md:grid md:grid-cols-3'>
                  <lable className="font-bold col-span-1 pr-4" htmlFor="email" >Email Address</lable>
                  <input className='ltg-input-email col-span-2' type='email' id="email" name="email" placeholder='Enter Email' />
                  
                  <lable className="font-bold col-span-1 pr-4" htmlFor="secret_1">Password</lable>
                  <input className='ltg-input-std col-span-2' type='password' id="secret_1" name="secret_1" placeholder='Enter Password' />

                  <lable className="font-bold col-span-1 pr-4" htmlFor="secret_2">Confirm Password</lable>
                  <input className='ltg-input-std col-span-2' type='password' name="secret_2" id="secret_2" placeholder='Re-enter Password' />

                  <lable className="font-bold col-span-1 pr-4" htmlFor="first_name">First Name</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="first_name" name="first_name" placeholder='First Name' />
                  
                  <lable className="font-bold col-span-1 pr-4" htmlFor="last_name" >Last Name</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="last_name" name="last_name" placeholder='Last Name/Surname' />
                  
                  <lable className="font-bold col-span-1 pr-4" htmlFor="str_address">Street Address</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="str_address" name="str_address" placeholder='Streeet Address' />

                  <lable className="font-bold col-span-1 pr-4" htmlFor="city">City</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="city" name="city" placeholder='City' />

                  <lable className="font-bold col-span-1 pr-4" htmlFor="state">State/Province</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="state" name="state" placeholder='State/Province' />
                  
                  <lable className="font-bold col-span-1 pr-4" htmlFor="postal_code">Zip Code</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="postal_code" name="postal_code" placeholder='Zip Code' />
              </div>
              <button className='ltg-button-green'>Signup</button>
            </form>
        </div>
    </div>
  )
}
