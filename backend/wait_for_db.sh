#!/usr/bin/env bash
set -e

host="$1"
shift
cmd="$@"

echo "Waiting for database ($host) to become available..."
until pg_isready -h "$host" -U "postgres" > /dev/null 2>&1; do
  sleep 2
done

echo "Database is ready. Starting backend..."
exec $cmd