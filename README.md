# SupplyGuard API

[![SupplyGuard CI](https://github.com/gaddah-yousef/SupplyGuard/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/gaddah-yousef/SupplyGuard/actions/workflows/ci.yml)

FastAPI demo project for practising a secure DevSecOps workflow.

## Features

- FastAPI REST API and Pytest tests
- Docker container running as a non-root user
- Docker Compose health check
- GitHub Actions tests and Docker image build
- Trivy vulnerability scan for HIGH and CRITICAL findings
- CycloneDX SBOM generation and archiving
- Image publication to GitHub Container Registry (GHCR)

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | API health status |
| GET | `/products` | List products |
| GET | `/products/{product_id}` | Get a product by ID |

Interactive API documentation: `http://localhost:8000/docs`

## Run locally with Docker Compose

```bash
docker compose up -d --build
docker compose ps
curl http://localhost:8000/health
curl http://localhost:8000/products
