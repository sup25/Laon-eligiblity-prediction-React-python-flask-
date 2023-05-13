import React, { useState } from "react";
import "./form.css";
import { Link } from "react-router-dom";
import { MdError } from "react-icons/md";

function Form() {
  const [isDisable, setIsDisable] = useState(false);
  const [alertmsg, setAlertMsg] = useState("");

  function openModal() {
    setIsDisable(true);
  }

  function closeModal() {
    setIsDisable(false);
  }

  //all the initial state are set to null
  const [data, setData] = useState("");

  const [isInvalid4Called, setIsInvalid4Called] = useState(false);
  //this is for Number Field
  function handleChange(event) {
    const { name, value } = event.target;
    setData((prevData) => ({ ...prevData, [name]: value }));
    setIsInvalid4Called(true);
  }

  //this is for Dropdown
  function handleChange0(event) {
    const { name, value } = event.target;
    setData((prevData) => ({ ...prevData, [name]: value }));
  }
  //used for radio button
  const [selectedOption1, setSelectedOption1] = useState("");
  const [selectedOption2, setSelectedOption2] = useState("");
  const [selectedOption3, setSelectedOption3] = useState("");

  //Radio Buttons
  function handleChange1(event) {
    const { name, value } = event.target;
    switch (name) {
      case "married":
        setSelectedOption1(value);
        break;
      case "dependents":
        setSelectedOption2(value);
        break;
      case "selfEmployed":
        setSelectedOption3(value);
        break;
      default:
        break;
    }
    setData((prevData) => ({ ...prevData, [name]: value }));
  }

  function iconInvalid() {
    if (data.creditHistory > 9 || data.creditHistory < 0) {
      return "The credit history should be between 0 to 9 .";
    } else {
      return "";
    }
  }

  function iconInvalid2() {
    if (data.loanAmount > 10000000)
      return " The loan amount cannot be greater than 10 million ";
    else if (data.loanAmount < 100) {
      return "The loan amount cannot be less than 100";
    } else {
      return "";
    }
  }

  function iconInvalid3() {
    if (data.loanAmountTerm > 480 || data.loanAmountTerm < 1)
      return "The loan amount term should be between 1 to 480 months";
    else {
      return "";
    }
  }
  function iconInvalid4() {
    if (String(data.applicantIncome).length < 3)
      return "Applicant income cannot be less than 100";
    else {
      return "";
    }
  }

  function iconInvalid5() {
    if (String(data.totalIncome).length < String(data.applicantIncome).length)
      return "Total family income should be more than Applicant Income";
    else {
      return "";
    }
  }

  // This function handles the submission of a form by sending data to a server API endpoint
  function handleSubmit(event) {
    // Prevent the form from submitting normally
    event.preventDefault();

    // Send a POST request to the server API with the data in the body
    fetch("/api/send-data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ data }),
    })
      // Parse the response from the server as JSON
      .then((response) => response.json())
      // Update the UI with the response message
      .then((data) => setAlertMsg(data["Remarks"]))
      // Log any errors that occur during the request
      .catch((error) => console.error(error));
    // Log the data sent to the server
    console.log(data);
  }
  const isInvalid =
    iconInvalid() ||
    iconInvalid2() ||
    iconInvalid3() ||
    iconInvalid4() ||
    iconInvalid5();
  const isFormValid =
    data.name &&
    data.Gender &&
    selectedOption1 &&
    selectedOption2 &&
    data.education &&
    selectedOption3 &&
    data.Area &&
    data.applicantIncome &&
    data.totalIncome &&
    data.loanAmount &&
    data.loanAmountTerm &&
    data.creditHistory &&
    !isInvalid;

  return (
    <form onSubmit={handleSubmit}>
      <label>
        <h3> Name</h3>
        <input
          type="text"
          title="Please enter your full name"
          name="name"
          placeholder="Full Name"
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        <h3>Gender</h3>
        <select name="Gender" onChange={handleChange0}>
          <option default value="">
            Select
          </option>
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
            checked={selectedOption1 === "Yes"}
            onChange={handleChange1}
          />
          &nbsp; Yes
        </label>
        <br />
        <label>
          <input
            type="radio"
            name="married"
            value="No"
            checked={selectedOption1 === "No"}
            onChange={handleChange1}
          />
          &nbsp; No
        </label>
      </div>
      <br />
      <h3>Dependents</h3>
      <label>
        <input
          type="radio"
          name="dependents"
          value="0"
          checked={selectedOption2 === "0"}
          onChange={handleChange1}
        />
        &nbsp;0
      </label>
      <br />
      <label>
        <input
          type="radio"
          name="dependents"
          value="1"
          checked={selectedOption2 === "1"}
          onChange={handleChange1}
        />
        &nbsp; 1
      </label>
      <br />
      <label>
        <input
          type="radio"
          name="dependents"
          value="2"
          checked={selectedOption2 === "2"}
          onChange={handleChange1}
        />
        &nbsp; 2
      </label>
      <br />
      <label>
        <input
          type="radio"
          name="dependents"
          value="3 or 3+"
          checked={selectedOption2 === "3 or 3+"}
          onChange={handleChange1}
        />
        &nbsp; 3 or 3+
      </label>
      <br />
      <label>
        <h3>Education</h3>
        <select name="education" onChange={handleChange0}>
          <option default value="">
            Select
          </option>
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
          checked={selectedOption3 === "Yes"}
          onChange={handleChange1}
        />
        &nbsp; Yes
      </label>
      <br />
      <label>
        <input
          type="radio"
          name="selfEmployed"
          value="No"
          checked={selectedOption3 === "No"}
          onChange={handleChange1}
        />
        &nbsp; No
      </label>
      <br />
      <label>
        <h3>Credit History</h3>
        <input
          type="number"
          name="creditHistory"
          placeholder="Credit History"
          onChange={handleChange}
          required
          min="0"
        />
        {iconInvalid() && (
          <div>
            <MdError color="red" size={20} />
            <span>{iconInvalid()}</span>
          </div>
        )}
      </label>
      <br />
      <label>
        <h3>Property Area</h3>
        <select name="Area" onChange={handleChange0}>
          <option default value="">
            Select
          </option>
          <option value="Urban">Urban</option>
          <option value="semiUrban">Semi Urban</option>
          <option value="Rular">Rular</option>
        </select>
      </label>
      <br />
      <label>
        <h3>Applicant Income </h3>
        <input
          type="number"
          name="applicantIncome"
          placeholder="Applicant Income "
          onChange={handleChange}
          required
        />
        {iconInvalid4() && <MdError color="red" size={20} />}
        <span>{iconInvalid4()}</span>
      </label>
      <br />
      <label>
        <h3>Loan Amount </h3>
        <input
          type="number"
          name="loanAmount"
          value={data.loanAmount}
          placeholder="Loan Amount "
          onChange={handleChange}
          required
        />
        {iconInvalid2() && <MdError color="red" size={20} />}
        <span>{iconInvalid2()}</span>
      </label>
      <br />
      <label>
        <h3>Loan Amount Term (month/s) </h3>
        <input
          type="number"
          name="loanAmountTerm"
          value={data.loanAmountTerm}
          placeholder="Loan Amount Term "
          onChange={handleChange}
          required
          min="1"
          max="480"
        />
        {iconInvalid3() && <MdError color="red" size={20} />}
        <span>{iconInvalid3()}</span>
      </label>
      <br />
      <label>
        <h3>Total Family Income </h3>
        <input
          type="number"
          name="totalIncome"
          placeholder="Total Income "
          onChange={handleChange}
          required
        />
        {iconInvalid5() && <MdError color="red" size={20} />}
        <span>{iconInvalid5()}</span>
      </label>
      <br />

      {isDisable && (
        <div id="style-one">
          <div id="style-two">
            <h3>{alertmsg}</h3>
            <h2>See Information about banks?</h2>
            <p>
              Visit our <Link to="/Blog">Blog</Link> content to know more!
            </p>
            <button onClick={closeModal}>Close</button>
          </div>
        </div>
      )}

      <button
        class="disable"
        onClick={openModal}
        type="submit"
        disabled={!isFormValid}
      >
        Submit
      </button>
    </form>
  );
}

export default Form;
