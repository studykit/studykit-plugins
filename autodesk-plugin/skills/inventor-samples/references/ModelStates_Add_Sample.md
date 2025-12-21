# Create a model state

## Description

This sample demonstrates creation of a model state in an assembly.

## Code Samples

* [VBA](#VBA)

Before running the sample, you need to open an assembly and create two part files called C:\Temp\Part1.ipt and C:\Temp\Part2.ipt, or edit the sample code to point to different part files if desired.

```
Public Sub CreateModelState()
    ' Set a reference to the assembly component definintion.
    ' This assumes an assembly document is open.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Create a matrix. A new matrix is initialized with an identity matrix.
    Dim oMatrix As Matrix
    Set oMatrix = oTG.CreateMatrix

    ' Add the first occurrence.
    Dim oOcc1 As ComponentOccurrence
    Set oOcc1 = oAsmCompDef.Occurrences.Add("C:\Temp\Part1.ipt", oMatrix)

    ' Set the translation portion of the matrix so the
    ' second part will be positioned at (3,2,1).
    Call oMatrix.SetTranslation(oTG.CreateVector(3, 2, 1))

    ' Add the second occurrence.
    Dim oOcc2 As ComponentOccurrence
    Set oOcc2 = oAsmCompDef.Occurrences.Add("C:\Temp\Part2.ipt", oMatrix)

    ' Create a new level of detail representation.
    ' The new representation is automatically activated.
    Dim oModelState As ModelState
    Set oModelState = oAsmCompDef.ModelStates.Add("Part2Suppressed")

    ' Suppress the second component in the new model state.
    ' If the document "C:\Temp\Part2.ipt" is not currently referenced
    ' elsewhere, it will be closed.
    oOcc2.Suppress
End Sub
```
