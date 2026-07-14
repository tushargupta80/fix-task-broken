There is an Apache-style access log at /app/access.log. Parse it and write a
summary report to /app/report.json as a JSON object with exactly these keys:

- total_requests: integer, the total number of log lines/requests.
- unique_ips: integer, the number of distinct client IP addresses.
- top_path: string, the request path (e.g. "/index.html") that appears most
  often across all requests.

Success criteria:
1. /app/report.json exists and contains valid JSON.
2. total_requests and unique_ips are correct integer counts.
3. top_path is the correct most-frequently-requested path.