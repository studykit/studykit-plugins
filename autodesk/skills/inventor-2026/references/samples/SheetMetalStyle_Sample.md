# Sheet Metal Style Display

## Description

This sample illustrates getting information about sheet metal styles.

## Code Samples

* [VBA](#VBA)

```
Public Sub SheetMetalStyleDisplay()
    ' Set a reference to the sheet metal document.
    ' This assumes a part document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Make sure the document is a sheet metal document.
    If oPartDoc.SubType  "{9C464203-9BAE-11D3-8BAD-0060B0CE6BB4}" Then
        MsgBox "A sheet metal document must be open."
        Exit Sub
    End If

    ' Get the sheet metal component definition. Because this is a part document whose
    ' sub type is sheet metal, the document will return a SheetMetalComponentDefinition
    ' instead of a PartComponentDefinition.
    Dim oSheetMetalCompDef As SheetMetalComponentDefinition
    Set oSheetMetalCompDef = oPartDoc.ComponentDefinition

    ' Display then name of the active style.
    Debug.Print "Active Sheet Metal Style: " & oSheetMetalCompDef.ActiveSheetMetalStyle.Name

    ' Iterate through the sheet metal styles.
    Debug.Print ""
    Debug.Print "Sheet Metal Styles"
    Dim oStyle As SheetMetalStyle
    For Each oStyle In oSheetMetalCompDef.SheetMetalStyles
        Debug.Print "  " & oStyle.Name
        Debug.Print "     In Use: " & oStyle.InUse
        Debug.Print "     Up to Date: " & oStyle.UpToDate

        Select Case oStyle.StyleLocation
            Case kBothStyleLocation
                Debug.Print "     Style Location: Both Local and in Library"
            Case kLibraryStyleLocation
                Debug.Print "     Style Location: Library"
            Case kLocalStyleLocation
                Debug.Print "     Style Location: Local"
        End Select

        Debug.Print "     Bend Radius: " & oStyle.BendRadius
        Debug.Print "     Bend Relief Depth: " & oStyle.BendReliefDepth
        Debug.Print "     Bend Relief Width: " & oStyle.BendReliefWidth

        Select Case oStyle.BendReliefShape
            Case kRoundBendReliefShape
                Debug.Print "     Bend Relief Shape: Round"
            Case kStraightBendReliefShape
                Debug.Print "     Bend Relief Shape: Straight"
        End Select

        Select Case oStyle.BendTransition
            Case kArcBendTransition
                Debug.Print "     Bend Transition: Arc"
            Case kDefaultBendTransition
                Debug.Print "     Bend Transition: Default"
            Case kIntersectionBendTransition
                Debug.Print "     Bend Transition: Intersection"
            Case kNoBendTransition
                Debug.Print "     Bend Transition: None"
            Case kStraightLineBendTransition
                Debug.Print "     Bend Transition: Straight Line"
            Case kTrimToBendBendTransition
                Debug.Print "     Bend Transition: Trim to Bend"
        End Select

        Debug.Print "     Bend Transition Arc Radius: " & oStyle.BendTransitionArcRadius

        Debug.Print "     Corner Relief Size: " & oStyle.CornerReliefSize
        Select Case oStyle.CornerReliefShape
            Case kArcWeldCornerReliefShape
                Debug.Print "     Corner Relief Shape: Arc Weld"
            Case kDefaultCornerReliefShape
                Debug.Print "     Corner Relief Shape: Default"
            Case kFullRoundCornerReliefShape
                Debug.Print "     Corner Relief Shape: Full Round"
            Case kIntersectionCornerReliefShape
                Debug.Print "     Corner Relief Shape: Intersection"
            Case kLinearWeldReliefShape
                Debug.Print "     Corner Relief Shape: Linear Weld"
            Case kNoReplacementCornerReliefShape
                Debug.Print "     Corner Relief Shape: No Replacement"
            Case kRoundCornerReliefShape
                Debug.Print "     Corner Relief Shape: Round"
            Case kRoundWithRadiusCornerReliefShape
                Debug.Print "     Corner Relief Shape: Round with Radius"
            Case kSquareCornerReliefShape
                Debug.Print "     Corner Relief Shape: Square"
            Case kTearCornerReliefShape
                Debug.Print "     Corner Relief Shape: Tear"
            Case kTrimToBendReliefShape
                Debug.Print "     Corner Relief Shape: Trim"
        End Select

        Debug.Print "     Corner Relief Size: " & oStyle.ThreeBendCornerReliefSize
        Select Case oStyle.ThreeBendCornerReliefShape
            Case kArcWeldCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Arc Weld"
            Case kDefaultCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Default"
            Case kFullRoundCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Full Round"
            Case kIntersectionCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Intersection"
            Case kLinearWeldReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Linear Weld"
            Case kNoReplacementCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: No Replacement"
            Case kRoundCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Round"
            Case kRoundWithRadiusCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Round with Radius"
            Case kSquareCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Square"
            Case kTearCornerReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Tear"
            Case kTrimToBendReliefShape
                Debug.Print "     Three Bend Corner Relief Shape: Trim"
        End Select

        Debug.Print "     Material: " & oStyle.Material.Name
        Debug.Print "     Minimum Remnant: " & oStyle.MinimumRemnant
        Debug.Print "     Thickness: " & oStyle.Thickness

        Select Case oStyle.PunchRepresentationType
            Case k2DSketchAndCenterMarkPunchRepresentation
                Debug.Print "     Punch Representation Type: 2D Sketch and Center Mark"
            Case k2DSketchPunchRepresentation
                Debug.Print "     Punch Representation Type: 2D Sketch"
            Case kCentermarkPunchRepresentation
                Debug.Print "     Punch Representation Type: Center Mark"
            Case kDefaultPunchRepresentation
                Debug.Print "     Punch Representation Type: Default"
            Case kFormedFeaturePunchRepresentation
                Debug.Print "     Punch Representation Type: Formed Feature"
        End Select

        Debug.Print "     Unfold Method: " & oStyle.UnfoldMethod.Name
    Next

    ' Display information about the unfold methods.
    Debug.Print ""
    Debug.Print "Unfold Methods"
    Dim oUnfoldMethod As UnfoldMethod
    For Each oUnfoldMethod In oSheetMetalCompDef.UnfoldMethods
        Debug.Print "  " & oUnfoldMethod.Name
        Debug.Print "     In Use: " & oUnfoldMethod.InUse
        Debug.Print "     Up to Date: " & oUnfoldMethod.UpToDate

        Select Case oUnfoldMethod.StyleLocation
            Case kBothStyleLocation
                Debug.Print "     Location: Both Local and in Library"
            Case kLibraryStyleLocation
                Debug.Print "     Location: Library"
            Case kLocalStyleLocation
                Debug.Print "     Location: Local"
        End Select

        Select Case oUnfoldMethod.UnfoldMethodType
            Case kBendTableUnfoldMethod
                Debug.Print "     Unfold Method Type: Bend Table"
            Case kLinearUnfoldMethod
                Debug.Print "     Unfold Method Type: Linear"
        End Select
        Debug.Print "     kFactor: " & oUnfoldMethod.kFactor
    Next
End Sub
```
