import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10, // virtual users
  duration: '3m', // test duration
};

const BASE_URL = 'http://localhost:8000/v1';
const API_KEY = 'fake-key';

export default function () {
  const payload = JSON.stringify({
    model: "qwen-0.5b",
    response_format: { type: "json_object" },
    messages: [
      {
        role: "system",
        content: "You are a helpful assistant that outputs JSON.",
      },
      {
        role: "user",
        content: "List three colors in JSON format",
      }
    ],
    stream: false // k6 doesn't support streamed responses
  });

  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${API_KEY}`,
    },
  };

  const res = http.post(`${BASE_URL}/chat/completions`, payload, params);

  check(res, {
    'status is 200': (r) => r.status === 200,
    'response contains colors': (r) => r.body.includes("colors"),
  });

  //sleep(1);
}
