# Projection - project across parts

## Description

This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program.

## Code Samples

* [VBA](#VBA)

```
Public Sub ProjectingAcrossParts()
    ' Set a reference to the assembly component definition.
    Dim oAsmCompDef As AssemblyComponentDefinition
    Set oAsmCompDef = ThisApplication.ActiveDocument.ComponentDefinition

    ' Get references to two occurrences.
    ' This arbitrarily gets the first and second occurrence.
    Dim oOcc1 As ComponentOccurrence
    Set oOcc1 = oAsmCompDef.Occurrences.Item(1)

    Dim oOcc2 As ComponentOccurrence
    Set oOcc2 = oAsmCompDef.Occurrences.Item(2)

    ' Create a sketch on the first part.
    Dim oSketch1 As PlanarSketch
    Set oSketch1 = oOcc1.Definition.Sketches.Add(oOcc1.Definition.WorkPlanes(1))

    ' Set a reference to the transient geometry collection.
    Dim oTransGeom As TransientGeometry
    Set oTransGeom = ThisApplication.TransientGeometry

    ' Create a sketch line on the sketch.
    Dim oSketchLine1 As Object
    Set oSketchLine1 = oSketch1.SketchLines.AddByTwoPoints(oTransGeom.CreatePoint2d(0, 0), _
    oTransGeom.CreatePoint2d(4, 0))

    ' Because we need the sketch line in the context of the assembly
    ' we need to create a proxy for the sketch line. The proxy
    ' represents the sketch line in the context of the assembly.
    Dim oSketchLine1Proxy As Object
    Call oOcc1.CreateGeometryProxy(oSketchLine1, oSketchLine1Proxy)

    ' Create a sketch on the second part.
    Dim oSketch2 As PlanarSketch
    Set oSketch2 = oOcc2.Definition.Sketches.Add(oOcc2.Definition.WorkPlanes(1))

    ' Create a proxy for the sketch in the second part.
    Dim oSketch2Proxy As PlanarSketchProxy
    Call oOcc2.CreateGeometryProxy(oSketch2, oSketch2Proxy)

    ' Project the line in the sketch in the first
    ' part to the sketch in the second part
    Dim oSketchLine2Proxy As SketchLineProxy
    Set oSketchLine2Proxy = oSketch2Proxy.AddByProjectingEntity(oSketchLine1Proxy)
End Sub
```
