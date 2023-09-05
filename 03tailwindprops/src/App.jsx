// import { useState } from 'react'
import './App.css'
import Card from './components/Card';

function App() {
  // const [count, setCount] = useState(0)

  // let myObj ={
  //   username:"harsh",
  //   age:21
  // }
  
  // let newArr=[1,2,3]

  return (
    <>
      <h1 className="bg-green-400 text-black p-4 rounded-xl mb-4">
        Test Tailwind
      </h1>
      <Card username="chaiorcode" btnText="click me" />
      <Card username="auscode" btnText="visit me " />
    </>
  );
}

export default App
