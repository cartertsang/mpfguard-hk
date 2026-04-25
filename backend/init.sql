CREATE EXTENSION IF NOT EXISTS pgcrypto;
-- RLS prep for PDPO multi-tenant
ALTER TABLE companies ENABLE ROW LEVEL SECURITY;
-- Add policies later