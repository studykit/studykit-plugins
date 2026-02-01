# Creating a ThreadInfo object

## Description

Demonstrates the use of a ThreadInfo object.

## Code Samples

* [VBA](#VBA)

```
Sub test_threadinfo()
    Dim oApp As Application
    Set oApp = ThisApplication

    Dim oGeneralOptions As GeneralOptions
    Set oGeneralOptions = oApp.GeneralOptions

    Dim oThreadTable As ThreadTableQuery
    Set oThreadTable = oGeneralOptions.ThreadTableQuery

    Dim oTypes() As String
    oTypes = oThreadTable.GetAvailableThreadTypes

    Dim oSizes() As String
    oSizes = oThreadTable.GetAvailableThreadSizes(False, "NPT")

    Dim oDesignations() As String
    oDesignations = oThreadTable.GetAvailableDesignations(False, "NPT", oSizes(1))

    Dim oThreadInfo As TaperedThreadInfo
    Set oThreadInfo = oThreadTable.CreateThreadInfo(False, True, "NPT", oDesignations(0))
End Sub
```
