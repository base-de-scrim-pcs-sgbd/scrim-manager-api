# Test 1
```
          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: test/sla-test-team-register.js
     output: -

  scenarios: (100.00%) 1 scenario, 2 max VUs, 40s max duration (incl. graceful stop):
           * default: 2 looping VUs for 10s (gracefulStop: 30s)


running (11.0s), 0/2 VUs, 18 complete and 0 interrupted iterations
default ✓ [======================================] 2 VUs  10s

     data_received..................: 15 kB 1.4 kB/s
     data_sent......................: 11 kB 1.0 kB/s
     http_req_blocked...............: avg=50ms     min=0s       med=0s       max=456.85ms p(90)=132.98ms p(95)=445.31ms
     http_req_connecting............: avg=15.59ms  min=0s       med=0s       max=144.22ms p(90)=40.94ms  p(95)=137.64ms
     http_req_duration..............: avg=164.7ms  min=154.75ms med=164.69ms max=180.81ms p(90)=174.36ms p(95)=177.47ms
       { expected_response:true }...: avg=164.7ms  min=154.75ms med=164.69ms max=180.81ms p(90)=174.36ms p(95)=177.47ms
     http_req_failed................: 0.00% ✓ 0       ✗ 18
     http_req_receiving.............: avg=17.02µs  min=0s       med=0s       max=168.9µs  p(90)=41.28µs  p(95)=142.29µs
     http_req_sending...............: avg=53.66µs  min=0s       med=0s       max=894.5µs  p(90)=21.45µs  p(95)=194.94µs
     http_req_tls_handshaking.......: avg=31.74ms  min=0s       med=0s       max=289.06ms p(90)=84.72ms  p(95)=283.4ms
     http_req_waiting...............: avg=164.63ms min=154.75ms med=164.69ms max=180.81ms p(90)=174.34ms p(95)=177.41ms
     http_reqs......................: 18    1.63807/s
     iteration_duration.............: avg=1.21s    min=1.15s    med=1.16s    max=1.63s    p(90)=1.31s    p(95)=1.61s
     iterations.....................: 18    1.63807/s
     vus............................: 2     min=2     max=2
     vus_max........................: 2     min=2     max=2
```

# Test 2
```
          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: test/sla-test-team-register.js
     output: -

  scenarios: (100.00%) 1 scenario, 100 max VUs, 40s max duration (incl. graceful stop):
           * default: 100 looping VUs for 10s (gracefulStop: 30s)


running (11.2s), 000/100 VUs, 765 complete and 0 interrupted iterations
default ✓ [======================================] 100 VUs  10s

     data_received..................: 721 kB 65 kB/s
     data_sent......................: 474 kB 43 kB/s
     http_req_blocked...............: avg=58.31ms  min=0s       med=0s       max=481.32ms p(90)=437.1ms  p(95)=449.78ms
     http_req_connecting............: avg=19.79ms  min=0s       med=0s       max=168.36ms p(90)=145.69ms p(95)=153.25ms
     http_req_duration..............: avg=324.75ms min=147.75ms med=185.73ms max=2.18s    p(90)=597.96ms p(95)=999.49ms
       { expected_response:true }...: avg=324.75ms min=147.75ms med=185.73ms max=2.18s    p(90)=597.96ms p(95)=999.49ms
     http_req_failed................: 0.00%  ✓ 0         ✗ 765
     http_req_receiving.............: avg=58.89µs  min=0s       med=0s       max=11.11ms  p(90)=0s       p(95)=306.63µs
     http_req_sending...............: avg=17.37µs  min=0s       med=0s       max=790.7µs  p(90)=0s       p(95)=66.17µs
     http_req_tls_handshaking.......: avg=37.54ms  min=0s       med=0s       max=309.07ms p(90)=280.74ms p(95)=287.3ms
     http_req_waiting...............: avg=324.67ms min=147.75ms med=185.67ms max=2.18s    p(90)=597.62ms p(95)=999.49ms
     http_reqs......................: 765    68.562906/s
     iteration_duration.............: avg=1.38s    min=1.14s    med=1.18s    max=3.18s    p(90)=1.92s    p(95)=2.44s
     iterations.....................: 765    68.562906/s
     vus............................: 23     min=23      max=100
     vus_max........................: 100    min=100     max=100
```

