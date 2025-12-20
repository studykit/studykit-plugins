# Sheet Metal Feature Display

## Description

This sample illustrates getting basic information from the various sheet metal features.

## Code Samples

* [VBA](#VBA)

Before running the sample, open a sheet metal document that contains some features.

|  |
| --- |
| Copy Code |

```
Public Sub SheetMetalFeatureDisplay()
    ' Set a reference to the sheet metal document.
    ' This assumes a part document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Make sure the document is a sheet metal document.
    If oPartDoc.SubType  "{9C464203-9BAE-11D3-8BAD-0060B0CE6BB4}" Then
        MsgBox "A sheet metal document must be open."
        Exit Sub
    End If

    ' Get the sheet metal component definition.  Because this is a part document whose
    ' sub type is sheet metal, the document will return a SheetMetalComponentDefinition
    ' instead of a PartComponentDefinition.
    Dim oSheetMetalCompDef As SheetMetalComponentDefinition
    Set oSheetMetalCompDef = oPartDoc.ComponentDefinition

    ' Iterate through the features looking specifically for sheet metal features.
    Dim oFeature As PartFeature
    For Each oFeature In oSheetMetalCompDef.Features
        Select Case oFeature.Type
            Case kFaceFeatureObject
                Dim oFaceFeature As FaceFeature
                Set oFaceFeature = oFeature
                Debug.Print "Face Feature: " & oFaceFeature.Name
                Debug.Print "   Adaptive: " & oFaceFeature.Adaptive
                Debug.Print "   Face Count: " & oFaceFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oFaceFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oFaceFeature.Suppressed
            Case kContourFlangeFeatureObject
                Dim oContourFlangeFeature As ContourFlangeFeature
                Set oContourFlangeFeature = oFeature
                Debug.Print "Contour Flange Feature: " & oContourFlangeFeature.Name
                Debug.Print "   Adaptive: " & oContourFlangeFeature.Adaptive
                Debug.Print "   Face Count: " & oContourFlangeFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oContourFlangeFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oContourFlangeFeature.Suppressed
            Case kCutFeatureObject
                Dim oCutFeature As CutFeature
                Set oCutFeature = oFeature
                Debug.Print "Cut Feature: " & oCutFeature.Name
                Debug.Print "   Adaptive: " & oCutFeature.Adaptive
                Debug.Print "   Face Count: " & oCutFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oCutFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oCutFeature.Suppressed
            Case kFlangeFeatureObject
                Dim oFlangeFeature As FlangeFeature
                Set oFlangeFeature = oFeature
                Debug.Print "Flange Feature: " & oFlangeFeature.Name
                Debug.Print "   Adaptive: " & oFlangeFeature.Adaptive
                Debug.Print "   Face Count: " & oFlangeFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oFlangeFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oFlangeFeature.Suppressed
            Case kHemFeatureObject
                Dim oHemFeature As HemFeature
                Set oHemFeature = oFeature
                Debug.Print "Hem Feature: " & oHemFeature.Name
                Debug.Print "   Adaptive: " & oHemFeature.Adaptive
                Debug.Print "   Face Count: " & oHemFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oHemFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oHemFeature.Suppressed
            Case kFoldFeatureObject
                Dim oFoldFeature As FoldFeature
                Set oFoldFeature = oFeature
                Debug.Print "Fold Feature: " & oFoldFeature.Name
                Debug.Print "   Adaptive: " & oFoldFeature.Adaptive
                Debug.Print "   Face Count: " & oFoldFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oFoldFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oFoldFeature.Suppressed
            Case kCornerFeatureObject
                Dim oCornerFeature As CornerFeature
                Set oCornerFeature = oFeature
                Debug.Print "Corner Seam Feature: " & oCornerFeature.Name
                Debug.Print "   Adaptive: " & oCornerFeature.Adaptive
                Debug.Print "   Face Count: " & oCornerFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oCornerFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oCornerFeature.Suppressed
            Case kBendFeatureObject
                Dim oBendFeature As BendFeature
                Set oBendFeature = oFeature
                Debug.Print "Bend Feature: " & oBendFeature.Name
                Debug.Print "   Adaptive: " & oBendFeature.Adaptive
                Debug.Print "   Face Count: " & oBendFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oBendFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oBendFeature.Suppressed
            Case kCornerRoundFeatureObject
                Dim oCornerRoundFeature As CornerRoundFeature
                Set oCornerRoundFeature = oFeature
                Debug.Print "Corner Round Feature: " & oCornerRoundFeature.Name
                Debug.Print "   Adaptive: " & oCornerRoundFeature.Adaptive
                Debug.Print "   Face Count: " & oCornerRoundFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oCornerRoundFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oCornerRoundFeature.Suppressed
            Case kCornerChamferFeatureObject
                Dim oCornerChamferFeature As CornerChamferFeature
                Set oCornerChamferFeature = oFeature
                Debug.Print "Corner Chamfer Feature: " & oCornerChamferFeature.Name
                Debug.Print "   Adaptive: " & oCornerChamferFeature.Adaptive
                Debug.Print "   Face Count: " & oCornerChamferFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oCornerChamferFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oCornerChamferFeature.Suppressed
            Case kPunchToolFeatureObject
                Dim oPunchToolFeature As PunchToolFeature
                Set oPunchToolFeature = oFeature
                Debug.Print "Punch Tool Feature: " & oPunchToolFeature.Name
                Debug.Print "   Adaptive: " & oPunchToolFeature.Adaptive
                Debug.Print "   Face Count: " & oPunchToolFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oPunchToolFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oPunchToolFeature.Suppressed
            Case Else
                Debug.Print "Non Sheetmetal Feature: " & oFeature.Name
                Debug.Print "   Adaptive: " & oFeature.Adaptive
                Debug.Print "   Face Count: " & oFeature.Faces.Count
                Debug.Print "   HealthStatus: " & oFeature.HealthStatus
                Debug.Print "   RangeBox: (" & Format(oFaceFeature.RangeBox.MinPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MinPoint.Z, "0.00000") & ")-(" & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.X, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Y, "0.00000") & ", " & _
                                        Format(oFaceFeature.RangeBox.MaxPoint.Z, "0.00000") & ")"
                Debug.Print "   Suppressed: " & oFeature.Suppressed
        End Select
    Next
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |