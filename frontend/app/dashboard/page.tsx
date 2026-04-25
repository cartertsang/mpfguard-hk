import { UserButton, SignedIn, SignedOut, SignInButton } from '@clerk/nextjs'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

export default function Dashboard() {
  return (
    <div className="container mx-auto p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">MPFGuard Dashboard</h1>
        <SignedIn>
          <UserButton afterSignOutUrl="/" />
        </SignedIn>
        <SignedOut>
          <SignInButton mode="modal">
            <Button>登入</Button>
          </SignInButton>
        </SignedOut>
      </div>
      <Card>
        <CardHeader>
          <CardTitle>快速 MPF 計算</CardTitle>
          <CardDescription>輸入 gross_salary 試算 (demo)</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <div>
              <Label> Gross Salary (HKD)</Label>
              <Input id="salary" type="number" placeholder="20000" />
            </div>
            <Button className="w-full">計算 MPF</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}