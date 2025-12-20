# Derived Parts and Assemblies

## Description

This sample demonstrates the use of the API to create derived parts and assemblies.

## Code Samples

* [VBA](#VBA)

This example used is a simple case of a part subtracted from a mold. To simplify setup, the program creates the parts representing the part and the mold. It then uses derived parts and assemblies to scale the part and subtract it from the mold.

|  |
| --- |
| Copy Code |

```
Public Sub MoldBaseSample()
    ' Initialize the string that defines the directory where the
    ' files will be created.
    Dim sFilePath As String
    sFilePath = "C:\Temp\"

    ' Call the functions to create the parts that represent the
    ' molded part and the mold base.
    Call CreateMoldPart(sFilePath & "MoldPart.ipt")
    Call CreateMoldBase(sFilePath & "MoldBase.ipt")

    ' Create a new part file to derive the mold part in.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Create a derived definition for the molded part.
    Dim oDerivedPartDef As DerivedPartUniformScaleDef
    Set oDerivedPartDef = oPartDoc.ComponentDefinition.ReferenceComponents.DerivedPartComponents.CreateUniformScaleDef(sFilePath & "MoldPart.ipt")

    ' Set the scale to use.
    oDerivedPartDef.ScaleFactor = 1.1

    ' We could set other options for the derived part using the derived part definition.
    ' In this case the defaults are good except for the scale which we changed.

    ' Create the derived part.
    Call oPartDoc.ComponentDefinition.ReferenceComponents.DerivedPartComponents.Add(oDerivedPartDef)

    ' Save and close the part.  Uses SilentOperation to bypass the save dialog.
    ThisApplication.SilentOperation = True
    Call oPartDoc.SaveAs(sFilePath & "ScaledMoldPart.ipt", False)
    ThisApplication.SilentOperation = False
    oPartDoc.Close

    ' Create a new assembly file to put the mold base and scaled part together.
    Dim oAsmDoc As AssemblyDocument
    Set oAsmDoc = ThisApplication.Documents.Add(kAssemblyDocumentObject, _
                ThisApplication.FileManager.GetTemplateFile(kAssemblyDocumentObject))

    ' Create the matrix used to define the position of the occurrences.  When a new
    ' matrix is created it is initialized to an identity matrix.  This will cause
    ' parts to be placed into the assembly in the same location that are in part space.
    Dim oMatrix As Matrix
    Set oMatrix = ThisApplication.TransientGeometry.CreateMatrix

    ' Place the mold base.
    Dim oOcc As ComponentOccurrence
    Set oOcc = oAsmDoc.ComponentDefinition.Occurrences.Add(sFilePath & "MoldBase.ipt", oMatrix)

    ' Rename the occurrence.  This sample uses the name to identify the occurrence later.
    ' This isn't the only method that could be used, but is one of the simplest.
    oOcc.Name = "Mold Base"

    ' Place the scaled part.
    Set oOcc = oAsmDoc.ComponentDefinition.Occurrences.Add(sFilePath & "ScaledMoldPart.ipt", oMatrix)
    oOcc.Name = "Mold Part"

    ' Save and close the assembly.
    Call oAsmDoc.SaveAs(sFilePath & "MoldSample.iam", False)
    oAsmDoc.Close

    ' Create a new part to derive the assembly into, subtracting the part from the mold base.
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Create a derived definition for the molded assembly.
    Dim oDerivedAsmDef As DerivedAssemblyDefinition
    Set oDerivedAsmDef = oPartDoc.ComponentDefinition.ReferenceComponents.DerivedAssemblyComponents.CreateDefinition(sFilePath & "MoldSample.iam")

    ' Set the part to be subtracted.
    oDerivedAsmDef.Occurrences.Item("Mold Part").InclusionOption = kDerivedSubtractAll

    ' Create the derived assembly.
    Call oPartDoc.ComponentDefinition.ReferenceComponents.DerivedAssemblyComponents.Add(oDerivedAsmDef)
End Sub

' Sub to create the part representing the molded part.
Private Sub CreateMoldPart(Filename As String)
    ' Create a new part document using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Create a new sketch on the XY base workplane.
    Dim oSketch As PlanarSketch
    Set oSketch = oPartDoc.ComponentDefinition.Sketches.Add(oPartDoc.ComponentDefinition.WorkPlanes(3))

    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry

    ' Draw the geometry defining the shape of the part.
    Dim oPoints As ObjectCollection
    Set oPoints = ThisApplication.TransientObjects.CreateObjectCollection
    oPoints.Add oTG.CreatePoint2d(-5, 0)
    oPoints.Add oTG.CreatePoint2d(-4, 3)
    oPoints.Add oTG.CreatePoint2d(-2, 4)
    oPoints.Add oTG.CreatePoint2d(0, 3)
    oPoints.Add oTG.CreatePoint2d(3, 4)
    oPoints.Add oTG.CreatePoint2d(4, 2)
    oPoints.Add oTG.CreatePoint2d(5, 0)

    Dim oSpline As SketchSpline
    Set oSpline = oSketch.SketchSplines.Add(oPoints)
    oSpline.FitMethod = kSweetSplineFit

    Dim oLine As SketchLine
    Set oLine = oSketch.SketchLines.AddByTwoPoints(oSpline.FitPoint(1), oSpline.FitPoint(oSpline.FitPointCount))

    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create a revolved feature.
    Call oPartDoc.ComponentDefinition.Features.RevolveFeatures.AddFull(oProfile, oLine, kJoinOperation)

    ' Save and close the document.
    Call oPartDoc.SaveAs(Filename, False)
    oPartDoc.Close
End Sub

' Sub to create the part representing the mold base.
Private Sub CreateMoldBase(Filename As String)
    ' Create a new part document using the default part template.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.Documents.Add(kPartDocumentObject, _
                 ThisApplication.FileManager.GetTemplateFile(kPartDocumentObject))

    ' Create a new sketch on the XY base workplane.
    Dim oSketch As PlanarSketch
    Set oSketch = oPartDoc.ComponentDefinition.Sketches.Add(oPartDoc.ComponentDefinition.WorkPlanes(3))

    ' Draw the geometry defining the shape of the part.
    Dim oTG As TransientGeometry
    Set oTG = ThisApplication.TransientGeometry
    Call oSketch.SketchLines.AddAsTwoPointRectangle(oTG.CreatePoint2d(-6, -5), oTG.CreatePoint2d(6, 5))

    Dim oProfile As Profile
    Set oProfile = oSketch.Profiles.AddForSolid

    ' Create an extruded feature.
    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oPartDoc.ComponentDefinition
    Dim oExtrudeDef As ExtrudeDefinition
    Set oExtrudeDef = oCompDef.Features.ExtrudeFeatures.CreateExtrudeDefinition(oProfile, kJoinOperation)
    Call oExtrudeDef.SetDistanceExtent(5, kNegativeExtentDirection)
    Call oCompDef.Features.ExtrudeFeatures.Add(oExtrudeDef)

    ' Save and close the document.
    Call oPartDoc.SaveAs(Filename, False)
    oPartDoc.Close
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |