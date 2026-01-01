# Sheet Metal Thickness Editing

## Description

This sample illustrates editing the thickness of a sheet metal part.

## Code Samples

* [VBA](#VBA)

```
Public Sub SetSheetMetalThickness()
    ' Set a reference to the sheet metal document.
    ' This assumes a sheet metal document is active.
    Dim oPartDoc As PartDocument
    Set oPartDoc = ThisApplication.ActiveDocument

    ' Get the sheet metal component definition. Because this is a part document whose
    ' sub type is sheet metal, the document will return a SheetMetalComponentDefinition
    ' instead of a PartComponentDefinition.
    Dim oSheetMetalCompDef As SheetMetalComponentDefinition
    Set oSheetMetalCompDef = oPartDoc.ComponentDefinition

    ' Override the thickness for the document
    oSheetMetalCompDef.UseSheetMetalStyleThickness = False

    ' Get a reference to the parameter controlling the thickness.
    Dim oThicknessParam As Parameter
    Set oThicknessParam = oSheetMetalCompDef.Thickness

    ' Change the value of the parameter.
    oThicknessParam.Value = oThicknessParam.Value * 1.5

    ' Update the part.
    ThisApplication.ActiveDocument.Update
End Sub
```
