#Requires -Version 5.1
<#
.SYNOPSIS
    Link this directory's definitions into the user's global Claude directory.

.DESCRIPTION
    The PowerShell counterpart to install.sh, for Windows shells where that script
    cannot run. Same contract: same flags, same output lines, same exit codes.

    `global/` mirrors the layout of ~/.claude, so global/agents/ lands in
    ~/.claude/agents. These are standalone definitions, not plugins: `claude --agent
    <name>` and @-mention resolve names from that directory, which is outside any
    repository. Linking rather than copying keeps this checkout the single source of
    truth — an edit here is live in the next session, with no reinstall step.

    Creating a symlink on Windows needs Developer Mode enabled or an elevated shell,
    and under Windows PowerShell 5.1 only elevation works — prefer PowerShell 7.
    The script does not fall back to copying: a copy would be a second source of
    truth that silently goes stale.
#>
[CmdletBinding()]
param(
    [switch]$Uninstall,
    [switch]$Force,
    [switch]$DryRun,
    [switch]$Help,
    # install.sh's long options, so a command copied from the docs still works here.
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Rest
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Write-Err([string]$Message) {
    [Console]::Error.WriteLine($Message)
}

function Show-Usage {
    @'
usage: install.ps1 [-Uninstall] [-Force] [-DryRun]

  -Uninstall  remove links this script created (leaves anything else alone)
  -Force      replace a destination that is not our link; a regular file is
              moved aside to <name>.bak-<timestamp> rather than deleted
  -DryRun     print what would happen and change nothing

Links global/agents/*.md into ~/.claude/agents; override the destination
with CLAUDE_AGENTS_DIR. install.sh's --uninstall / --force / --dry-run spellings
are accepted too.
'@
}

foreach ($arg in $Rest) {
    switch ($arg) {
        '--uninstall' { $Uninstall = $true }
        '--force' { $Force = $true }
        '--dry-run' { $DryRun = $true }
        '--help' { $Help = $true }
        '-h' { $Help = $true }
        default {
            Write-Err "install.ps1: unknown option $arg`n"
            Write-Err (Show-Usage)
            exit 2
        }
    }
}

if ($Help) {
    Show-Usage
    exit 0
}

$srcDir = Join-Path $PSScriptRoot 'agents'
$destDir = if ($env:CLAUDE_AGENTS_DIR) { $env:CLAUDE_AGENTS_DIR } else { Join-Path $HOME '.claude/agents' }

# A symlink target may be stored relative to the link, so resolve it the way the
# filesystem would before comparing it with the file we are about to link.
function Resolve-LinkTarget([string]$Target, [string]$LinkPath) {
    if ([string]::IsNullOrEmpty($Target)) { return $null }
    if ([System.IO.Path]::IsPathRooted($Target)) { return [System.IO.Path]::GetFullPath($Target) }
    return [System.IO.Path]::GetFullPath((Join-Path (Split-Path -Parent $LinkPath) $Target))
}

function Test-SamePath([string]$A, [string]$B) {
    if ([string]::IsNullOrEmpty($A) -or [string]::IsNullOrEmpty($B)) { return $false }
    $normalize = { param($p) [System.IO.Path]::GetFullPath($p).TrimEnd('\', '/') }
    return [string]::Equals((& $normalize $A), (& $normalize $B), 'OrdinalIgnoreCase')
}

function Invoke-Step([string]$Description, [scriptblock]$Action) {
    if ($DryRun) {
        "  would: $Description"
        return
    }
    & $Action
}

if (-not (Test-Path -LiteralPath $srcDir)) {
    Write-Err "install.ps1: no agents directory at $srcDir"
    exit 1
}

if (-not $DryRun -and -not $Uninstall) {
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
}

$status = 0
$found = 0

foreach ($src in @(Get-ChildItem -LiteralPath $srcDir -Filter *.md -File | Sort-Object Name)) {
    # An agent definition is a file with a `name:` in its YAML frontmatter. Anything
    # else here is documentation, and linking it would put a non-agent in the roster.
    $lines = @(Get-Content -LiteralPath $src.FullName)
    if ($lines.Count -eq 0 -or $lines[0].TrimEnd() -ne '---') { continue }
    $hasName = $false
    for ($i = 1; $i -lt $lines.Count; $i++) {
        if ($lines[$i].TrimEnd() -eq '---') { break }
        if ($lines[$i] -match '^name:') { $hasName = $true; break }
    }
    if (-not $hasName) { continue }

    $found++
    $dest = Join-Path $destDir $src.Name

    # -Force so a hidden or broken link is still seen: a link to a deleted target is
    # still ours to manage.
    $item = Get-Item -LiteralPath $dest -Force -ErrorAction SilentlyContinue
    $exists = $null -ne $item
    $isLink = $exists -and $item.LinkType -eq 'SymbolicLink'
    $target = if ($isLink) { Resolve-LinkTarget (@($item.Target)[0]) $dest } else { $null }
    $ours = $isLink -and (Test-SamePath $target $src.FullName)

    if ($Uninstall) {
        if ($ours) {
            Invoke-Step "remove $dest" { Remove-Item -LiteralPath $dest -Force }
            "unlinked  $dest"
        }
        elseif ($exists) {
            "skipped   $dest (not a link this script made)"
        }
        continue
    }

    if ($ours) {
        "ok        $dest"
        continue
    }

    if ($isLink) {
        if ($Force) {
            Invoke-Step "remove $dest" { Remove-Item -LiteralPath $dest -Force }
        }
        else {
            Write-Err "CONFLICT  $dest -> $target (use -Force to replace)"
            $status = 1
            continue
        }
    }
    elseif ($exists) {
        if ($Force) {
            $backup = "$dest.bak-$(Get-Date -Format 'yyyyMMddHHmmss')"
            Invoke-Step "move $dest -> $backup" { Move-Item -LiteralPath $dest -Destination $backup }
            "moved     $dest -> $backup"
        }
        else {
            Write-Err "CONFLICT  $dest exists and is not a link (use -Force)"
            $status = 1
            continue
        }
    }

    $srcPath = $src.FullName
    try {
        Invoke-Step "link $dest -> $srcPath" {
            New-Item -ItemType SymbolicLink -Path $dest -Target $srcPath -ErrorAction Stop | Out-Null
        }
    }
    catch {
        # Every remaining link would fail the same way, so say why once and stop.
        Write-Err "install.ps1: could not create $dest"
        Write-Err "  $($_.Exception.Message)"
        if ($PSVersionTable.PSVersion.Major -lt 6) {
            # Windows PowerShell's New-Item does not pass the unprivileged-create flag,
            # so Developer Mode does not help it; PowerShell 7's does.
            Write-Err '  Windows PowerShell 5.1 cannot create a symlink without elevation, even'
            Write-Err '  with Developer Mode on. Run this under PowerShell 7 (pwsh), or in a'
            Write-Err '  shell running as Administrator.'
        }
        else {
            Write-Err '  Creating a symlink on Windows requires Developer Mode (Settings >'
            Write-Err '  System > For developers) or a shell running as Administrator.'
        }
        exit 1
    }
    "linked    $dest -> $srcPath"
}

if ($found -eq 0) {
    Write-Err "install.ps1: no agent definitions in $srcDir"
    exit 1
}

exit $status
