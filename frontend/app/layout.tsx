import type { Metadata } from "next"
import { Inter } from "next/font/google"
import { ClerkProvider } from '@clerk/nextjs'
import './globals.css'
import { QueryProvider } from '@/lib/query'

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "MPFGuard HK - SME MPF Automation",
  description: "自動 MPF 計算 + OCR payroll, 合規零錯漏",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <ClerkProvider>
      <html lang="zh-TW">
        <body className={inter.className}>
          <QueryProvider>
            {children}
          </QueryProvider>
        </body>
      </html>
    </ClerkProvider>
  )
}