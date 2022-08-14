function delay(n) {
    return new Promise(function (resolve) {
        setTimeout(resolve, n * 1000);
    });
}

async function myAsyncFunction() {
    while (1) {
        const washingMachine_box1 = document.getElementById('wash-box-1-1');
        const washingMachine_1 = document.getElementById('washingMachine-1-1');
        const washingMachine_box2 = document.getElementById('wash-box-1-2');
        const washingMachine_2 = document.getElementById('washingMachine-1-2');

        const shower_box1 = document.getElementById('bath-box-1-1');
    		const shower_1 = document.getElementById('bath-1-1');
    		const shower_box2 = document.getElementById('bath-box-1-2');
    		const shower_2 = document.getElementById('bath-1-2');
    		const shower_box3 = document.getElementById('bath-box-1-3');
    		const shower_3 = document.getElementById('bath-1-3');
    		const shower_box4 = document.getElementById('bath-box-1-4');
    		const shower_4 = document.getElementById('bath-1-4');
    		const shower_box5 = document.getElementById('bath-box-1-5');
    		const shower_5 = document.getElementById('bath-1-5');

        const disabled_box1 = document.getElementById('dis-box-1-1');
        const disabled_1 = document.getElementById('disabled-1-1');
        const dryerMachine_box1 = document.getElementById('dry-box-1-1');
        const dryerMachine_1 = document.getElementById('dryerMachine-1-1');

        const wc_1 = document.getElementById('wc-1-1');
        const wc_2 = document.getElementById('wc-1-2');
        const wc_3 = document.getElementById('wc-1-3');


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

                console.log("washingMachine_1_usage",washingMachine_1_usage);
                console.log(shower_1_usage);
                console.log(disabled_1_usage);
                console.log(dryerMachine_1_usage);

                //下面的顏色動畫確定可以
            		if (parseInt(washingMachine_box1_usage) > 10) {
            				washingMachine_box1.style.background = 'yellow';
            				washingMachine_1.style.fill = '#4071F5';
            		} else {
            				washingMachine_1.style.fill = '#faf4f1';
            				washingMachine_box1.style.background = '#609755';
            		}

            		if (parseInt(washingMachine_box2_usage) > 10) {
            				washingMachine_box2.style.background = 'yellow';
            				washingMachine_2.style.fill = '#4071F5';
            		} else {
            				washingMachine_2.style.fill = '#faf4f1';
            				washingMachine_box2.style.background = '#609755';
            		}

                if (parseInt(shower_1_usage) > 10) {
            				shower_1.style.opacity = 1;
            				shower_box1.style.background = 'yellow';
            		} else {
            				shower_1.style.opacity = 0.1;
            				shower_box1.style.background = '#609755';
            		}

            		if (parseInt(shower_2_usage) > 10) {
            				shower_2.style.opacity = 1;
            				shower_box2.style.background = 'yellow';
            		} else {
            				shower_2.style.opacity = 0.1;
            				shower_box2.style.background = '#609755';
            		}

            		if (parseInt(shower_3_usage) > 10) {
            				shower_3.style.opacity = 1;
            				shower_box3.style.background = 'yellow';
            		} else {
            				shower_3.style.opacity = 0.1;
            				shower_box3.style.background = '#609755';
            		}
            		if (parseInt(shower_4_usage) > 10) {
            				shower_4.style.opacity = 1;
            				shower_box4.style.background = 'yellow';
            		} else {
            				shower_4.style.opacity = 0.1;
            				shower_box4.style.background = '#609755';
            		}
            		if (parseInt(shower_5_usage) > 10) {
            				shower_5.style.opacity = 1;
            				shower_box5.style.background = 'yellow';
            		} else {
            				shower_5.style.opacity = 0.1;
            				shower_box5.style.background = '#609755';
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

                if (parseInt(wc_1_usage) > 10) {
                    wc_1.style.opacity = 0.8;
                } else {
                    wc_1.style.opacity = 0.1;
                }
                if (parseInt(wc_2_usage) > 10) {
                    wc_2.style.opacity = 0.8;
                } else {
                    wc_2.style.opacity = 0.1;
                }
                if (parseInt(wc_3_usage) > 10) {
                    wc_3.style.opacity = 0.8;
                } else {
                    wc_3.style.opacity = 0.1;
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
