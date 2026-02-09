import mobileBgImg from "../../../HelperFunctions/mobileBgImg";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faXmark } from "@fortawesome/free-solid-svg-icons";


export function SignInContainer({
    setLogIn
}){
    const labelTextInput = (labelTitle, inputType) => {
        return(
            <div
                className="w-9/10 flex flex-col h-2/10 mt-10 ml-10"
            >
                <label>
                    {labelTitle}
                </label>

                <input 
                    type={inputType}
                    className="border rounded-lg h-10 text-center"
                />
            </div>
        )
    }

    return(
        <div
            className="h-2/3 w-9/10 bg-white rounded-lg grid grid-cols-[2fr_3fr]"
        >
            <div 
                style={{backgroundImage: mobileBgImg("4")}}
                className="bg-no-repeat bg-center bg-cover"
            />

            <div
                className="flex flex-col items-center"
            >
                <div
                    className="w-9/10 border-b border-gray-300 self-center justify-self-center text-center mt-4 flex items-center justify-between"
                >
                    <h1>Sign In to Nihongo</h1>

                    <FontAwesomeIcon icon={faXmark} 
                        onClick={() => setLogIn(false)}
                        className="text-red-500 rounded-full text-2xl hover:bg-gray-500 cursor-pointer"
                    />
                </div>

                {labelTextInput("Enter Email", "text")}

                {labelTextInput("Enter Password", "password")}

                <button
                    className="bg-green-600 text-white w-30 h-15 rounded-lg cursor-pointer hover:-translate-y-2 duration-200"
                >
                    Sign In
                </button>
            </div>
        </div>
    )
}