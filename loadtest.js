import http from 'k6/http';
import { check } from 'k6';

export const options = {
  stages: [
    { duration: '5s', target: 2 },
    { duration: '30s', target: 2 }, // Hold at peak
    { duration: '5s', target: 0 },   // Ramp down
  ],
};

const payload = JSON.stringify(
  "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief"
);

export default function () {
  const res = http.post('http://127.0.0.1:8000/', payload, {
    headers: { 'Content-Type': 'application/json' },
  });

  check(res, {
    'status is 200': (r) => r.status === 200,
  });
}