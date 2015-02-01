import math

let logmillion = math.ln(1_000_000)
var logs : array[0..100, float]

var count = 0
for n in 1..100:
    logs[n] = logs[n-1] + math.ln(float(n))
    for k in 1..n:
        if logs[n] - logs[k] - logs[n-k] >= logmillion:
            count += 1
echo(count)
