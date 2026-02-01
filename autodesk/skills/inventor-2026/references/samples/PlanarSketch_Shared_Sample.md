# Sketch Share

## Description

This sample demonstrates setting a sketch so it is shared.

## Code Samples

* [VBA](#VBA)

To use this sample, open a part document open that contains at least one extrusion feature and run the sample. The sketch of the first extrusion feature should not already be shared.

```
Public Sub MakeSketchShared()
   ' Set a reference to the part component definition.
   ' This assumes that a part document is active.
   Dim oCompDef As PartComponentDefinition
   Set oCompDef = ThisApplication.ActiveDocument.ComponentDefinition

   ' Get the first extrusion feature in the part.
   ' This assumes that an extrusion feature exists in the part.
   Dim oExtrudeFeature As ExtrudeFeature
   Set oExtrudeFeature = oCompDef.Features.ExtrudeFeatures.Item(1)

   ' Set a reference to the sketch of the feature.
   Dim oSketch As PlanarSketch
   Set oSketch = oExtrudeFeature.Definition.Profile.Parent

   ' Share the sketch of the feature.
   oSketch.Shared = True
End Sub
```
