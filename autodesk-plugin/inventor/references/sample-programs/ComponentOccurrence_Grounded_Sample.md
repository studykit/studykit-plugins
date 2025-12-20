# Assembly Ground Occurrences

## Description

This sample demonstrates grounding an assembly occurrence.

## Code Samples

* [VBA](#VBA)

Before running the sample, you need to open an assembly and create a part file called C:\TempPart1.ipt, or edit the sample code to point to another part file if desired.

|  |
| --- |
| Copy Code |

```
Public Sub FixAllOccurrences()
    ' Set a reference to the assembly component definintion.
    ' This assumes an assembly document is open.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Ask whether to delete or suppress the existing constraints.
    Dim bDelete As Boolean
    If MsgBox("Do you want to delete all existing constraints?", vbYesNo + vbQuestion) = vbYes Then
      bDelete = True
    Else
      bDelete = False
    End If

    ' Iterate through all of the constraints and perform the specified operation.
    Dim oConstraint As AssemblyConstraint
    For Each oConstraint In oAsmCompDef.Constraints
      If bDelete Then
        oConstraint.Delete
      Else
        oConstraint.Suppressed = True
      End If
    Next

    ' Iterate through all of the occurrences and ground them.
    Dim oOccurrence As ComponentOccurrence
    For Each oOccurrence In oAsmCompDef.Occurrences
      oOccurrence.Grounded = True
    Next
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |