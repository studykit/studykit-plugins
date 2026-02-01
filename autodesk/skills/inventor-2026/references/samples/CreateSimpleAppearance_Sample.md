# Create a simple appearance.

## Description

Creates a sample appearance in the active part or assembly document.

## Code Samples

* [VBA](#VBA)

```
Public Sub CreateSimpleColorAppearance()
    Dim doc As Document
    Set doc = ThisApplication.ActiveDocument

    ' Only document appearances can be edited, so that's what's created.
    ' This assumes a part or assembly document is active.
    Dim docAssets As Assets
    Set docAssets = doc.Assets

    ' Create a new appearance asset.
    Dim appearance As Asset
    Set appearance = docAssets.Add(kAssetTypeAppearance, "Generic", _
                                    "MyShinyRed", "My Shiny Red Color")

    Dim tobjs As TransientObjects
    Set tobjs = ThisApplication.TransientObjects

    Dim color As ColorAssetValue
    Set color = appearance.Item("generic_diffuse")
    color.value = tobjs.CreateColor(255, 15, 15)

    Dim floatValue As FloatAssetValue
    Set floatValue = appearance.Item("generic_reflectivity_at_0deg")
    floatValue.value = 0.5

    Set floatValue = appearance.Item("generic_reflectivity_at_90deg")
    floatValue.value = 0.5
End Sub
```
