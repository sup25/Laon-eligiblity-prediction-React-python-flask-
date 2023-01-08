
import React from 'react';
import { Link } from 'react-router-dom'
import logo from '../components/img/logo.png'
import "./navbar.css"; // Importing a stylesheet for the navbar

function Navbar() {
    return (
        <>
            <nav>
                
                   <div >
                    <Link to='/'>
                   <img className='logo'       
                    src={logo} alt="Logo" />
                    </Link> 
                    </div> 
                    
                    

                    
              

                <div>
                    <ul id="navbar">
                        <li>
                        <a href='index.html'>
                           <Link to='/'>
                                Home
                         </Link>
                         </a>
                        </li>

                        <li>
                        <a href='index.html'>
                           <Link to='/Blog'>
                                Blog
                                </Link>
                            </a>
                        </li>
                        <li>
                            <a href='index.html'>
                                About
                            </a>
                        </li>
                        <li>
                            <a href='index.html'>
                                Contact
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>
        </>
    );
}

export default Navbar;
