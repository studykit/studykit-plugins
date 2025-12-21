# Display custom error messages

## Description

Demonstrates displaying custom error messages.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Sub DisplayErrorsInInventorDialog()
    ' Set a reference to the ErrorManager object
    Dim oErrorMgr As ErrorManager
    Set oErrorMgr = ThisApplication.ErrorManager

    ' Start a message section
    Dim oMsgSection1 As MessageSection
    Set oMsgSection1 = oErrorMgr.StartMessageSection

    ' Start another (nested) message section
    Dim oMsgSection2 As MessageSection
    Set oMsgSection2 = oErrorMgr.StartMessageSection

    ' Add a message
    Call oErrorMgr.AddMessage("My third level error", True)

    ' Adopt the above message under a new message
    Call oMsgSection2.AdoptMessages("My second level error", True)

    ' Adopt the above messages under the top level message
    Call oMsgSection1.AdoptMessages("My first level error", True)

    ' Show the error dialog
    Call oErrorMgr.Show("My errors", False, False)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |