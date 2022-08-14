function delay(n) {
    return new Promise(function (resolve) {
        setTimeout(resolve, n * 1000);
    });
}

async function myAsyncFunction() {
    while (1) {
        const f3washingMachine_box1 = document.getElementById('wash-box-3-1');
        const f3washingMachine_1 = document.getElementById('washingMachine-3-1');
        const f3washingMachine_box2 = document.getElementById('wash-box-3-2');
        const f3washingMachine_2 = document.getElementById('washingMachine-3-2');

        const f3shower_box1 = document.getElementById('bath-box-3-1');
        const f3shower_1 = document.getElementById('bath-3-1');
        const f3shower_box2 = document.getElementById('bath-box-3-2');
        const f3shower_2 = document.getElementById('bath-3-2');
        const f3shower_box3 = document.getElementById('bath-box-3-3');
        const f3shower_3 = document.getElementById('bath-3-3');
        const f3shower_box4 = document.getElementById('bath-box-3-4');
        const f3shower_4 = document.getElementById('bath-3-4');
        const f3shower_box5 = document.getElementById('bath-box-3-5');
        const f3shower_5 = document.getElementById('bath-3-5');
        const f3shower_box6 = document.getElementById('bath-box-3-6');
        const f3shower_6 = document.getElementById('bath-3-6');

        const f3disabled_box1 = document.getElementById('dis-box-3-1');
        const f3disabled_1 = document.getElementById('disabled-3-1');
        const f3dryerMachine_box1 = document.getElementById('dry-box-3-1');
        const f3dryerMachine_1 = document.getElementById('dryerMachine-3-1');

        const f3wc_1 = document.getElementById('wc-3-1');
        const f3wc_2 = document.getElementById('wc-3-2');
        const f3wc_3 = document.getElementById('wc-3-3');


        console.log("start to fetch data");
        fetch('http://127.0.0.1:8000/dorm/getJsondata1')
            .then((response) => {
                console.log("response.json()", response);
                return response.json();
            })
            .then((data) => {
                //這部分不太確定哪個欄位從哪裡讀資料
                washingMachine_box1_usage = data[0]["fields"]['battery'];
                washingMachine_1_usage = data[0]["fields"]['battery'];
                shower_box1_usage = data[1]["fields"]['battery'];
                shower_1_usage = data[1]["fields"]['battery'];
                disabled_box1_usage = data[2]["fields"]['battery'];
                disabled_1_usage = data[2]["fields"]['battery'];
                dryerMachine_box1_usage = data[3]["fields"]['battery'];
                dryerMachine_1_usage = data[3]["fields"]['battery'];

                console.log("washingMachine_1_usage", washingMachine_1_usage);
                console.log(shower_1_usage);
                console.log(disabled_1_usage);
                console.log(dryerMachine_1_usage);

                //下面的顏色動畫確定可以
                if (parseInt(f3washingMachine_box1_usage) > 10) {
                    f3washingMachine_box1.style.background = 'yellow';
                    f3washingMachine_1.style.fill = '#4071F5';
                } else {
                    f3washingMachine_1.style.fill = '#faf4f3';
                    f3washingMachine_box1.style.background = '#609755';
                }

                if (parseInt(f3washingMachine_box2_usage) > 10) {
                    f3washingMachine_box2.style.background = 'yellow';
                    f3washingMachine_2.style.fill = '#4071F5';
                } else {
                    f3washingMachine_2.style.fill = '#faf4f3';
                    f3washingMachine_box2.style.background = '#609755';
                }

                if (parseInt(f3shower_1_usage) > 10) {
                    f3shower_1.style.opacity = 1;
                    f3shower_box1.style.background = 'yellow';
                } else {
                    f3shower_1.style.opacity = 0.1;
                    f3shower_box1.style.background = '#609755';
                }

                if (parseInt(f3shower_2_usage) > 10) {
                    f3shower_2.style.opacity = 1;
                    f3shower_box2.style.background = 'yellow';
                } else {
                    f3shower_2.style.opacity = 0.1;
                    f3shower_box2.style.background = '#609755';
                }

                if (parseInt(f3shower_3_usage) > 10) {
                    f3shower_3.style.opacity = 1;
                    f3shower_box3.style.background = 'yellow';
                } else {
                    f3shower_3.style.opacity = 0.1;
                    f3shower_box3.style.background = '#609755';
                }
                if (parseInt(f3shower_4_usage) > 10) {
                    f3shower_4.style.opacity = 1;
                    f3shower_box4.style.background = 'yellow';
                } else {
                    f3shower_4.style.opacity = 0.1;
                    f3shower_box4.style.background = '#609755';
                }
                if (parseInt(f3shower_5_usage) > 10) {
                    f3shower_5.style.opacity = 1;
                    f3shower_box5.style.background = 'yellow';
                } else {
                    f3shower_5.style.opacity = 0.1;
                    f3shower_box5.style.background = '#609755';
                }
                if (parseInt(f3shower_6_usage) > 10) {
                    f3shower_6.style.opacity = 1;
                    f3shower_box6.style.background = 'yellow';
                } else {
                    f3shower_6.style.opacity = 0.1;
                    f3shower_box6.style.background = '#609755';
                }
                if (parseInt(f3disabled_1_usage) > 10) {
                    f3disabled_1.style.opacity = 1;
                    f3disabled_box1.style.background = 'yellow';
                } else {
                    f3disabled_1.style.opacity = 0.1;
                    f3disabled_box1.style.background = '#609755';
                }

                if (parseInt(f3dryerMachine_1_usage) > 10) {
                    f3dryerMachine_1.style.animation = 'dash 1.4s linear infinite';
                    f3dryerMachine_box1.style.background = 'yellow';
                } else {
                    f3dryerMachine_box1.style.background = '#609755';
                }

                if (parseInt(f3wc_1_usage) > 10) {
                    f3wc_1.style.opacity = 0.8;
                } else {
                    f3wc_1.style.opacity = 0.1;
                }
                if (parseInt(f3wc_2_usage) > 10) {
                    f3wc_2.style.opacity = 0.8;
                } else {
                    f3wc_2.style.opacity = 0.1;
                }
                if (parseInt(f3wc_3_usage) > 10) {
                    f3wc_3.style.opacity = 0.8;
                } else {
                    f3wc_3.style.opacity = 0.1;
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
// fetch("https://api.unsplash.com/photos/random/?client_id=28snvwYLK_PZOGpDBVrXCf62otQb0xR3RRmiToO6ggs")
//     .then((res) => {
//         const data = res.json();
//         return data;
//     })
//     .then((data) => {
//         console.log(data);
//         for (let i = 0; i < data.length; i++) {
//             let container = document.querySelector(".container");
//             let img = document.createElement("img");
//             img.setAttribute("src", data[i].urls.small);
//             container.append(img);
//         }
//     });