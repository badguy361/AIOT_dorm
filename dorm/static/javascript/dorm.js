function delay(n){
    return new Promise(function(resolve){
        setTimeout(resolve,n*1000);
    });
}
const jsondata = {
    Date : 20,
    facilities_name : 'dry machine', 
    facilities_useage: 0, 
    Acce:0.0 ,
    Acce_X:0.0, 
    Acce_Y:0.0,
    Acce_Z:0.0,
    Temp:0.0,
    Current:0.0,
    Power:0.0,
    Voltage:0.0, 
    battery:0.0
};

async function myAsyncFunction(){
    while(1){
        const date = document.getElementsByClassName('date')
        const facilities_name = document.getElementsByClassName('facilities name')
        const facilities_useage = document.getElementsByClassName('facilities useage')
        const Acce = document.getElementsByClassName('facilities Acce')
        const Acce_X = document.getElementsByClassName('facilities Acce_X')
        const Acce_Y = document.getElementsByClassName('facilities Acce_Y')
        const Acce_Z = document.getElementsByClassName('facilities Acce_Z')
        const Temp = document.getElementsByClassName('facilities Temp')
        const Current = document.getElementsByClassName('facilities Current')
        const Power = document.getElementsByClassName('facilities Power')
        const Voltage = document.getElementsByClassName('facilities Voltage')
        const battery = document.getElementsByClassName('facilities battery')

        console.log("start to fetch data")
        fetch('http://140.115.200.38:80/dorm/getJsondata')
            .then((response) => {
                console.log("response.json()",response)
                return response.json();
            })
            .then((data) => { //impot response.json() value to data
                // console.log("data",data[0]["fields"]['Date'])
                for (let facilities_index = 0; facilities_index < 4; facilities_index++){
                    jsondata.Date = data[facilities_index]["fields"]['Date']
                    jsondata.facilities_name = data[facilities_index]["fields"]['facilities_name']
                    jsondata.facilities_useage = data[facilities_index]["fields"]['facilities_useage']
                    jsondata.Acce = data[facilities_index]["fields"]['Acce']
                    jsondata.Acce_X = data[facilities_index]["fields"]['Acce_X']
                    jsondata.Acce_Y = data[facilities_index]["fields"]['Acce_Y']
                    jsondata.Acce_Z = data[facilities_index]["fields"]['Acce_Z']
                    jsondata.Temp = data[facilities_index]["fields"]['Temp']
                    jsondata.Current = data[facilities_index]["fields"]['Current']
                    jsondata.Power = data[facilities_index]["fields"]['Power']
                    jsondata.Voltage = data[facilities_index]["fields"]['Voltage']
                    jsondata.battery = data[facilities_index]["fields"]['battery']

                    console.log(jsondata.Date)

                    date[facilities_index].innerText = jsondata.Date
                    facilities_name[facilities_index].innerText = jsondata.facilities_name
                    facilities_useage[facilities_index].innerText = jsondata.facilities_useage
                    Acce[facilities_index].innerText = jsondata.Acce
                    Acce_X[facilities_index].innerText = jsondata.Acce_X
                    Acce_Y[facilities_index].innerText = jsondata.Acce_Y
                    Acce_Z[facilities_index].innerText = jsondata.Acce_Z
                    Temp[facilities_index].innerText = jsondata.Temp
                    Current[facilities_index].innerText = jsondata.Current
                    Power[facilities_index].innerText = jsondata.Power
                    Voltage[facilities_index].innerText = jsondata.Voltage
                    battery[facilities_index].innerText = jsondata.battery
                }
            })
            .catch((error) => {
                console.log(`Error: ${error}`);
            });

        await delay(10);
        }
}

myAsyncFunction();
