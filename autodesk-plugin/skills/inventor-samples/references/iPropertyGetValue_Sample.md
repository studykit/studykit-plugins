# Get value of iProperty

## Description

Demonstrates getting the values of the "Part Number" iProperty. Any property can be retrieved by accesing the correct property set and property.

A document must be open when this sample is run.

## Code Samples

* [VBA](#VBA)

```
Public Sub GetPropertySample()
    ' Get the active document.
    Dim invDoc As Document
    Set invDoc = ThisApplication.ActiveDocument

    ' Get the design tracking property set.
    Dim invDesignInfo As PropertySet
    Set invDesignInfo = invDoc.PropertySets.Item("Design Tracking Properties")

    ' Get the part number property.
    Dim invPartNumberProperty As Property
    Set invPartNumberProperty = invDesignInfo.Item("Part Number")

    MsgBox "Part Number: " & invPartNumberProperty.value
End Sub
```
