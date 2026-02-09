import { createBrowserRouter } from "react-router";

import App from "./App";
import VerificationPage from "./Pages/VerificationPage/VerificationPage";
import { NoSignInHome } from "./Pages/NoSignInHome/NoSignInHome";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            // Create object with path and element keys 
            {
                index: true,
                element: <NoSignInHome />
            },

            {
                path: "/verify",
                element: <VerificationPage />
            }
        ]
    }
])