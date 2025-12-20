# SketchArcs3D.AddAsBend Method

Parent Object: [SketchArcs3D](../SketchArcs3D/SketchArcs3D.md)

## Description

Method that creates a new bend feature based on the two input lines.

## Syntax

SketchArcs3D.**AddAsBend**( ***LineOne*** As [SketchLine3D](../SketchLine3D/SketchLine3D.md), ***LineTwo*** As [SketchLine3D](../SketchLine3D/SketchLine3D.md), [***BendRadius***] As Variant ) As [SketchArc3D](../SketchArc3D/SketchArc3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LineOne | [SketchLine3D](../SketchLine3D/SketchLine3D.md) | Input 3D sketch line. Note that LineOne and LineTwo should be constrained end to end. |
| LineTwo | [SketchLine3D](../SketchLine3D/SketchLine3D.md) | Input 3D sketch line. Note that LineOne and LineTwo should be constrained end to end. |
| BendRadius | Variant | Optional input variant that defines the radius of the bend. If not supplied the auto bend radius defined in the document options is used. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |