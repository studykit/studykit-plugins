# Part SimplifyFeature Sample

## Description

This sample demonstrates how to create a simplify feature in part document.

## Code Samples

* [VBA](#VBA)
* [VBA](#VBA)

This sample demonstrates how to create a simplify feature in part document. You need to open a part document firstly before running below sample code.

|  |
| --- |
| Copy Code |

```
Sub PartSimplifyFeatureSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oSimplifyFeatures As SimplifyFeatures
    Set oSimplifyFeatures = oCompDef.Features.SimplifyFeatures

    Dim oSimplifyDef As SimplifyDefinition
    Set oSimplifyDef = oSimplifyFeatures.CreateDefinition()

    ' Configure the options for simplify feature.
    oSimplifyDef.EnvelopesReplaceStyle = kEachBodyReplaceStyle
    oSimplifyDef.EnvelopeBoundingType = kOrientedMinimumBoundingBox
    oSimplifyDef.RemoveInternalBodies = False
    oSimplifyDef.RemoveBodiesBySize = True
    ' remove bodies which diagonal size is less than 10 centimeters.
    oSimplifyDef.RemoveBodiesSize = 10

    ' Create the Simplify feature.
    Dim oSimplifyFeature As SimplifyFeature
    Set oSimplifyFeature = oSimplifyFeatures.Add(oSimplifyDef)
End Sub
```

This sample demonstrates how to create a simplify feature in part document. You need to open a part document firstly before running below sample code.

|  |
| --- |
| Copy Code |

```
Sub PartSimplifyFeatureSample()
    Dim oDoc As PartDocument
    Set oDoc = ThisApplication.ActiveDocument

    Dim oCompDef As PartComponentDefinition
    Set oCompDef = oDoc.ComponentDefinition

    Dim oSimplifyFeatures As SimplifyFeatures
    Set oSimplifyFeatures = oCompDef.Features.SimplifyFeatures

    Dim oSimplifyDef As SimplifyDefinition
    Set oSimplifyDef = oSimplifyFeatures.CreateDefinition()

    ' Configure the options for simplify feature.
    oSimplifyDef.EnvelopesReplaceStyle = kEachBodyReplaceStyle
    oSimplifyDef.EnvelopeBoundingType = kOrientedMinimumBoundingBox
    oSimplifyDef.RemoveInternalBodies = False
    oSimplifyDef.RemoveBodiesBySize = True
    ' remove bodies which diagonal size is less than 10 centimeters.
    oSimplifyDef.RemoveBodiesSize = 10

    ' Create the Simplify feature.
    Dim oSimplifyFeature As SimplifyFeature
    Set oSimplifyFeature = oSimplifyFeatures.Add(oSimplifyDef)
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |