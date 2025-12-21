# Associative body copy

## Description

The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly.

## Code Samples

* [VBA](#VBA)

Before running the sample, create an assembly with two parts in it. The sample copies the body from the first part into the second part.

|  |
| --- |
| Copy Code |

```
Sub AssociativeBodyCopy()
    ' Set a reference to the active assembly document.
    Dim oAssemblyDoc As AssemblyDocument
    Set oAssemblyDoc = ThisApplication.ActiveDocument

    Dim oAssemblyDef As AssemblyComponentDefinition
    Set oAssemblyDef = oAssemblyDoc.ComponentDefinition

    Dim oOccurrence1 As ComponentOccurrence
    Set oOccurrence1 = oAssemblyDef.Occurrences.Item(1)

    Dim oPartDef1 As PartComponentDefinition
    Set oPartDef1 = oOccurrence1.Definition

    Dim oOccurrence2 As ComponentOccurrence
    Set oOccurrence2 = oAssemblyDef.Occurrences.Item(2)

    Dim oPartDef2 As PartComponentDefinition
    Set oPartDef2 = oOccurrence2.Definition

    ' Get the source solid body from the first part.
    Dim oSourceBody As SurfaceBody
    Set oSourceBody = oPartDef1.SurfaceBodies.Item(1)

    Dim oSourceBodyProxy As SurfaceBodyProxy
    Call oOccurrence1.CreateGeometryProxy(oSourceBody, oSourceBodyProxy)

    ' Create an associative surface base feature in the second part.
    Dim oFeatureDef1 As NonParametricBaseFeatureDefinition
    Set oFeatureDef1 = oPartDef2.Features.NonParametricBaseFeatures.CreateDefinition

    Dim oCollection As ObjectCollection
    Set oCollection = ThisApplication.TransientObjects.CreateObjectCollection

    oCollection.Add oSourceBodyProxy

    oFeatureDef1.BRepEntities = oCollection
    oFeatureDef1.OutputType = kSurfaceOutputType
    oFeatureDef1.TargetOccurrence = oOccurrence2
    oFeatureDef1.IsAssociative = True

    Dim oBaseFeature1 As NonParametricBaseFeature
    Set oBaseFeature1 = oPartDef2.Features.NonParametricBaseFeatures.AddByDefinition(oFeatureDef1)

    ' Create a non-associative solid base feature in the second part.
    Dim oFeatureDef2 As NonParametricBaseFeatureDefinition
    Set oFeatureDef2 = oPartDef2.Features.NonParametricBaseFeatures.CreateDefinition

    oFeatureDef2.BRepEntities = oCollection
    oFeatureDef2.OutputType = kSolidOutputType
    oFeatureDef2.TargetOccurrence = oOccurrence2

    Dim oBaseFeature2 As NonParametricBaseFeature
    Set oBaseFeature2 = oPartDef2.Features.NonParametricBaseFeatures.AddByDefinition(oFeatureDef2)

    oAssemblyDoc.Update
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |