import React from 'react'
import Form from './Pages/Form';
import Navbar from './components/Navbar';
import Blog from './Pages/Blog';
import {
  createBrowserRouter,
  RouterProvider,

  Outlet,
} from "react-router-dom";
//outlet renders whole body of our webpage
const Layout = () => {
  return (
    <>
      <Navbar />

      <Outlet />

    </>
  )
}

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Form />
      },
      {
        path: "/Blog",
        element: <Blog />
      },

    ]
  },

]);




function App() {
  //only for checking the connection, not needed 
  //delete python route if you delete this
  // const [data, setData] = useState([{}])

  // useEffect(() => {
  //   fetch("/members").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data);
  //     }
  //   )
  // }, [])
  return (
    <div>
      <RouterProvider router={router} />



      {/* used this just to see the connection, not needed */}
      {/* {(typeof data.members === 'undefined') ? (
        <p></p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )} */}

    </div>
  )

}

export default App