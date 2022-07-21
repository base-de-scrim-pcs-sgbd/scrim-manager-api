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