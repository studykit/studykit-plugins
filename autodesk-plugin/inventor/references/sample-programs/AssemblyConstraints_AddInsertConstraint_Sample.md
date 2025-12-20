# Add assembly insert constraint

## Description

This sample demonstrates the creation of an assembly insert constraint.

## Code Samples

* [VBA](#VBA)

Before running the sample, you need to open an assembly that contains at least two parts. Select circular edges on the two parts that will be used for the constraint and run the sample code. (Set the priority of the Select command and use the Shift-Select to select multiple edges.)

|  |
| --- |
| Copy Code |

```
Public Sub InsertConstraint()
    ' Set a reference to the assembly component definintion.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Set a reference to the select set.
    Dim oSelectSet As SelectSet
    Set oSelectSet = ThisApplication.ActiveDocument.SelectSet

    ' Validate the correct data is in the select set.
    If oSelectSet.Count <> 2 Then
        MsgBox "You must select the two circular edges for the insert."
        Exit Sub
    End If

    If Not TypeOf oSelectSet.Item(1) Is Edge Or Not TypeOf oSelectSet.Item(2) Is Edge Then
        MsgBox "You must select the two circular edges for the insert."
        Exit Sub
    End If

    ' Get the two edges from the select set.
    Dim oEdge1 As Edge
    Dim oEdge2 As Edge
    Set oEdge1 = oSelectSet.Item(1)
    Set oEdge2 = oSelectSet.Item(2)

    ' Create the insert constraint between the parts.
    Dim oInsert As InsertConstraint
    Set oInsert = oAsmCompDef.Constraints.AddInsertConstraint(oEdge1, oEdge2, True, 0)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |