function delay(n){
    return new Promise(function(resolve){
        setTimeout(resolve,n*1000);
    });
}

async function myAsyncFunction(){
    while(1){
        const washingMachine = document.getElementById('wash-box-1');

        console.log("start to fetch data");
        fetch('http://140.115.200.38:80/dorm/getJsondata')
            .then((response) => {
                console.log("response.json()",response)
                return response.json();
            })
            .then((data) => { 
                washingMachine_battery = data[2]["fields"]['battery']
                console.log(washingMachine_battery)
                
                if (parseInt(washingMachine_battery) > 10){
                    washingMachine.style.background= 'yellow'
                }else{
                    washingMachine.style.background= '#609755'
                }

            })
            .catch((error) => {
                console.log(`Error: ${error}`);
            });
        
            
        await delay(10);
        }
}

myAsyncFunction();

// API pratice
fetch("https://api.unsplash.com/photos/random/?client_id=28snvwYLK_PZOGpDBVrXCf62otQb0xR3RRmiToO6ggs")
    .then((res) => {
        const data = res.json();
        return data;
    })
    .then((data) => {
        console.log(data);
        for (let i = 0; i < data.length; i++) {
            let container = document.querySelector(".container");
            let img = document.createElement("img");
            img.setAttribute("src", data[i].urls.small);
            container.append(img);
        }
    });