# Set the value of a parameter

## Description

Sets the value of an existing parameter. A part must be open that contains a parameter named "Length".

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub SetParameter()
    ' Get the Parameters object. Assumes a part or assembly document is active.
    Dim oParameters As Parameters
    Set oParameters = ThisApplication.ActiveDocument.ComponentDefinition.Parameters

    ' Get the parameter named "Length".
    Dim oLengthParam As Parameter
    Set oLengthParam = oParameters.Item("Length")

    ' Change the equation of the parameter.
    oLengthParam.Expression = "3.5 in"

    ' Update the document.
    ThisApplication.ActiveDocument.Update
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |