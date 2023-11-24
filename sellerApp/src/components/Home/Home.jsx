import carsData from "../data/carsData.json";

function CarList() {
  const carList = carsData.cars;

  return (
    <div className="flex bg-powderblue shadow-lg rounded-lg p-6">
      <ul className=" flex flex-wrap">
        {carList.map((car, index) => (
          <div key={index} className=" w-1/3 p-2">
            <div className="bg-white shadow-lg rounded-lg p-2">
              <div className="box">
                <img className=" rounded-lg" src={car.images} alt="" />
              </div>
              <div className="flex ">
                <div className="flex flex-wrap items-center">
                  <h2 className="text-xl font-semibold mb-2">{car.car_name}</h2>
                  <button className="ml-16">{car.launch_year}</button>
                </div>
              </div>
              <div className="flex flex-wrap">
                <div className="w-1/2">{car.seating_capacity} People</div>
                <div className="w-1/2">{car.fuel_type}</div>
                <div className="w-1/2">{car.mileage}</div>
                <div className="w-1/2">{car.shift_type}</div>
              </div>
              <div>
                <div className="">{car.price}</div>
              </div>
            </div>
          </div>
        ))}
      </ul>
    </div>
  );
}

export default CarList;
