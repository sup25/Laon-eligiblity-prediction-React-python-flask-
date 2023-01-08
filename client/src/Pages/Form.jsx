import React, { useState  } from 'react';
import './form.css';
import axios from 'axios';
import { Link } from 'react-router-dom'

//axios is used to send data from a React component to a Python backend and a POST request.
function Form() {
    const [isModalOpen, setIsModalOpen] = useState(false);

    function openModal() {
      setIsModalOpen(true);
    
    }
  
    function closeModal() {
      setIsModalOpen(false);
    }

    

    const [data, setData] = useState('');
    const [selectedOption1, setSelectedOption1] = useState('');
    const [selectedOption2, setSelectedOption2] = useState('');
    const [selectedOption3, setSelectedOption3] = useState('');


    function handleChange(event) {
        const { name, value } = event.target;
        setData(prevData => ({ ...prevData, [name]: value }));

    }

    function handleChange1(event) {
        setSelectedOption1(event.target.value);
        const { name, value } = event.target;
        setData(prevData => ({ ...prevData, [name]: value }));
    }

    function handleChange2(event) {
        setSelectedOption2(event.target.value);
        const { name, value } = event.target;
        setData(prevData => ({ ...prevData, [name]: value }));
    }
    function handleChange3(event) {
        setSelectedOption3(event.target.value);
        const { name, value } = event.target;
        setData(prevData => ({ ...prevData, [name]: value }));
    }


  

    async function handleSubmit(event) {
        event.preventDefault();//prevents reload of the page
         try {
            const response = await axios.post('/api/send-data', { data });
            alert(response.data["Remarks"]);
             
            
            
        } catch (error) {
            console.error(error);
        }
        console.log(data);// values are stored in data when we click submit button
        
    
    }
   
      

    return (
        <form onSubmit={handleSubmit}  >

            <label>
                <h3> Name</h3>
                <input type="text"
                    name="name"
                    placeholder='Full Name'
                    onChange={handleChange} />
            </label>
            <br />
            <label>
                <h3>Gender</h3>
                <select name="Gender"
                    onChange={handleChange}>
                    <option default value="" >Select</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>
            </label>
            <br />
            <div>
                <h3>Marital Status</h3>
                <label>
                    <input
                        type="radio"
                        name="married"
                        value="Yes"
                        checked={selectedOption1 === 'Yes'}
                        onChange={handleChange1}
                    />
                    Yes
                </label>
                <br />
                <label>
                    <input
                        type="radio"
                        name="married"
                        value="No"
                        checked={selectedOption1 === 'No'}
                        onChange={handleChange1}
                    />
                    No
                </label>
            </div>
            <br />
            <h3>Dependents</h3>
            <label>
                <input
                    type="radio"
                    name="dependents"
                    value="0"
                    checked={selectedOption2 === '0'}
                    onChange={handleChange2}
                />
                0
            </label>
            <br />
            <label>
                <input
                    type="radio"
                    name="dependents"
                    value="1"
                    checked={selectedOption2 === '1'}
                    onChange={handleChange2}
                />
                1
            </label>
            <br />
            <label>
                <input
                    type="radio"
                    name="dependents"
                    value='2'
                    checked={selectedOption2 === '2'}
                    onChange={handleChange2}
                />
                2
            </label>
            <br />
            <label>
                <input
                    type="radio"
                    name="dependents"
                    value='3 or 3+'
                    checked={selectedOption2 === '3 or 3+'}
                    onChange={handleChange2}
                />
                3 or 3+
            </label>
            <br />
            <label>
                <h3>Education</h3>
                <select name="education"
                    onChange={handleChange}>
                    <option default value="">Select</option>
                    <option value="Graduate">Graduate</option>
                    <option value="Not Graduate">Not Graduate</option>

                </select>
            </label>
            <br />
            <h3>Self Employed</h3>
            <label>
                <input
                    type="radio"
                    name="selfEmployed"
                    value="Yes"
                    checked={selectedOption3 === 'Yes'}
                    onChange={handleChange3}
                />
                Yes
            </label>
            <br />
            <label>
                <input
                    type="radio"
                    name="selfEmployed"
                    value="No"
                    checked={selectedOption3 === 'No'}
                    onChange={handleChange3}
                />
                No
            </label>
            <br />
            <label>
                <h3>Credit History</h3>
                <input type="number"
                    name="creditHistory"
                    placeholder='Credit History'
                    onChange={handleChange} />
            </label>
            <br />
            <label>
                <h3>Property Area</h3>
                <select name="Area"
                    onChange={handleChange}>
                    <option default value="">Select</option>
                    <option value="Urban">Urban</option>
                    <option value="semiUrban">Semi Urban</option>
                    <option value="Rular">Rular</option>
                </select>
            </label>
            <br />
            <label>
                <h3>Applicant Income </h3>
                <input type="number"
                    name="applicantIncome"
                    placeholder='Applicant Income '
                    onChange={handleChange} />
            </label>
            <br />
            <label>
                <h3>Loan Amount </h3>
                <input type="number"
                    name="loanAmount"
                    placeholder='Loan Amount '
                    onChange={handleChange} />
            </label>
            <br />
            <label>
                <h3>Loan Amount Term </h3>
                <input type="number"
                    name="loanAmountTerm"
                    placeholder='Loan Amount Term '
                    onChange={handleChange} />
            </label>
            <br />
            <label>
                <h3>Total Income </h3>
                <input type="number"
                    name="totalIncome"
                    placeholder='Total Income '
                    onChange={handleChange} />
            </label>
            <br />

            
        {isModalOpen && (
        <div id='style-one'>
          <div id='style-two'>
            <h2>See Information about banks?</h2>
            <p>Visit our <Link to='/Blog'>Blog</Link> content to know more!</p>
            <button onClick={closeModal}>Close</button>
          </div>
        </div>
      )}
          
        
        <button  onClick={openModal}  type="submit">Submit</button>
        </form>
    );
}

export default Form;
