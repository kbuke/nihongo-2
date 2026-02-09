import mobileBgImg from "../../../HelperFunctions/mobileBgImg"
import { SignIn } from "./SignIn"

export function MobileHome(){
    return(
        <>
            {/* Background */}
            <div
                className="fixed inset-0 bg-cover bg-center -z-20"
                style={{ backgroundImage: mobileBgImg("signUpHomeImg") }}
            />
    
            {/* Fixed header */}
            <div className="fixed top-0 left-0 w-full z-20">
                <SignIn />
            </div>
    
            {/* Scroll content */}
            <section className="relative z-10">
            {/* Scroll trigger */}
                <div className="h-screen" />
                {/* Centered overlay */}
                <div className="min-h-screen flex items-center justify-center px-4">
                    <div className="bg-black/60 backdrop-blur-md text-white p-10 rounded-xl text-center">
                        <div className="border-b border-white">
                            <h1 className="text-4xl font-bold uppercase">
                            Welcome to Nihongo
                            </h1>
            
                            <img
                            src={`NihongoPics/nihongoLogo.png`}
                            className="mx-auto mt-4 h-40"
                            alt="Nihongo Logo"
                            />
            
                            <h3 className="text-2xl font-bold">
                            Your go-to travel app for Japan.
                            </h3>
                        </div>
                    </div>
                </div>
            </section>
        </>
    )
}