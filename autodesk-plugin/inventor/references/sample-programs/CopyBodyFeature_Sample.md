# SurfaceBody Copy

## Description

This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CopyBodyFromPartToPart()
    ' The first portion of this program creates an assembly so that the
    ' copy body API can be demonstrated. Any assembly could potentially
    ' be used, but the sample is simpler if it's for a specific case.
    '
    ' This creates an assembly that contains two parts. An interesting
    ' aspect of the sample is that the assembly and parts only exist
    ' in memory and are not written to disk. Filenames are assigned,
    ' so that if you perform a Save they will be written to disk using
    ' the specified filenames.

    ' Create a new assembly.
    Dim oAsmDoc As AssemblyDocument
    Set oAsmDoc = ThisApplication.Documents.Add(kAssemblyDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kAssemblyDocumentObject))

    ' Define the filename for the assembly. It won't be saved at this point, but
    ' this name will be used if the assembly is saved later by the user.
    oAsmDoc.FullFileName = "C:\Temp\CopyBodyTestAsm.iam"

    ' Create a new part, invisibly.
    Dim oPartDoc1 As PartDocument
    Set oPartDoc1 = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject), False)

    ' Define the filename for the part. It won't be saved at this point, but
    ' this name will be used if the part is saved later by the user.
    oPartDoc1.FullFileName = "C:\Temp\CopyBodyTestPart1.ipt"

    ' Set a reference to the transient geometry object.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc1.ComponentDefinition

    ' Create an extrude feature.
    Dim oSketch As PlanarSketch
    Set oSketch = oCompDef.Sketches.Add(oCompDef.WorkPlanes.Item(1))
    Call oSketch.SketchCircles.AddByCenterRadius(oTG.CreatePoint2d(0, 0), 2)
    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(3, kPositiveExtentDirection)
    Dim oExtrude As ExtrudeFeature
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Create a second extrude feature as a work surface.
    Set oSketch = oPartDoc1.ComponentDefinition.Sketches.Add( _
                    oPartDoc1.ComponentDefinition.WorkPlanes.Item(1))
    Call oSketch.SketchLines.AddAsTwoPointRectangle(oTG.CreatePoint2d(-3, -3), oTG.CreatePoint2d(3, 3))
    Set oProfile = oSketch.Profiles.AddForSolid

    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kSurfaceOperation)
    Call oExtrudeDef.SetDistanceExtent(1.5, kPositiveExtentDirection)
    Set oExtrude = oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Insert the occurrence into the assembly using a somewhat arbitrary position.
    Dim oMatrix As Matrix
    Set oMatrix = oTG.CreateMatrix
    Call oMatrix.Translation.AddVector(oTG.CreateVector(2, 3, 4))
    Call oMatrix.SetToRotation(0.5, oTG.CreateVector(1, 0, 0), oTG.CreatePoint(2, 3, 4))
    Dim oOcc1 As ComponentOccurrence
    Set oOcc1 = oAsmDoc.ComponentDefinition.Occurrences.AddByComponentDefinition( _
                                        oPartDoc1.ComponentDefinition, oMatrix)

    ' Create a second new part, invisibly.
    Dim oPartDoc2 As PartDocument
    Set oPartDoc2 = ThisApplication.Documents.Add(kPartDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject), False)

    ' Define the filename for the part. It won't be saved at this point, but
    ' this name will be used if the part is saved later by the user.
    oPartDoc2.FullFileName = "C:\Temp\CopyBodyTestPart2.ipt"

    ' Insert the second part into the assembly using a somewhat arbitrary position.
    Set oMatrix = oTG.CreateMatrix
    Call oMatrix.Translation.AddVector(oTG.CreateVector(-1, -1, -1))
    Call oMatrix.SetToRotation(0.5, oTG.CreateVector(1, 1, 0), oTG.CreatePoint(1, 1, 1))
    Dim oOcc2 As ComponentOccurrence
    Set oOcc2 = oAsmDoc.ComponentDefinition.Occurrences.AddByComponentDefinition( _
                                        oPartDoc2.ComponentDefinition, oMatrix)

    ' Get the surface body from the first part that represents the work surface.
    ' In this case we know there's only one work surface so this just gets the
    ' first work surface in the collection.
    Dim oWorkSurface As WorkSurface
    Set oWorkSurface = oPartDoc1.ComponentDefinition.WorkSurfaces.Item(1)
    Dim oBody As SurfaceBody
    Set oBody = oWorkSurface.SurfaceBodies.Item(1)

    ' Define the matrix to use in copying the surface body from one part to
    ' another. Any matrix can be used, but in this case I want the position
    ' of the body to be the same with respect to assembly space. Because
    ' the occurrences are in different positions within the assembly the matrix
    ' needs to take into account the transfrom from one occurrence to the other.

    ' Get the transform from the occurrence where the surface body currently exists.
    ' This defines the tranform of the surface body into assembly space.
    Set oMatrix = oOcc1.Transformation

    ' Get the matrix of the second occurrence and invert it.
    ' The inverse of the second occurrence's transform defines the tranform from
    ' assembly space into that occurrence's part space.
    Dim oMatrix2 As Matrix
    Set oMatrix2 = oOcc2.Transformation
    oMatrix2.Invert

    ' Combine these matrices.
    Call oMatrix.PreMultiplyBy(oMatrix2)

    ' Copy the surface body from the first part into the second. You shouldn't
    ' see anything graphically change because the new body is directly on top of
    ' the existing body, but it can be verified because the new body is in
    ' the second part.
    Call oPartDoc2.ComponentDefinition.Features.NonParametricBaseFeatures.Add(oBody, oMatrix)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |