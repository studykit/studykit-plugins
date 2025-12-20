# Imprint bodies within an assembly.

## Description

This sample demonstrates creating imprinted bodies from two selected occurrences in an assembly.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateImprintFromAssembly()
    ' Get the active assembly document and its definition.
    Dim asmDoc As AssemblyDocument
    Set asmDoc = ThisApplication.ActiveDocument

    ' Have two parts selected in the assembly.
    Dim part1 As ComponentOccurrence
    Dim part2 As ComponentOccurrence
    Set part1 = ThisApplication.CommandManager.Pick(kAssemblyLeafOccurrenceFilter, "Select part 1")
    Set part2 = ThisApplication.CommandManager.Pick(kAssemblyLeafOccurrenceFilter, "Select part 2")

    ' Get the bodies associated with the occurrences.  Because of a problem when
    ' this sample was written the ImprintBodies method fails when used with SurfaceBodyProxy
    ' objects.  The code below works around this by creating new transformed bodies that
    ' will provide the equivalent result.

    ' Get the bodies in part space as transient bodies.
    Dim transBrep As TransientBRep
    Set transBrep = ThisApplication.TransientBRep
    Dim body1 As SurfaceBody
    Dim body2 As SurfaceBody
    Set body1 = transBrep.Copy(part1.Definition.SurfaceBodies.Item(1))
    Set body2 = transBrep.Copy(part2.Definition.SurfaceBodies.Item(1))

    ' Transform the bodies to be in the location represented in the assembly.
    Call transBrep.Transform(body1, part1.Transformation)
    Call transBrep.Transform(body2, part2.Transformation)

    ' Imprint the bodies.
    Dim newBody1 As SurfaceBody
    Dim newBody2 As SurfaceBody
    Dim body1OverlapFaces As Faces
    Dim body2OverlapFaces As Faces
    Dim body1OverlapEdges As Edges
    Dim body2OverlapEdges As Edges
    Call ThisApplication.TransientBRep.ImprintBodies(body1, body2, True, newBody1, newBody2, _
                                                     body1OverlapFaces, body2OverlapFaces, _
                                                     body1OverlapEdges, body2OverlapEdges)

    ' Create a new part document to show the resulting bodies in.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                  ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Create a new feature from the first imprinted body.
    Dim non1 As NonParametricBaseFeature
    Set non1 = partDef.Features.NonParametricBaseFeatures.Add(newBody1)
    Set newBody1 = non1.SurfaceBodies.Item(1)

    ' Create a new feature from the second imprinted body.
    Dim non2 As NonParametricBaseFeature
    Set non2 = partDef.Features.NonParametricBaseFeatures.Add(newBody2)
    Set newBody2 = non2.SurfaceBodies.Item(1)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |