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