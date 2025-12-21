# Using Inventor's progress bars

## Description

Demonstrates using Inventor's progress bar.

## Code Samples

* [VBA](#VBA)

```
' 64-bit version
Public Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As LongLong)

' 32-bit version
'Public Declare Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As Long)

Public Sub TestDialogProgressBar()
    Dim iStepCount As Long
    iStepCount = 50

    ' Create a new ProgressBar object.
    Dim oProgressBar As ProgressBar
    Set oProgressBar = ThisApplication.CreateProgressBar(False, iStepCount, "Test Progress")

    ' Set the message for the progress bar
    oProgressBar.Message = "Executing some process"

    Dim i As Long
    For i = 1 To iStepCount
        ' Sleep 0.2 sec to simulate some process
        Sleep 200
        oProgressBar.Message = "Executing some process - " & i
        oProgressBar.UpdateProgress
    Next

    ' Terminate the progress bar.
    oProgressBar.Close
End Sub

Public Sub TestStatusBarProgressBar()
    Dim iStepCount As Long
    iStepCount = 50

    ' Create a new ProgressBar object.
    Dim oProgressBar As ProgressBar
    Set oProgressBar = ThisApplication.CreateProgressBar(True, iStepCount, "Test Progress")

    ' Set the message for the progress bar
    oProgressBar.Message = "Executing some process"

    Dim i As Long
    For i = 1 To iStepCount
        ' Sleep 0.2 sec to simulate some process
        Sleep 200
        oProgressBar.Message = "Executing some process - " & i
        oProgressBar.UpdateProgress
    Next

    ' Terminate the progress bar.
    oProgressBar.Close
End Sub
```
