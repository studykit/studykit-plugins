# GeometricConstraints3D.AddCustom Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new custom constraint on the input sketch entity.

## Syntax

GeometricConstraints3D.**AddCustom**( ***Entity*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md), ***ClientId*** As String ) As [CustomConstraint3D](../CustomConstraint3D/CustomConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | SketchEntity3D object that specifies the entity to which the custom constraint needs to be applied. |
| ClientId | String | String that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |

## Version

Introduced in version 11
