# Add mate constraint using work planes in parts

## Description

This sample demonstrates creating a mate constraint between two occurrences using the work planes within those occurrences.

## Code Samples

* [VBA](#VBA)

To use the sample, have an assembly open that contains at least two occurrences, (part or subassembly), and run the program.

```
Public Sub MateConstraintOfWorkPlanes()
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Get references to the two occurrences to constrain.
    ' This arbitrarily gets the first and second occurrence.
    Dim oOcc1 As ComponentOccurrence
    Set oOcc1 = oAsmCompDef.Occurrences.Item(1)

    Dim oOcc2 As ComponentOccurrence
    Set oOcc2 = oAsmCompDef.Occurrences.Item(2)

    ' Get the XY plane from each occurrence.  This goes to the
    ' component definition of the part to get this information.
    ' This is the same as accessing the part document directly.
    ' The work plane obtained is in the context of the part,
    ' not the assembly.
    Dim oPartPlane1 As WorkPlane
    Set oPartPlane1 = oOcc1.Definition.WorkPlanes.Item(3)

    Dim oPartPlane2 As WorkPlane
    Set oPartPlane2 = oOcc2.Definition.WorkPlanes.Item(3)

    ' Because we need the work plane in the context of the assembly
    ' we need to create proxies for the work planes.  The proxies
    ' represent the work planes in the context of the assembly.
    Dim oAsmPlane1 As WorkPlaneProxy
    Call oOcc1.CreateGeometryProxy(oPartPlane1, oAsmPlane1)

    Dim oAsmPlane2 As WorkPlaneProxy
    Call oOcc2.CreateGeometryProxy(oPartPlane2, oAsmPlane2)

    ' Create the constraint using the work plane proxies.
    Call oAsmCompDef.Constraints.AddMateConstraint(oAsmPlane1, oAsmPlane2, 0)
End Sub
```
