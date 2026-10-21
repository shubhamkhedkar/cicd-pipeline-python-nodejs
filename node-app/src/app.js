const express = require('express');

const app = express();

app.get('/health', (req, res) => res.json({ status: 'ok' }));

app.get('/api/greet', (req, res) => {
  const name = req.query.name || 'world';
  res.json({ message: `Hello, ${name}!` });
});

module.exports = app;
