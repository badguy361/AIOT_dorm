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
        console.log("start to fetch data")
        fetch('http://140.115.200.38:80/dorm/example')
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                jsondata.Date = data.Date
                console.log(jsondata)
            })
            .catch((error) => {
                console.log(`Error: ${error}`);
            });

        await delay(10);
        }
}

myAsyncFunction();
