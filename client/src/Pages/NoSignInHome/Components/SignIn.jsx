import { renderLandscapeImg } from "../../../HelperFunctions/renderLandscapemg"

export function SignIn({
    setSignIn
}) {
  // Create Sign-In and Sign-Up Buttons
  const homeNavButtons = (buttonType) => {
    return (
      <button
        className={`
            text-white px-4 rounded-md w-3/10 h-3/5 lg:h-2/5 lg:w-12/100 hover:-translate-y-2 duration-200 cursor-pointer
            ${buttonType === "Sign Up" ? "bg-[rgba(0,100,0,1)]" : "bg-[rgba(0,0,100,1)]"} uppercase
        `}
        onClick={buttonType === "Sign In" ? () => setSignIn(true) : null}
      >
        {buttonType}
      </button>
    )
  }

  return (
    <div className="h-20 lg:h-30 w-full flex flex-row items-center justify-around px-2 z-20 top-20 mt-0">
        <img 
            src={renderLandscapeImg("nihongoLogo")}
            className="h-20 lg:h-30"
        />
        {homeNavButtons("Sign Up")}
        {homeNavButtons("Sign In")}
    </div>
  )
}
