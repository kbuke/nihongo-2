import { renderPortrait } from "../../../HelperFunctions/renderPortraitImg";
import video from "../../../HelperFunctions/video";
import { SignIn } from "./SignIn";

export function DesktopHome({
    setSignIn
}){
  return (
    <div className="relative h-screen w-full overflow-hidden flex flex-col">
      
      {/* Background video */}
      <video
        className="absolute inset-0 w-full h-full object-cover -z-10"
        autoPlay
        muted
        loop
        playsInline
      >
        <source src={video("nihongoWelcome")} type="video/mp4" />
      </video>

      {/* Fixed / top content */}
      <div className="relative z-20">
        <SignIn 
            setSignIn={setSignIn}
        />
      </div>

      {/* Centered hero */}
      <div className="relative z-20 flex-1 flex items-center justify-center text-black">
        <div className="flex flex-col items-center rounded-lg py-6 px-12">
          <h1 className="uppercase font-bold tracking-widest">
            Welcome to Nihongo
          </h1>

          <h2 className="mt-2 text-3xl font-bold">
            Your Go-To for Travel in Japan!
          </h2>

          <button
            className="mt-6 w-48 bg-red-500 text-white uppercase rounded-md h-12 hover:-translate-y-2 duration-200 cursor-pointer"
          >
            Learn More
          </button>
        </div>
      </div>

    </div>
  );
}
