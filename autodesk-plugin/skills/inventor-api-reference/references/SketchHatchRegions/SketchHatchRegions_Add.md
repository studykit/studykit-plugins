# SketchHatchRegions.Add Method

Parent Object: [SketchHatchRegions](../SketchHatchRegions/SketchHatchRegions.md)

## Description

Method that creates a new SketchHatchRegion. The new created SketchHatchRegion is returned.

## Syntax

SketchHatchRegions.**Add**( ***Profile*** As [Profile](../Profile/Profile.md), [***DrawingHatchPattern***] As Variant, [***Angle***] As Variant, [***Scale***] As Variant, [***Shift***] As Variant, [***LineWeight***] As Variant, [***DoublePattern***] As Variant, [***Color***] As Variant ) As [SketchHatchRegion](../SketchHatchRegion/SketchHatchRegion.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object that being hatched. |
| DrawingHatchPattern | Variant | Optional input DrawingHatchPattern that specifies the hatch pattern. If this is left empty, the default pattern will be used for the sketch hatch region. If not provided the “ANSI 31” will be used. The “Solid” pattern can be used to set the color fill region. |
| Angle | Variant | Optional input Double that defines the rotation angle of the hatch pattern in radians.   This is an optional argument whose default value is null. |
| Scale | Variant | Optional input Double that indicates the scale factor when applying the pattern.   This is an optional argument whose default value is null. |
| Shift | Variant | Optional input Double that specifies the distance to offset the hatch original hatch pattern position.   This is an optional argument whose default value is null. |
| LineWeight | Variant | Optional input Double that specifies the line weight in centimeters. A value of 0 indicates By Layer.   This is an optional argument whose default value is null. |
| DoublePattern | Variant | Optional input Boolean that specifies if a duplicate hatch pattern should be created that is perpendicular to the hatch pattern assigned to the sketch hatch region.   This is an optional argument whose default value is null. |
| Color | Variant | Optional input Color object that specifies the color for hatch pattern. A value of Nothing indicates that the layer color should be used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Drawing Sketch Hatch Region Sample](../../sample-programs/DrawingSketchHatchRegionSample_Sample.md) | This sample demonstrates how to create a sketch hatch region in drawing. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |