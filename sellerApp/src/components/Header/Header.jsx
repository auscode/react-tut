import { useState } from "react";
function Header() {
  const [showDropdown1, setShowDropdown1] = useState(false);
  const [showDropdown2, setShowDropdown2] = useState(false);
  const toggleDropdown1 = () => {
    setShowDropdown1(!showDropdown1);
  };
  const toggleDropdown2 = () => {
    setShowDropdown2(!showDropdown2);
  };
  return (
    <header className="flex space-x-4 bg-gray-800 px-8 py-4 mt-0 rounded-lg">
      <div className=" flex search-bar">
        <input className="p-2 rounded-lg py-1.5" type="text" placeholder="Search..." />
      </div>
      <div className="dropdown">
        <div className=" text-white" onClick={toggleDropdown1}>
          Relevance
        </div>
        {showDropdown1 && (
          <ul>
            <li>Option 1</li>
            <li>Option 2</li>
            <li>Option 3</li>
          </ul>
        )}
      </div>
      <div className="dropdown ">
        <button className="text-white" onClick={toggleDropdown2}>
          All brands
        </button>
        {showDropdown2 && (
            <ul>
              <li>Option A</li>
              <li>Option B</li>
              <li>Option C</li>
            </ul>
        )}
      </div>
    </header>
  );
}

export default Header;
