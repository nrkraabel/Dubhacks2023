import Image from 'next/image'
import React, {useState} from 'react'
import yelpSkiImg from '../public/assets/project-images/yelpSki1-Copy.png'
import sortingVisualizerImg from '../public/assets/project-images/sortingVisualizer.png'
import cosmicClashImg from '../public/assets/project-images/cosmicClash.png'
import matrixImg from '../public/assets/project-images/matrix.png'
import nasaImg from '../public/assets/project-images/nasa.png'
import physicsImg from '../public/assets/project-images/physics.png'
import mathImg from '../public/assets/project-images/mandelbrot.jpg'
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
                    <LandingItem title='About' backgroundImg={yelpSkiImg} projectUrl='/yelpSki' tech='test' />
                    <LandingItem title='Search' backgroundImg={yelpSkiImg} projectUrl='/SearchForm' tech='test' />
                    <LandingItem title='Share' backgroundImg={yelpSkiImg} projectUrl='/ShareForm' tech='test' />
                </div>
            </div>
        </div>
    );
};

export default LandingLower;