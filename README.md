# calibration
TODO

# plotting
first connect to te device using mpremote
```
mpremote connect a0
```
make a named fifo
```
mkfifo /tmp/pw 
```
start plotting the data
```
mpremote | tee -a /tmp/pw
python3 graph.py