# Test 3

```
          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: test/sla-test-team-register.js
     output: -

  scenarios: (100.00%) 1 scenario, 255 max VUs, 40s max duration (incl. graceful stop):
           * default: 255 looping VUs for 10s (gracefulStop: 30s)


running (13.2s), 000/255 VUs, 1038 complete and 0 interrupted iterations
default ✓ [======================================] 255 VUs  10s

     data_received..................: 1.6 MB 123 kB/s
     data_sent......................: 694 kB 53 kB/s
     http_req_blocked...............: avg=449.52ms min=0s       med=0s    max=3.56s    p(90)=3.47s    p(95)=3.52s
     http_req_connecting............: avg=361.48ms min=0s       med=0s    max=3.2s     p(90)=3.14s    p(95)=3.16s
     http_req_duration..............: avg=1.35s    min=150.47ms med=1.63s max=3.56s    p(90)=1.78s    p(95)=1.93s
       { expected_response:true }...: avg=1.35s    min=150.47ms med=1.63s max=3.56s    p(90)=1.78s    p(95)=1.93s
     http_req_failed................: 0.00%  ✓ 0         ✗ 1038
     http_req_receiving.............: avg=66.4µs   min=0s       med=0s    max=1.58ms   p(90)=86.25µs  p(95)=739.18µs
     http_req_sending...............: avg=22.2µs   min=0s       med=0s    max=998.5µs  p(90)=0s       p(95)=81.19µs
     http_req_tls_handshaking.......: avg=71.35ms  min=0s       med=0s    max=312.83ms p(90)=291.41ms p(95)=298.25ms
     http_req_waiting...............: avg=1.35s    min=150.47ms med=1.63s max=3.56s    p(90)=1.78s    p(95)=1.93s
     http_reqs......................: 1038   78.547842/s
     iteration_duration.............: avg=2.81s    min=1.32s    med=2.7s  max=6.28s    p(90)=5.08s    p(95)=5.74s
     iterations.....................: 1038   78.547842/s
     vus............................: 18     min=18      max=255
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
     script: test/sla-test-team-register.js
     output: -

  scenarios: (100.00%) 1 scenario, 257 max VUs, 40s max duration (incl. graceful stop):
           * default: 257 looping VUs for 10s (gracefulStop: 30s)


running (12.8s), 000/257 VUs, 1024 complete and 0 interrupted iterations
default ✓ [======================================] 257 VUs  10s

     data_received..................: 1.6 MB 128 kB/s
     http_req_blocked...............: avg=345.07ms min=0s      med=0s    max=3.5s    p(90)=502.64ms p(95)=3.46s
     http_req_connecting............: avg=266.4ms  min=0s      med=0s    max=3.18s   p(90)=185.16ms p(95)=3.15s
     http_req_duration..............: avg=1.5s     min=164.2ms med=1.64s max=2.32s   p(90)=1.8s     p(95)=1.85s
       { expected_response:true }...: avg=1.5s     min=164.2ms med=1.64s max=2.32s   p(90)=1.8s     p(95)=1.85s
     http_req_failed................: 0.00%  ✓ 0         ✗ 1024
     http_req_receiving.............: avg=49.86µs  min=0s      med=0s    max=1.02ms  p(90)=0s       p(95)=547.09µs
     http_req_sending...............: avg=28.53µs  min=0s      med=0s    max=1ms     p(90)=42.97µs  p(95)=186.74µs
     http_req_tls_handshaking.......: avg=72.58ms  min=0s      med=0s    max=306.3ms p(90)=290.69ms p(95)=297.17ms
     http_req_waiting...............: avg=1.5s     min=164.2ms med=1.64s max=2.32s   p(90)=1.8s     p(95)=1.85s
     http_reqs......................: 1024   80.168565/s
     iteration_duration.............: avg=2.85s    min=1.57s   med=2.71s max=6.22s   p(90)=3.57s    p(95)=5.59s
     iterations.....................: 1024   80.168565/s
     vus............................: 80     min=80      max=257
     vus_max........................: 257    min=257     max=257
```