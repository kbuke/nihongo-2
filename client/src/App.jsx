import { Outlet } from "react-router"

function App() {
    return(
        <div>
            <h2 className="text-lg">
                Tester
            </h2>
            <Outlet />
        </div>
    )
}

export default App
