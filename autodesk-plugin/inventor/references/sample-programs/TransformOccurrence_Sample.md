# Assembly Move Occurrence

## Description

This sample demonstrates moving a component occurrence. This sample performs a translate, but a rotate can also be performed since the transform is defined using a matrix.

## Code Samples

* [VBA](#VBA)

Before running the sample you need to open an assembly and select the occurrence to move. The sample code first moves the occurrence honoring any existing constraints and then moves it ignoring any constraints.

|  |
| --- |
| Copy Code |

```
Public Sub MoveOccurrence()
   ' Set a reference to the assembly component definintion.
   Dim oAsmCompDef As AssemblyComponentDefinition
   Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

   ' Get an occurrence from the select set.
   On Error Resume Next
   Dim oOccurrence As ComponentOccurrence
   Set oOccurrence = ThisApplication.ActiveDocument.SelectSet.Item(1)
   If Err Then
      MsgBox "An occurrence must be selected."
      Exit Sub
   End If
   On Error GoTo 0

   ' Get the current transformation matrix from the occurrence.
   Dim oTransform As Matrix
   Set oTransform = oOccurrence.Transformation

   ' Move the occurrence honoring any existing constraints.
   oTransform.SetTranslation ThisApplication.TransientGeometry.CreateVector(2, 2, 3)
   oOccurrence.Transformation = oTransform

   ' Move the occurrence ignoring any constraints.
   ' Anything that causes the assembly to recompute will cause the
   ' occurrence to reposition itself to honor the constraints.
   oTransform.SetTranslation ThisApplication.TransientGeometry.CreateVector(3, 4, 5)
   Call oOccurrence.SetTransformWithoutConstraints(oTransform)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |