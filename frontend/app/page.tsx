import { UserButton, SignedIn, SignedOut, SignInButton } from '@clerk/nextjs'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'

export default function Home() {
  return (
    <div className="container mx-auto p-8 min-h-screen flex flex-col items-center justify-center bg-gray-50">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle className="text-4xl font-bold text-center text-blue-600">
            MPFGuard HK 已上線
          </CardTitle>
          <CardDescription className="text-center text-lg">
            自動 MPF 計算 + OCR payroll，合規零錯漏
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-6 pt-6">
          <SignedIn>
            <Button className="w-full text-lg py-6" asChild>
              <a href="/dashboard">前往 Dashboard</a>
            </Button>
            <div className="flex justify-center">
              <UserButton afterSignOutUrl="/" />
            </div>
          </SignedIn>
          <SignedOut>
            <SignInButton mode="redirect" redirectUrl="/dashboard">
              <Button className="w-full text-lg py-6">前往登入</Button>
            </SignInButton>
          </SignedOut>
        </CardContent>
      </Card>
    </div>
  )
}
