import { useState } from "react";
import "./App.css";

function App() {
  const [counter, setCounter] = useState(15);
  // let counter =15
  const addValue = () => {
    if (counter < 20) {
      console.log("clicked", counter);
      // counter = counter+1;
      setCounter(counter + 1);
    }
  };
  const removeValue = () => {
    if (counter > 0) {
      console.log("clicked", counter);
      // counter = counter+1;
      setCounter(counter - 1);
    }
  };
  return (
    <>
      <h1>chai aur code</h1>
      <h2>Counter value: {counter} </h2>

      <button onClick={addValue}> Add Value {counter}</button>
      <br />
      <br />
      <button onClick={removeValue}> Remove Value {counter} </button>
      {/* <p> footer : {counter}</p> */}
      <br />
    </>
  );
}
export default App;
