# Prompt message creation sample

## Description

This sample demonstrates how to creat a custom prompt message.

## Code Samples

* [VBA](#VBA)

This sample demonstrates how to creat a custom prompt message.

|  |
| --- |
| Copy Code |

```
Sub PromptMessageSample()
    Dim oPO As PromptsOptions
    Set oPO = ThisApplication.PromptsOptions

    Dim oPMs As PromptMessages
    Set oPMs = oPO.PromptMessages

    Dim oPM As PromptMessage

    On Error Resume Next
    Set oPM = oPMs.Item("User_defined_prompt")

    If Err Then
        Set oPM = oPMs.Add("User_defined_prompt", "This is not allowed", vbOKCancel, vbCritical, "Inventor", vbDefaultButton1, kNoRestrictions)
    End If

    On Error GoTo 0

    oPM.Display
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |