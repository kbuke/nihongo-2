// VerificationPage.jsx
import { useEffect, useState } from "react"
import mobileBgImg from "../../HelperFunctions/mobileBgImg"
import desktopBgImg from "../../HelperFunctions/desktopBgImg"

export default function VerificationPage() {
  const [status, setStatus] = useState("Verifying...")

  const welcomeContainer = () => {
    return (
      <div className="bg-black/80 h-9/10 w-9/10 grid grid-cols-[1fr_2fr] text-white rounded-xl overflow-hidden overflow-y-auto">
        <h1
          className="self-center justify-self-center lg:font-bold text-7xl"
          style={{ writingMode: "vertical-rl" }}
        >
          いらっしゃいませ
        </h1>

        <div className="py-10 flex flex-col items-center justify-center">
          <h1 className="text-3xl font-bold uppercase mb-4 lg:text-6xl">
            Welcome to Nihongo
          </h1>
          <p className="lg:text-2xl px-2">
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ex
            voluptatem maiores saepe deserunt dolor. Quibusdam, accusamus.
            Laborum consectetur quidem id soluta. Natus esse tempora provident
            aliquam placeat expedita nam culpa. Lorem ipsum dolor, sit amet
            consectetur adipisicing elit. Voluptates reprehenderit aspernatur
            adipisci consectetur tempora, quam enim, quisquam minus beatae fuga,
            assumenda harum? Eveniet aliquam impedit dolores laboriosam quia
            nihil qui?
          </p>

          <button className="bg-[rgba(0,100,0,1)] p-4 w-40 mt-10 rounded-xl uppercase tracking-widest cursor-pointer hover:-translate-y-2 duration-200">
            Sign In
          </button>
        </div>
      </div>
    )
  }

  useEffect(() => {
    const params = new URLSearchParams(window.location.search)
    const token = params.get("token")

    if (!token) {
      setStatus("No token provided.")
      return
    }

    fetch("http://localhost:5555/users/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ token }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.message) setStatus(data.message)
        else if (data.error) setStatus(data.error)
      })
      .catch(() => setStatus("An error occurred."))
  }, [])

  return (
    <>
      <div
        className="md:hidden h-screen w-full bg-center bg-no-repeat bg-cover flex items-center justify-center"
        style={{ backgroundImage: mobileBgImg("welcomeImg.png") }}
      >
        {welcomeContainer()}
      </div>

      <div
        className="hidden bg-no-repeat bg-center bg-cover w-full h-screen md:flex items-center justify-center"
        style={{ backgroundImage: desktopBgImg("verify.png") }}
      >
        {welcomeContainer()}
      </div>
    </>
  )
}
