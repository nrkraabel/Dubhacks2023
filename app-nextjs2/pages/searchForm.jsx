import Image from 'next/image'
import Navbar from '@/components/Navbar'
import React, {useState} from 'react'
import mathImg from '../public/assets/project-images/mandelbrot.jpg'
import Link from 'next/link'
import {AiOutlineClose, AiOutlineMenu, AiOutlineMail} from 'react-icons/ai'
import {FaGithub, FaLinkedinIn} from 'react-icons/fa'
import {BsFillPersonLinesFill} from 'react-icons/bs'
import {RiRadioButtonFill} from 'react-icons/ri'
import SearchForm from '@/components/SearchForm'

const form = () => {
    return (
        <>
        <Navbar />
        < SearchForm/>
        </>
    );
};

export default form;