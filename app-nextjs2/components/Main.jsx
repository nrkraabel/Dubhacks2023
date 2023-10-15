import Image from 'next/image'
import React, { useState, useEffect } from "react";
import Link from 'next/link'
import { AiOutlineMail} from 'react-icons/ai'
import {FaGithub, FaLinkedinIn} from 'react-icons/fa'
import {BsFillPersonLinesFill} from 'react-icons/bs'
import {HiOutlineChevronDoubleDown} from 'react-icons/hi'
import {useRouter} from 'next/router'


const Main = () => {

    const router = useRouter()
    const onMain = (router.asPath === '/#LandingLower')

    const [data, setdata] = useState({
        name: "",
        age: 0,
        date: "",
        programming: "",
      });
  
      // Using useEffect for single rendering
      useEffect(() => {
          // Using fetch to fetch the api from 
          // flask server it will be redirected to proxy
          fetch("http://127.0.0.1:5000/data").then((res) =>
              res.json().then((data) => {
                  // Setting a data from api
                  console.log(data)
                  setdata({
                      name: data.Name,
                      age: data.Age,
                      date: data.Date,
                      programming: data.programming,
                  });
              })
          );
      }, []);

    return (
        <div id='home' className='w-full h-screen text-center'>
            <div className='max-w-[1240px] pt-32 m-auto px-2 w-full h-full flex flex-col justify-between'>
                <div className='max-w-[1240px] w-full h-full mx-auto p-2 flex justify-center items-center'>
                    <div>
                        <h1 className='py-4 text-gray-700'>CSW</h1>
                        <h2>React and flask</h2>
                        {/* Calling a data from setdata for showing */}
                        <p>{data.name}</p>
                        <p>{data.age}</p>
                        <p>{data.date}</p>
                        <p>{data.programming}</p>
                    </div>
                </div>
                <div className='flex justify-center py-12'>
                    <Link href='/#LandingLower'>
                        <HiOutlineChevronDoubleDown className='text-[#5651e5]' size={30} /> {/* using size property of react icons */}
                    </Link>
                </div>
            </div>
        </div>   
    );
};

export default Main;