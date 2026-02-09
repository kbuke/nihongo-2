import { useScrollLock } from "./useScrollLock";

export function PopUp({popUpPage}){
    useScrollLock(true)

    return(
        <div
            className="fixed flex inset-0 z-50 justify-center items-center bg-black/40"
        >
            {popUpPage}
        </div>
    )
}