function delay(n){
    return new Promise(function(resolve){
        setTimeout(resolve,n*1000);
    });
}
const jsondata = {
    Date : 20
};

async function myAsyncFunction(){
    while(1){
        const date = document.getElementsByClassName('date')
        const facilities_name = document.getElementsByClassName('facilities name')
        const facilities_index = 0
        if (facilities_name==='dry machine'){
            facilities_index = 0
        }   else if(facilities_name==='bathroom'){
            facilities_index = 1
        }   else if(facilities_name==='washing machine'){
            facilities_index = 2
        }   else if(facilities_name==='toilet'){
            facilities_index = 3
        }
        console.log("start to fetch data")
        fetch('http://140.115.200.38:80/dorm/getJsondata')
            .then((response) => {
                console.log("response.json()",response)
                return response.json();
            })
            .then((data) => {
                // console.log("data",data[0]["fields"]['Date'])
                jsondata.Date = data[facilities_index]["fields"]['Date']
                date[facilities_index].innerText = jsondata.Date
                console.log(jsondata.Date)
            })
            // .catch((error) => {
            //     console.log(`Error: ${error}`);
            // });

        await delay(10);
        }
}

myAsyncFunction();
