# Display feature information

## Description

Displays information about all of the extrude features in the active document. A part document must be active when this is run.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub GetFeatureInfo()
    ' Get the active document assuming it is a part.
    Dim partDoc As PartDocument
    Set partDoc = ThisApplication.ActiveDocument

    ' Get the component definition.  This owns the part specific info for the part.
    Dim partDef As PartComponentDefinition
    Set partDef = partDoc.ComponentDefinition

    ' Iterate over the extrude features.
    Dim extrude As ExtrudeFeature
    For Each extrude In partDef.Features.ExtrudeFeatures
        Debug.Print extrude.name

        ' Get the definition object from the feature.
        Dim extrudeDef As ExtrudeDefinition
        Set extrudeDef = extrude.Definition

        ' Display information in the definition object.
        Select Case extrudeDef.ExtentType
            Case kDistanceExtent
                Dim distance As DistanceExtent
                Set distance = extrudeDef.Extent

                Debug.Print "Distance"
                Call DisplayToleranceInfo(distance.distance)
            Case kFromToExtent
                Dim fromTo As FromToExtent
                Set fromTo = extrudeDef.Extent

                Debug.Print "FromTo extent between to faces and/or work features."
            Case kThroughAllExtent
                Dim throughAll As ThroughAllExtent
                Set throughAll = extrudeDef.Extent

                Debug.Print "Through all extent."
            Case kToExtent
                Dim toExt As ToExtent
                Set toExt = extrudeDef.Extent

                Debug.Print "To a face or work plane extent."
            Case kToNextExtent
                Dim toNext As ToNextExtent
                Set toNext = extrudeDef.Extent

                Debug.Print "To next extent."
            Case Else
                Debug.Print "Unhandled case: " & extrudeDef.ExtentType
        End Select
    Next
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |