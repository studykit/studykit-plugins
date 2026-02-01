# iMate Result Creation

## Description

This sample demonstrates creating an iMate result using two existin iMate definitions.

## Code Samples

* [VBA](#VBA)

To use this sample create a new part by extruding a rectangle to create a cube. Create a mate iMate on one of the faces. This sample assumes the iMate is named the default name used in the English version of Inventor, which is iMate:1. If the iMate definition is created with another name you can either edit the name of the iMate definition in the part file, or edit the sample code below to use the different name. Save the part to C:\Temp\iMatePart.ipt. Finally, have an assembly open and run the sample code.

```
Public Sub iMateResultCreationSample()
    ' Get the component definition of the currently open assembly.
    ' This will fail if an assembly document is not open.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Create a new matrix object.  It will be initialized to an identity matrix.
    Dim oMatrix As Matrix
    Set oMatrix = ThisApplication.TransientGeometry.CreateMatrix

    ' Place the first occurrence.
    Dim oOcc1 As ComponentOccurrence
    Set oOcc1 = oAsmCompDef.Occurrences.Add("C:\Temp\iMatePart.ipt", oMatrix)

    ' Place the second occurrence, but adjust the matrix slightly so they're
    ' not right on top of each other.
    oMatrix.Cell(1, 4) = 10
    Dim oOcc2 As ComponentOccurrence
    Set oOcc2 = oAsmCompDef.Occurrences.Add("C:\Temp\iMatePart.ipt", oMatrix)

    ' Look through the iMateDefinitions defined for the first occurrence
    ' and find the one named "iMate:1".  This loop demonstrates using the
    ' Count and Item properties of the iMateDefinitions object.
    Dim i As Long
    Dim oiMateDef1 As iMateDefinition
    For i = 1 To oOcc1.iMateDefinitions.Count
        If oOcc1.iMateDefinitions.Item(i).Name = "iMate:1" Then
            Set oiMateDef1 = oOcc1.iMateDefinitions.Item(i)
            Exit For
        End If
    Next

    If oiMateDef1 Is Nothing Then
        MsgBox "An iMate definition named ""iMate:1"" does not exist in " & oOcc1.Name
        Exit Sub
    End If

    ' Look through the iMateDefinitions defined for the second occurrence
    ' and find the one named "iMate:1".  This loop demonstrates using the
    ' For Each method of iterating through a collection.
    Dim oiMateDef2 As iMateDefinition
    Dim bFoundDefinition As Boolean
    For Each oiMateDef2 In oOcc2.iMateDefinitions
        If oiMateDef2.Name = "iMate:1" Then
            bFoundDefinition = True
            Exit For
        End If
    Next

    If Not bFoundDefinition Then
        MsgBox "An iMate definition named ""iMate:1"" does not exist in " & oOcc2.Name
        Exit Sub
    End If

    ' Create an iMate result using the two definitions.
    Dim oiMateResult As iMateResult
    Set oiMateResult = oAsmCompDef.iMateResults.AddByTwoiMates(oiMateDef1, oiMateDef2)

End Sub
```
