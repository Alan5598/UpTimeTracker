# UpTimeTracker API

Starter REST API for the UpTimeTracker platform, built with Node.js, TypeScript, and Fastify.

## Requirements

- Node.js 22 or later
- npm

## Getting started

```sh
npm install
npm run dev
```

The server listens on `http://localhost:3000` by default. Set `PORT` or `HOST` in
your environment to change the address.

## Available endpoints

- `GET /health/live` — process liveness
- `GET /health/ready` — service readiness (no external dependencies are configured yet)

## Scripts

- `npm run dev` — start the API with watch mode
- `npm run build` — compile TypeScript to `dist/`
- `npm start` — run the compiled server
- `npm test` — run the starter health-route test

Authentication and other product features are intentionally not included in this
starter. Use feature branches for subsequent work.
