# Create or update custom iProperty

## Description

This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample.

## Code Samples

* [VBA](#VBA)

```
Public Sub UpdateVolume()
    ' Get the active part document.
    Dim invPartDoc As PartDocument
    Set invPartDoc = ThisApplication.ActiveDocument

    ' Get the volume of the part. This will be returned in
    ' cubic centimeters.
    Dim dVolume As Double
    dVolume = invPartDoc.ComponentDefinition.MassProperties.Volume

    ' Get the UnitsOfMeasure object which is used to do unit conversions.
    Dim oUOM As UnitsOfMeasure
    Set oUOM = invPartDoc.UnitsOfMeasure

    ' Convert the volume to the current document units.
    Dim strVolume As String
    strVolume = oUOM.GetStringFromValue(dVolume, oUOM.GetStringFromType(oUOM.LengthUnits) & "^3")

    ' Get the custom property set.
    Dim invCustomPropertySet As PropertySet
    Set invCustomPropertySet = invPartDoc.PropertySets.Item("Inventor User Defined Properties")

    ' Attempt to get an existing custom property named "Volume".
    On Error Resume Next
    Dim invVolumeProperty As Property
    Set invVolumeProperty = invCustomPropertySet.Item("Volume")
    If Err.Number <> 0 Then
        ' Failed to get the property, which means it doesn't exist
        ' so we'll create it.
        Call invCustomPropertySet.Add(strVolume, "Volume")
    Else
        ' Got the property so update the value.
        invVolumeProperty.value = strVolume
    End If
End Sub
```
