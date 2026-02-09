import { useState } from "react"
import { DesktopHome } from "./Components/DesktopHome"
import { MobileHome } from "./Components/MobileHome"
import { PopUp } from "../../Components/PopUp"
import { SignInContainer } from "./Components/SignInContainer"

export function NoSignInHome() {
    const [signIn, setSignIn] = useState(false)

    return (
    <>
        <div
        className="flex lg:hidden"
        >
        <MobileHome />
        </div>

        <div
        className="hidden lg:block"
        >
        <DesktopHome 
            setSignIn={setSignIn}
        />
        </div>

        {signIn && (
            <PopUp 
                popUpPage={<SignInContainer setLogIn={setSignIn}/>}
            />
        )}
    </>
    )
}
