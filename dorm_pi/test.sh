if ps aux | grep python3 | grep -v grep > /dev/null #ps aux: 觀察系統下所有程序，grep: 可用正則表示，grep -v 選擇沒對應到的Line
#pipe (|) 就是把第一個指令處理的結果直接當成參數給第二個指令當成輸入來處理
then
    echo "yes"
else 
    python3 /home/pi/tx.py > /home/pi/tx.log
fi
