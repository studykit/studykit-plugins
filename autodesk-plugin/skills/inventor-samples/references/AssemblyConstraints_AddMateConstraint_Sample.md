# Add assembly mate constraint

## Description

This sample demonstrates the creation of an assembly mate constraint.

## Code Samples

* [VBA](#VBA)

Before running the sample, you need to open an assembly that contains at least two parts. Select planar faces on the two parts that will be used for the constraint and run the sample code. (Set the priority of the Select command and use the Shift-Select to select multiple faces.)

|  |
| --- |
| Copy Code |

```
Public Sub MateConstraint()
    ' Set a reference to the assembly component definintion.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Set a reference to the select set.
    Dim oSelectSet As SelectSet
    Set oSelectSet = ThisApplication.ActiveDocument.SelectSet

    ' Validate the correct data is in the select set.
    If oSelectSet.Count <> 2 Then
        MsgBox "You must select the two entities valid for mate."
        Exit Sub
    End If

    ' Get the two entities from the select set.
    Dim oBrepEnt1 As Object
    Dim oBrepEnt2 As Object
    Set oBrepEnt1 = oSelectSet.Item(1)
    Set oBrepEnt2 = oSelectSet.Item(2)

    ' Create the insert constraint between the parts.
    Dim oMate As MateConstraint
    Set oMate = oAsmCompDef.Constraints.AddMateConstraint(oBrepEnt1, oBrepEnt2, 0)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |