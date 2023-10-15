import React, {useState} from 'react'
import Image from 'next/image'
import contactImg from '../public/assets/contact.jpg'
import Link from 'next/link'
import {AiOutlineClose, AiOutlineMenu, AiOutlineMail} from 'react-icons/ai'
import {FaGithub, FaLinkedinIn} from 'react-icons/fa'
import {BsFillPersonLinesFill} from 'react-icons/bs'
import {HiOutlineChevronDoubleUp} from 'react-icons/hi'


const ShareForm = () => {
    return (
        <div id='contact' className='w-full lg:h-screen'>
            <div className='max-w-[1080px] py-32 m-auto px-2 w-full'>
                <p className='text-xl tracking-widest uppercase text-[#5651e5]'>Contact</p>
                <h2 className='py-4'>Get In Touch</h2>
                <div className='grid md:grid-cols-5 gap-8'>
                    {/* left */}
                    <div className='col-span-3 md:col-span-2 w-full h-full shadow-xl shadow-gray-400 rounded-xl p-4'>
                        <div className='lg:p-4 h-full'>
                            <div className='hidden md:flex'>
                                <Image src={contactImg} className='rounded-xl' alt='/' /> {/* hover:scale-105 ease-in duration-200 */}
                            </div>
                            <div>
                                <h2 className='py-2'>CSW</h2>
                                <p>Fill out dis form</p>
                                <p className='py-4'></p>
                            </div>
                            <div>
                                <p className='uppercase pt-8'>Connect With Us</p>
                                <div className='flex items-cetner justify-between py-4'>
                                    <a href="http://www.linkedin.com/in/leo-curdi" target='_blank' rel='noreferrer'>
                                        <div className='rounded-full shadow-lg shadow-gray-400 p-[1.2rem] cursor-pointer hover:scale-110 ease-in duration-200'>
                                            <FaLinkedinIn size={25} />
                                        </div>
                                    </a>
                                    <a href="https://github.com/LeoCurdi" target='_blank' rel='noreferrer'>
                                        <div className='rounded-full shadow-lg shadow-gray-400 p-[1.2rem] cursor-pointer hover:scale-110 ease-in duration-200'>
                                            <FaGithub size={25} />
                                        </div>
                                    </a>
                                    <a href="/assets/Resume.pdf" rel='noreferrer'>
                                        <div className='rounded-full shadow-lg shadow-gray-400 p-[1.2rem] cursor-pointer hover:scale-110 ease-in duration-200'>
                                            <BsFillPersonLinesFill size={25} />
                                        </div>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* right */}
                    <div className='col-span-3 w-full h-auto shadow-xl shadow-gray-400 rounded-xl lg:p-4'>
                        <div className='p-4'>
                            <form>

                                <div className='grid md:grid-cols-2 gap-4 w-full py-1'>

                                    <div className='flex flex-col'>
                                        <label className='uppercase text-sm py-1'>Name</label>
                                        <input className='border-2 rounded-lg p-2 flex border-gray-300' type="text" />
                                    </div>

                                    <div className='flex flex-col'>
                                        <label className='uppercase text-sm py-1'>Phone Number</label>
                                        <input className='border-2 rounded-lg p-2 flex border-gray-300' type="text" />
                                    </div>

                                </div>

                                <div className='flex flex-col py-1'>
                                    <label className='uppercase text-sm py-1'>Address</label>
                                    <input className='border-2 rounded-lg p-2 flex border-gray-300' type="email" />
                                </div>

                                <div className='flex flex-col py-1'>
                                    <label className='uppercase text-sm py-1'>Social Security Number</label>
                                    <input className='border-2 rounded-lg p-2 flex border-gray-300' type="text" />
                                </div>

                                <div className='flex flex-col py-1'>
                                    <label className='uppercase text-sm py-1'>Bank account information</label>
                                    <textarea className='border-2 rounded-lg p-2 border-gray-300' rows='5'></textarea>
                                </div>

                                <button className='w-full p-4 text-gray-100 mt-4'>Send Message</button>

                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ShareForm;