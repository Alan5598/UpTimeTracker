import assert from "node:assert/strict";
import test from "node:test";
import { buildApp } from "./app.js";

test("health endpoints report the service status", async (t) => {
  const app = buildApp();
  t.after(() => app.close());

  for (const endpoint of ["/health/live", "/health/ready"]) {
    const response = await app.inject({ method: "GET", url: endpoint });

    assert.equal(response.statusCode, 200);
    assert.deepEqual(response.json(), { status: "ok" });
  }
});
