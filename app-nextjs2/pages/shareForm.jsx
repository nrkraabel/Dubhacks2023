import Image from 'next/image'
import Navbar from '@/components/Navbar'
import React, {useState} from 'react'
import Link from 'next/link'
import {AiOutlineClose, AiOutlineMenu, AiOutlineMail} from 'react-icons/ai'
import {FaGithub, FaLinkedinIn} from 'react-icons/fa'
import {BsFillPersonLinesFill} from 'react-icons/bs'
import {RiRadioButtonFill} from 'react-icons/ri'
import ShareForm from '@/components/ShareForm'

const shareForm = () => {
    return (
        <>
        <Navbar />
        < ShareForm/>
        </>
    );
};

export default shareForm;