# Run API smoke tests (requires Neo4j).
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..

Write-Host "Checking /health..."
try {
    $health = Invoke-RestMethod -Uri "http://127.0.0.1:8000/health" -TimeoutSec 5
    Write-Host ("  status={0} neo4j={1}" -f $health.status, $health.neo4j)
} catch {
    Write-Host "Server not reachable at http://127.0.0.1:8000"
    Write-Host "Start it with: uv run uvicorn backend.main:app --host 127.0.0.1 --port 8000"
    exit 1
}

Write-Host "Running API integration tests..."
uv run pytest tests/api -v
exit $LASTEXITCODE
