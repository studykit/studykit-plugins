# Sheet Metal Style Creation

## Description

This sample illustrates creating a new sheet metal style. It uses a bend table and assumes the sample bend table delivered with Inventor is available. You can edit the path below to reference any existing bend table. To use the sample make sure a bend table is available at the specified path, open a sheet metal document, and run the sample.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateSheetMetalStyle()
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

    ' Create a new unfold method.
    Dim okFactorUnfoldMethod As UnfoldMethod
    Set okFactorUnfoldMethod = oSheetMetalCompDef.UnfoldMethods.AddLinearUnfoldMethod("kFactorTest", "0.43")

    ' Create a new unfold method using a bend table.
    Dim oTableUnfoldMethod As UnfoldMethod
    On Error Resume Next
    Set oTableUnfoldMethod = oSheetMetalCompDef.UnfoldMethods.AddBendTableFromFile("Table Sample", "C:\Program Files\Autodesk\Inventor 2010\Design Data\Bend Tables\Bend Table (in).txt")
    If Err Then
        MsgBox "Unable to load bend table"
    End If
    On Error Goto 0

    ' Copy a sheet metal style to create a new one. This arbitrarily uses the
    ' first style in the collection.
    Dim oStyle As SheetMetalStyle
    Set oStyle = oSheetMetalCompDef.SheetMetalStyles.Item(1).Copy("Sample Style")

    ' Set the value for the thickness. This is an expression that will be used to
    ' set a parameter when this style is activated.
    oStyle.Thickness = ".1 in"

    ' The name "Thickness" as used below is handled specially when the style
    ' is used so it will behave as expected for all languages.
    oStyle.BendRadius = "Thickness * 1.5"
    oStyle.BendReliefDepth = "Thickness * 1.5"
    oStyle.BendReliefShape = kRoundBendReliefShape
    oStyle.BendReliefWidth = "Thickness / 2"
    oStyle.BendTransition = kArcBendTransition
    oStyle.BendTransitionArcRadius = "Thickness * 2.0"
    oStyle.CornerReliefShape = kRoundCornerReliefShape
    oStyle.CornerReliefSize = "Thickness * 2.0"
    oStyle.MinimumRemnant = "Thickness * 2.0"

    ' Set the material.  For this example it arbitrarily uses the first material in the collection.
    oStyle.Material = oPartDoc.Materials.Item(1)

    oStyle.PunchRepresentationType = kFormedFeaturePunchRepresentation
    oStyle.ThreeBendCornerReliefShape = kFullRoundCornerReliefShape
    oStyle.ThreeBendCornerReliefSize = "Thickness * 2.0"

    ' Activate this style.
    oStyle.Activate

    ' This section will override some of the settings defined by the style.
    Dim bOverrideStyle As Boolean
    bOverrideStyle = True
    If bOverrideStyle Then
        ' Set the unfold method to use the unfold method created above.
        oSheetMetalCompDef.UnfoldMethod = okFactorUnfoldMethod

        ' Set the thickness.
        oSheetMetalCompDef.UseSheetMetalStyleThickness = False
        oSheetMetalCompDef.Thickness.Expression = ".12 in"

        ' Set the material.
        oSheetMetalCompDef.Material = oPartDoc.Materials.Item(2)
    End If
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |