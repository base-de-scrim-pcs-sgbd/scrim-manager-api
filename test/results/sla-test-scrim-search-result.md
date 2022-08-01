# TEST #1

```
          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: test/sla-test-scrim-search.js
     output: -

  scenarios: (100.00%) 1 scenario, 2 max VUs, 40s max duration (incl. graceful stop):
           * default: 2 looping VUs for 10s (gracefulStop: 30s)


running (11.2s), 0/2 VUs, 18 complete and 0 interrupted iterations
default ✓ [======================================] 2 VUs  10s

     data_received..................: 15 kB 1.4 kB/s
     data_sent......................: 18 kB 1.6 kB/s
     http_req_blocked...............: avg=51.59ms  min=0s       med=0s       max=465.16ms p(90)=139.05ms p(95)=463.75ms
     http_req_connecting............: avg=15.87ms  min=0s       med=0s       max=143.76ms p(90)=42.58ms  p(95)=142.21ms
     http_req_duration..............: avg=182.94ms min=169.55ms med=176.91ms max=222.86ms p(90)=199.25ms p(95)=203.57ms
     http_req_receiving.............: avg=0s       min=0s       med=0s       max=0s       p(90)=0s       p(95)=0s
     http_req_sending...............: avg=0s       min=0s       med=0s       max=0s       p(90)=0s       p(95)=0s
     http_req_tls_handshaking.......: avg=32.23ms  min=0s       med=0s       max=290.17ms p(90)=87.03ms  p(95)=290.12ms
     http_req_waiting...............: avg=182.94ms min=169.55ms med=176.91ms max=222.86ms p(90)=199.25ms p(95)=203.57ms
     http_reqs......................: 18    1.614316/s
     iteration_duration.............: avg=1.23s    min=1.17s    med=1.17s    max=1.69s    p(90)=1.33s    p(95)=1.66s
     iterations.....................: 18    1.614316/s
     vus_max........................: 2     min=2      max=2
```

# TEST #2
```
          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: test/sla-test-scrim-search.js
     output: -

  scenarios: (100.00%) 1 scenario, 257 max VUs, 40s max duration (incl. graceful stop):
           * default: 257 looping VUs for 10s (gracefulStop: 30s)


running (13.0s), 000/257 VUs, 885 complete and 0 interrupted iterations
default ✓ [======================================] 257 VUs  10s

     data_received..................: 1.6 MB 124 kB/s
     data_sent......................: 955 kB 73 kB/s
     http_req_blocked...............: avg=597.49ms min=0s       med=0s    max=3.67s    p(90)=3.56s    p(95)=3.62s
     http_req_connecting............: avg=485.66ms min=0s       med=0s    max=3.27s    p(90)=3.17s    p(95)=3.22s
     http_req_duration..............: avg=1.73s    min=162.93ms med=1.94s max=3.03s    p(90)=2.68s    p(95)=2.94s
       { expected_response:true }...: avg=1.73s    min=162.93ms med=1.94s max=3.03s    p(90)=2.68s    p(95)=2.94s
     http_req_failed................: 0.00%  ✓ 0         ✗ 885
     http_req_receiving.............: avg=106.44µs min=0s       med=0s    max=1.09ms   p(90)=512.22µs p(95)=867.83µs
     http_req_sending...............: avg=19.63µs  min=0s       med=0s    max=1.06ms   p(90)=0s       p(95)=65.27µs
     http_req_tls_handshaking.......: avg=84.53ms  min=0s       med=0s    max=326.18ms p(90)=294.02ms p(95)=301.12ms
     http_req_waiting...............: avg=1.73s    min=162.3ms  med=1.94s max=3.03s    p(90)=2.68s    p(95)=2.94s
     http_reqs......................: 885    67.918302/s
     iteration_duration.............: avg=3.33s    min=1.53s    med=2.96s max=7.66s    p(90)=6.52s    p(95)=7.11s
     iterations.....................: 885    67.918302/s
     vus............................: 8      min=8       max=257
     vus_max........................: 257    min=257     max=257
```

# Test #3

```
          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: test/sla-test-scrim-search.js
     output: -

  scenarios: (100.00%) 1 scenario, 255 max VUs, 40s max duration (incl. graceful stop):
           * default: 255 looping VUs for 10s (gracefulStop: 30s)


running (12.8s), 000/255 VUs, 874 complete and 0 interrupted iterations
default ✓ [======================================] 255 VUs  10s

     data_received..................: 1.6 MB 124 kB/s
     data_sent......................: 944 kB 74 kB/s
     http_req_blocked...............: avg=597.63ms min=0s       med=0s    max=3.69s    p(90)=3.55s    p(95)=3.61s
     http_req_connecting............: avg=488.4ms  min=0s       med=0s    max=3.31s    p(90)=3.18s    p(95)=3.24s
     http_req_duration..............: avg=1.73s    min=165.1ms  med=1.88s max=3.36s    p(90)=2.09s    p(95)=2.22s
       { expected_response:true }...: avg=1.73s    min=165.1ms  med=1.88s max=3.36s    p(90)=2.09s    p(95)=2.22s
     http_req_failed................: 0.00%  ✓ 0         ✗ 874
     http_req_receiving.............: avg=72.42µs  min=0s       med=0s    max=1.01ms   p(90)=167.44µs p(95)=813.01µs
     http_req_sending...............: avg=29.36µs  min=0s       med=0s    max=1.02ms   p(90)=3.5µs    p(95)=83.19µs
     http_req_tls_handshaking.......: avg=84.68ms  min=0s       med=0s    max=318.35ms p(90)=293.8ms  p(95)=299.21ms
     http_req_waiting...............: avg=1.73s    min=164.89ms med=1.88s max=3.36s    p(90)=2.09s    p(95)=2.22s
     http_reqs......................: 874    68.026667/s
     iteration_duration.............: avg=3.33s    min=1.74s    med=2.91s max=7.1s     p(90)=6.02s    p(95)=6.52s
     iterations.....................: 874    68.026667/s
     vus............................: 90     min=90      max=255
     vus_max........................: 255    min=255     max=255
```
# Test 4
```
          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: test/sla-test-scrim-search.js
     output: -

  scenarios: (100.00%) 1 scenario, 100 max VUs, 40s max duration (incl. graceful stop):
           * default: 100 looping VUs for 10s (gracefulStop: 30s)


running (12.5s), 000/100 VUs, 636 complete and 0 interrupted iterations
default ✓ [======================================] 100 VUs  10s

     data_received..................: 698 kB 56 kB/s
     data_sent......................: 650 kB 52 kB/s
     http_req_blocked...............: avg=79.04ms  min=0s    med=0s       max=561.66ms p(90)=487.37ms p(95)=519.35ms
     http_req_connecting............: avg=29.29ms  min=0s    med=0s       max=243.04ms p(90)=170.41ms p(95)=205.2ms
     http_req_duration..............: avg=594.78ms min=150ms med=349.17ms max=2.31s    p(90)=1.49s    p(95)=1.51s
       { expected_response:true }...: avg=594.78ms min=150ms med=349.17ms max=2.31s    p(90)=1.49s    p(95)=1.51s
     http_req_failed................: 0.00%  ✓ 0         ✗ 636
     http_req_receiving.............: avg=51.97µs  min=0s    med=0s       max=1.02ms   p(90)=0s       p(95)=505.82µs
     http_req_sending...............: avg=14.31µs  min=0s    med=0s       max=959.09µs p(90)=0s       p(95)=59.95µs
     http_req_tls_handshaking.......: avg=44.65ms  min=0s    med=0s       max=300.04ms p(90)=279.16ms p(95)=288.12ms
     http_req_waiting...............: avg=594.71ms min=150ms med=349.17ms max=2.31s    p(90)=1.49s    p(95)=1.51s
     http_reqs......................: 636    50.885172/s
     iteration_duration.............: avg=1.67s    min=1.15s med=1.36s    max=3.31s    p(90)=2.58s    p(95)=2.9s
     iterations.....................: 636    50.885172/s
     vus............................: 1      min=1       max=100
     vus_max........................: 100    min=100     max=100
```