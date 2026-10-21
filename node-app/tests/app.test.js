const request = require('supertest');
const app = require('../src/app');

describe('API', () => {
  test('GET /health', async () => {
    const r = await request(app).get('/health');
    expect(r.status).toBe(200);
    expect(r.body).toEqual({ status: 'ok' });
  });
  test('GET /api/greet', async () => {
    const r = await request(app).get('/api/greet?name=Shubham');
    expect(r.body.message).toBe('Hello, Shubham!');
  });
});
