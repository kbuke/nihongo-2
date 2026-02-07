import { createBrowserRouter } from "react-router";

import App from "./App";
import VerificationPage from "./Pages/VerificationPage/VerificationPage";
import { HomePg } from "./Pages/HomePg";

export const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            // Create object with path and element keys 
            {
                index: true,
                element: <HomePg />
            },

            {
                path: "/verify",
                element: <VerificationPage />
            }
        ]
    }
])