function delay(n) {
    return new Promise(function (resolve) {
        setTimeout(resolve, n * 1000);
    });
}

async function myAsyncFunction() {
    while (1) {
        const f4washingMachine_box1 = document.getElementById('wash-box-4-1');
        const f4washingMachine_1 = document.getElementById('washingMachine-4-1');
        const f4washingMachine_box2 = document.getElementById('wash-box-4-2');
        const f4washingMachine_2 = document.getElementById('washingMachine-4-2');

        const f4shower_box1 = document.getElementById('bath-box-4-1');
        const f4shower_1 = document.getElementById('bath-4-1');
        const f4shower_box2 = document.getElementById('bath-box-4-2');
        const f4shower_2 = document.getElementById('bath-4-2');
        const f4shower_box3 = document.getElementById('bath-box-4-3');
        const f4shower_3 = document.getElementById('bath-4-3');
        const f4shower_box4 = document.getElementById('bath-box-4-4');
        const f4shower_4 = document.getElementById('bath-4-4');
        const f4shower_box5 = document.getElementById('bath-box-4-5');
        const f4shower_5 = document.getElementById('bath-4-5');
        const f4shower_box6 = document.getElementById('bath-box-4-6');
        const f4shower_6 = document.getElementById('bath-4-6');

        const f4disabled_box1 = document.getElementById('dis-box-4-1');
        const f4disabled_1 = document.getElementById('disabled-4-1');
        const f4dryerMachine_box1 = document.getElementById('dry-box-4-1');
        const f4dryerMachine_1 = document.getElementById('dryerMachine-4-1');

        const f4wc_1 = document.getElementById('wc-4-1');
        const f4wc_2 = document.getElementById('wc-4-2');
        const f4wc_3 = document.getElementById('wc-4-3');


        console.log("start to fetch data");
        fetch('http://127.0.0.1:8000/dorm/getJsondata4')
            .then((response) => {
                console.log("response.json()", response);
                return response.json();
            })
            .then((data) => {
                //這部分不太確定哪個欄位從哪裡讀資料
                f4dryerMachine_1_usage = data[0]["fields"]['facilities_useage'];
                f4washingMachine_box1_usage = data[1]["fields"]['facilities_useage'];
                f4washingMachine_box2_usage = data[2]["fields"]['facilities_useage'];
                f4disabled_1_usage = data[3]["fields"]['facilities_useage'];
                f4wc_1_usage = data[4]["fields"]['facilities_useage'];
                f4wc_2_usage = data[5]["fields"]['facilities_useage'];
                f4wc_3_usage = data[6]["fields"]['facilities_useage'];
                f4shower_1_usage = data[7]["fields"]['facilities_useage'];
                f4shower_2_usage = data[8]["fields"]['facilities_useage'];
                f4shower_3_usage = data[9]["fields"]['facilities_useage'];
                f4shower_4_usage = data[10]["fields"]['facilities_useage'];
                f4shower_5_usage = data[11]["fields"]['facilities_useage'];
                f4shower_6_usage = data[12]["fields"]['facilities_useage'];

                // console.log("washingMachine_1_usage", washingMachine_1_usage);
                // console.log(shower_1_usage);
                // console.log(disabled_1_usage);
                // console.log(dryerMachine_1_usage);

                //下面的顏色動畫確定可以
                if (parseInt(f4washingMachine_box1_usage) > 0) {
                    f4washingMachine_box1.style.background = 'yellow';
                    f4washingMachine_1.style.fill = '#4071F5';
                } else {
                    f4washingMachine_1.style.fill = '#faf4f4';
                    f4washingMachine_box1.style.background = '#609755';
                }

                if (parseInt(f4washingMachine_box2_usage) > 0) {
                    f4washingMachine_box2.style.background = 'yellow';
                    f4washingMachine_2.style.fill = '#4071F5';
                } else {
                    f4washingMachine_2.style.fill = '#faf4f4';
                    f4washingMachine_box2.style.background = '#609755';
                }

                if (parseInt(f4shower_1_usage) > 0) {
                    f4shower_1.style.opacity = 1;
                    f4shower_box1.style.background = 'yellow';
                } else {
                    f4shower_1.style.opacity = 0.1;
                    f4shower_box1.style.background = '#609755';
                }

                if (parseInt(f4shower_2_usage) > 0) {
                    f4shower_2.style.opacity = 1;
                    f4shower_box2.style.background = 'yellow';
                } else {
                    f4shower_2.style.opacity = 0.1;
                    f4shower_box2.style.background = '#609755';
                }

                if (parseInt(f4shower_3_usage) > 0) {
                    f4shower_3.style.opacity = 1;
                    f4shower_box3.style.background = 'yellow';
                } else {
                    f4shower_3.style.opacity = 0.1;
                    f4shower_box3.style.background = '#609755';
                }
                if (parseInt(f4shower_4_usage) > 0) {
                    f4shower_4.style.opacity = 1;
                    f4shower_box4.style.background = 'yellow';
                } else {
                    f4shower_4.style.opacity = 0.1;
                    f4shower_box4.style.background = '#609755';
                }
                if (parseInt(f4shower_5_usage) > 0) {
                    f4shower_5.style.opacity = 1;
                    f4shower_box5.style.background = 'yellow';
                } else {
                    f4shower_5.style.opacity = 0.1;
                    f4shower_box5.style.background = '#609755';
                }
                if (parseInt(f4shower_6_usage) > 0) {
                    f4shower_6.style.opacity = 1;
                    f4shower_box6.style.background = 'yellow';
                } else {
                    f4shower_6.style.opacity = 0.1;
                    f4shower_box6.style.background = '#609755';
                }
                if (parseInt(f4disabled_1_usage) > 0) {
                    f4disabled_1.style.opacity = 1;
                    f4disabled_box1.style.background = 'yellow';
                } else {
                    f4disabled_1.style.opacity = 0.1;
                    f4disabled_box1.style.background = '#609755';
                }

                if (parseInt(f4dryerMachine_1_usage) > 0) {
                    f4dryerMachine_1.style.animation = 'dash 1.4s linear infinite';
                    f4dryerMachine_box1.style.background = 'yellow';
                } else {
                    f4dryerMachine_box1.style.background = '#609755';
                }

                if (parseInt(f4wc_1_usage) > 0) {
                    f4wc_1.style.opacity = 0.8;
                } else {
                    f4wc_1.style.opacity = 0.1;
                }
                if (parseInt(f4wc_2_usage) > 0) {
                    f4wc_2.style.opacity = 0.8;
                } else {
                    f4wc_2.style.opacity = 0.1;
                }
                if (parseInt(f4wc_3_usage) > 0) {
                    f4wc_3.style.opacity = 0.8;
                } else {
                    f4wc_3.style.opacity = 0.1;
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