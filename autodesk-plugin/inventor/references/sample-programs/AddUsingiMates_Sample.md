# iMate Creation During Occurrence Placement

## Description

This sample demonstrates creating multiple iMate results when adding an occurrence into an assembly. This uses the AddUsingiMate method which is the equivalent of using the Place Component command and checking the Use iMate check box on the dialog.

## Code Samples

* [VBA](#VBA)

To use this sample create a new part by extruding a rectangle to create a cube. Create a mate iMate on one of the faces. Next, create a flush iMate on any of the faces connecting to the first face. Save this part to C:\TempiMatePart.ipt. Finally, have an assembly open and run the sample code.

|  |
| --- |
| Copy Code |

```
Public Sub iMateDuringOccurrencePlacementSample()
    ' Get the component definition of the currently open assembly.
    ' This will fail if an assembly document is not open.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Create a new matrix object. It will be initialized to an identity matrix.
    Dim oMatrix As Matrix
    Set oMatrix = ThisApplication.TransientGeometry.CreateMatrix

    ' Place the first occurrence.
    Dim oOcc1 As ComponentOccurrence
    Set oOcc1 = oAsmCompDef.Occurrences.Add("C:\TempiMatePart.ipt", oMatrix)

    ' Place the second occurrence, but use iMates for its placement. This is
    ' equivalent to "Use iMate" check box on the "Place Component" dialog.
    Dim oOccEnumerator As ComponentOccurrencesEnumerator
    Set oOccEnumerator = oAsmCompDef.Occurrences.AddUsingiMates("C:\TempiMatePart.ipt", False)

    ' Since the 'PlaceAllMatching' flag was specified as False, we can be
    ' sure that just one ComponentOccurrence was returned in the enumerator.
    Dim oOcc1 As ComponentOccurrence
    Set oOcc1 = oOccEnumerator.Item(1)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |