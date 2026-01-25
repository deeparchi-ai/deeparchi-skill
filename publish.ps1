# DeepArchi Skill publish script
# Publish skill to GitHub and OpenSkills

Write-Host "=== DeepArchi Skill Publish Script ===" -ForegroundColor Green
Write-Host ""

# Ensure script is run from skill directory
if (-not (Test-Path "README.md")) {
    Write-Host "Error: run this script in the deeparchi skill folder." -ForegroundColor Red
    exit 1
}

# Check Git
try {
    $gitVersion = git --version
    Write-Host "Git found: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "Error: Git not found. Please install Git first." -ForegroundColor Red
    exit 1
}

# Init Git if needed
if (-not (Test-Path ".git")) {
    Write-Host "Initializing Git repository..." -ForegroundColor Yellow
    git init
    Write-Host "Git repository initialized." -ForegroundColor Green
} else {
    Write-Host "Git repository exists." -ForegroundColor Green
}

# Add files
Write-Host "Adding files to Git..." -ForegroundColor Yellow
git add .

# Commit changes if any
$status = git status --porcelain
if ($status) {
    Write-Host "Committing changes..." -ForegroundColor Yellow
    $commitMessage = Read-Host "Commit message (default: Initial commit: DeepArchi Skill v1.0.0)"
    if ([string]::IsNullOrWhiteSpace($commitMessage)) {
        $commitMessage = "Initial commit: DeepArchi Skill v1.0.0"
    }
    git commit -m $commitMessage
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Commit failed." -ForegroundColor Red
        Write-Host "You may need to set git user.name and user.email." -ForegroundColor Yellow
        $setIdentity = Read-Host "Set local git identity now? (y/n)"
        if ($setIdentity -eq "y" -or $setIdentity -eq "Y") {
            $userName = Read-Host "git user.name"
            $userEmail = Read-Host "git user.email"
            if ($userName) { git config user.name $userName }
            if ($userEmail) { git config user.email $userEmail }
            git commit -m $commitMessage
        }
    }
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Changes committed." -ForegroundColor Green
    } else {
        Write-Host "Commit still failed. Fix git identity and retry." -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "No changes to commit." -ForegroundColor Green
}

# Check remote
$remote = $null
try {
    $remoteOutput = git remote get-url origin 2>&1
    if ($LASTEXITCODE -eq 0) {
        $remote = $remoteOutput
        Write-Host "Remote set: $remote" -ForegroundColor Green
    }
} catch {
    # 忽略错误，继续执行
}

if (-not $remote) {
    Write-Host "Configure remote repository..." -ForegroundColor Yellow
    $repoUrl = Read-Host "GitHub repo URL (e.g. https://github.com/username/deeparchi-skill.git)"
    if ($repoUrl) {
        git remote add origin $repoUrl
        $remote = $repoUrl
        Write-Host "Remote configured." -ForegroundColor Green
    } else {
        Write-Host "Skipping remote config. You can add it later." -ForegroundColor Yellow
    }
}

# Create tag
Write-Host ""
$createTag = Read-Host "Create tag v1.0.0? (y/n)"
$shouldCreateTag = $false
if ($createTag -eq "y") { $shouldCreateTag = $true }
if ($createTag -eq "Y") { $shouldCreateTag = $true }

if ($shouldCreateTag) {
    git rev-parse --verify HEAD 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Cannot create tag: no commits found." -ForegroundColor Red
        $shouldCreateTag = $false
    } else {
        git tag -l "v1.0.0" 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0 -and (git tag -l "v1.0.0")) {
            Write-Host "Tag v1.0.0 already exists. Skipping." -ForegroundColor Yellow
        } else {
            git tag -a v1.0.0 -m "DeepArchi Skill v1.0.0 - Initial release"
            if ($LASTEXITCODE -eq 0) {
                Write-Host "Tag v1.0.0 created." -ForegroundColor Green
            } else {
                Write-Host "Tag creation failed." -ForegroundColor Red
                $shouldCreateTag = $false
            }
        }
    }
}

# Push to remote
Write-Host ""
$push = Read-Host "Push to GitHub? (y/n)"
$shouldPush = $false
if ($push -eq "y") {
    $shouldPush = $true
}
if ($push -eq "Y") {
    $shouldPush = $true
}

if ($shouldPush) {
    if (-not $remote) {
        Write-Host "No remote configured. Skipping push." -ForegroundColor Yellow
        $shouldPush = $false
    }
}

if ($shouldPush) {
    $currentBranch = "main"
    try {
        $branchOutput = git rev-parse --abbrev-ref HEAD 2>&1
        if ($LASTEXITCODE -eq 0 -and $branchOutput) {
            $currentBranch = $branchOutput.Trim()
        }
    } catch {
        $currentBranch = "main"
    }

    Write-Host "Pushing to GitHub (branch: $currentBranch)..." -ForegroundColor Yellow
    git push -u origin $currentBranch 2>&1 | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Pushed to GitHub." -ForegroundColor Green
    } else {
        Write-Host "Push failed. Check remote URL and auth." -ForegroundColor Red
    }
    
    if ($shouldCreateTag) {
        git push origin v1.0.0 2>&1 | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Tag pushed." -ForegroundColor Green
        } else {
            Write-Host "Tag push failed." -ForegroundColor Red
        }
    }
}

Write-Host ""
Write-Host "=== Done ===" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Verify the GitHub repo." -ForegroundColor White
Write-Host "2. Install with:" -ForegroundColor White
if ($remote) {
    $repoName = $remote -replace '.*github\.com[:/](.+?)(?:\.git)?$', '$1'
    Write-Host "   npx openskills install $repoName" -ForegroundColor Yellow
} else {
    Write-Host "   npx openskills install YOUR_USERNAME/deeparchi-skill" -ForegroundColor Yellow
}
Write-Host "3. See PUBLISH.md for more info." -ForegroundColor White
