import Head from 'next/head'
import Image from 'next/image'
import Main from '../components/Main'
import LandingLower from '@/components/LandingLower'

export default function Home() {
  return (
    <>
        <Head>
            <title>DubHacks2023</title>
            <meta name="description" content="Generated by create next app" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <link rel="icon" href="/favicon.png" />
        </Head>

        <Main />
        < LandingLower/>

    </>
  )
}