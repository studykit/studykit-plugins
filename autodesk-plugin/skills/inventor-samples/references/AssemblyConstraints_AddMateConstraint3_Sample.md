# Add mate constraint with limits

## Description

This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub MateConstraintWithLimits()
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

    ' Create the mate constraint between the parts, with an offset value of 0.
    Dim oMate As MateConstraint
    Set oMate = oAsmCompDef.Constraints.AddMateConstraint(oBrepEnt1, oBrepEnt2, 0)

    ' Set a maximum value of 2 inches
    oMate.ConstraintLimits.MaximumEnabled = True
    oMate.ConstraintLimits.Maximum.Expression = "2 in"

    ' Set a minimum value of -2 inches
    oMate.ConstraintLimits.MinimumEnabled = True
    oMate.ConstraintLimits.Minimum.Expression = "-2 in"
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |