function delay(n){
    return new Promise(function(resolve){
        setTimeout(resolve,n*1000);
    });
}
const jsondata = {
    Date : 20
};

async function myAsyncFunction(){
    //Do what you want here 
    while(1){
        console.log("start to fetch data")
        fetch('http://140.115.200.38:80/dorm/example')
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                // console.log(data.Date)
                jsondata.Date = data.Date
                console.log(jsondata)
            });
            // .catch((error) => {
            //     console.log(`Error: ${error}`);
            // })
            // mydata.Date = jsondata

        await delay(10);
        }
}

myAsyncFunction();
