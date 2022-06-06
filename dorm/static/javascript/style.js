function delay(n) {
    return new Promise(function (resolve) {
        setTimeout(resolve, n * 1000);
    });
}

async function myAsyncFunction() {
    while (1) {
        const washingMachine_box1 = document.getElementById('wash-box-1');
        const washingMachine_1 = document.getElementById('washingMachine-1');
        const shower_box1 = document.getElementById('bath-box-1');
        const shower_1 = document.getElementById('shower-1');
        const disabled_box1 = document.getElementById('dis-box-1');
        const disabled_1 = document.getElementById('disabled-1');
        const dryerMachine_box1 = document.getElementById('dry-box-1');
        const dryerMachine_1 = document.getElementById('dryerMachine-1');

        console.log("start to fetch data");
        fetch('http://140.115.200.38:80/dorm/getJsondata')
            .then((response) => {
                console.log("response.json()", response);
                return response.json();
            })
            .then((data) => {
                washingMachine_box1_usage = data[0]["fields"]['battery'];
                washingMachine_1_usage = data[0]["fields"]['battery'];
                shower_box1_usage = data[1]["fields"]['battery'];
                shower_1_usage = data[1]["fields"]['battery'];
                disabled_box1_usage = data[2]["fields"]['battery'];
                disabled_1_usage = data[2]["fields"]['battery'];
                dryerMachine_box1_usage = data[3]["fields"]['battery'];
                dryerMachine_1_usage = data[3]["fields"]['battery'];
                
                console.log("washingMachine_1_usage",washingMachine_1_usage);
                console.log(shower_1_usage);
                console.log(disabled_1_usage);
                console.log(dryerMachine_1_usage);

                if (parseInt(washingMachine_box1_usage) > 10) {
                    washingMachine_box1.style.background = 'yellow';
                    washingMachine_1.style.fill = '#4071F5';
                } else {
                    washingMachine_1.style.fill = 'white';
                    washingMachine_box1.style.background = '#609755';
                }

                if (parseInt(shower_1_usage) > 10) {
                    shower_1.style.opacity = 1;
                    shower_box1.style.background = 'yellow';
                } else {
                    shower_1.style.opacity = 0.1;
                    shower_box1.style.background = '#609755';
                }

                if (parseInt(disabled_1_usage) > 10) {
                    disabled_1.style.opacity = 1;
                    disabled_box1.style.background = 'yellow';
                } else {
                    disabled_1.style.opacity = 0.1;
                    disabled_box1.style.background = '#609755';
                }

                if (parseInt(dryerMachine_1_usage) > 10) {
                    dryerMachine_1.style.animation = 'dash 1.4s linear infinite';
                    dryerMachine_box1.style.background = 'yellow';
                } else {
                    dryerMachine_box1.style.background = '#609755';
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