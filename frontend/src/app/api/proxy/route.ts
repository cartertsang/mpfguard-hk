import { NextRequest, NextResponse } from 'next/server';

const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://172.20.123.59:8001';

export async function GET(req: NextRequest) {
  const url = `${backendUrl}${req.nextUrl.pathname}${req.nextUrl.search}`;
  const resp = await fetch(url, {
    headers: {
      'X-API-Key': 'mpfguard_demo_api_key_very_secure_random_20260425_XYZabc1234567890',
      ...Object.fromEntries(req.headers.entries())
    }
  });
  const data = await resp.json();
  return NextResponse.json(data, { status: resp.status });
}

export async function POST(req: NextRequest) {
  const url = `${backendUrl}${req.nextUrl.pathname}${req.nextUrl.search}`;
  const body = await req.json();
  const resp = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': 'mpfguard_demo_api_key_very_secure_random_20260425_XYZabc1234567890'
    },
    body: JSON.stringify(body)
  });
  const data = await resp.json();
  return NextResponse.json(data, { status: resp.status });
}