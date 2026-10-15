import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({
    service: "simulator",
    specVersion: "1",
    studentToken: process.env.SITE_TOKEN,
  });
}
