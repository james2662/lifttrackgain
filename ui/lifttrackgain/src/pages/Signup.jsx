import React from 'react'

export const Signup = () => {
  return (
    // TODO:  NEed to split user/pass into seperate form, page 1 of flow.  
    // Makes formatting easier and appearance better
    <div className='w-full py-16 text-white px-4'>
        <div className='max-w-[1240px mx-auto'>
            <h1 className='ltg-h1-green py-3'>Signup</h1>
            <form>
              <div className='flex flex-row sm:flex-col md:text-right text-bottom w-full grid sm:grid-cols-1 md:grid md:grid-cols-3'>
                  <div className='p-2 w-full flex col-span-2'>
                    <lable className="font-bold col-span-1 pr-4" htmlFor="email" >Email Address</lable>
                    <input className='ltg-input-email col-span-2' type='email' id="email" name="email" placeholder='Enter Email' />
                  </div>
                  <div className='p-2 w-full flex col-span-2'>
                    <lable className="font-bold col-span-1 pr-4" htmlFor="secret_1">Password</lable>
                    <input className='ltg-input-std col-span-2 w-48' type='password' id="secret_1" name="secret_1" placeholder='Enter Password' />
                  </div>
                  <div className='p-2 w-full flex col-span-2'>
                    <lable className="font-bold col-span-1 pr-4" htmlFor="secret_2">Confirm Password</lable>
                    <input className='ltg-input-std col-span-2' type='password' name="secret_2" id="secret_2" placeholder='Re-enter Password' />
                  </div>  
                  <div className='p-2 w-full flex'>
                    <lable className="font-bold col-span-1 pr-4" htmlFor="first_name">First Name</lable>
                    <input className='ltg-input-std col-span-2' type='text' id="first_name" name="first_name" placeholder='First Name' />
                  </div>
                  <div className='p-2 w-full flex'>
                    <lable className="font-bold col-span-1 pr-4" htmlFor="last_name" >Last Name</lable>
                    <input className='ltg-input-std col-span-2' type='text' id="last_name" name="last_name" placeholder='Last Name/Surname' />
                  </div>
                  <div className='p-2 w-full flex'>
                    <lable className="font-bold col-span-1 pr-4" htmlFor="str_address">Street Address</lable>
                    <input className='ltg-input-std col-span-2' type='text' id="str_address" name="str_address" placeholder='Streeet Address' />
                  </div>
                  <div className='p-2 w-full flex'>
                  <lable className="font-bold col-span-1 pr-4" htmlFor="city">City</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="city" name="city" placeholder='City' />
                  </div>
                  <div className='p-2 w-full flex'>
                  <lable className="font-bold col-span-1 pr-4" htmlFor="state">State/Province</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="state" name="state" placeholder='State/Province' />
                  </div>
                  <div className='p-2 w-full flex'>
                  <lable className="font-bold col-span-1 pr-4" htmlFor="postal_code">Zip Code</lable>
                  <input className='ltg-input-std col-span-2' type='text' id="postal_code" name="postal_code" placeholder='Zip Code' />
                  </div>
              </div>
              <button className='ltg-button-green'>Signup</button>
            </form>
        </div>
    </div>
  )
}
