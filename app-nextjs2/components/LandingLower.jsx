import Image from 'next/image'
import React, {useState} from 'react'
import burnerImg from '../public/assets/contact.jpg'
import Link from 'next/link'
import {AiOutlineClose, AiOutlineMenu, AiOutlineMail} from 'react-icons/ai'
import {FaGithub, FaLinkedinIn} from 'react-icons/fa'
import {BsFillPersonLinesFill} from 'react-icons/bs'
import LandingItem from './LandingItem'


const LandingLower = () => {
    return (
        <div id='LandingLower' className='w-full h-screen'> {/* parent container for projects */}
            <div className='max-w-[1240px] pt-32 mx-auto px-2'>
                <p className='text-xl tracking-widest uppercase text-[#5651e5]'>Options</p>
                <div className='grid sm:grid-cols-2 lg:grid-cols-3 gap-8'>
                    <LandingItem title='About' backgroundImg={burnerImg} projectUrl='/' tech='test' />
                    <LandingItem title='Search' backgroundImg={burnerImg} projectUrl='/searchForm' tech='test' />
                    <LandingItem title='Share' backgroundImg={burnerImg} projectUrl='/shareForm' tech='test' />
                </div>
            </div>
        </div>
    );
};

export default LandingLower;