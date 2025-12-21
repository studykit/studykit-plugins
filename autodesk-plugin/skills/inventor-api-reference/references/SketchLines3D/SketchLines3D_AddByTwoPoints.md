# SketchLines3D.AddByTwoPoints Method

Parent Object: [SketchLines3D](../SketchLines3D/SketchLines3D.md)

## Description

Method that creates a new sketch line based on the two input points. The new sketch line is returned.

## Syntax

SketchLines3D.**AddByTwoPoints**( ***StartPoint*** As Object, ***EndPoint*** As Object, [***UseAutoBend***] As Boolean, [***BendRadius***] As Variant ) As [SketchLine3D](../SketchLine3D/SketchLine3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input object that defines the start point of the line. This can be either a vertex object, a workpoint, a SketchPoint, or an existing SketchPoint3D object. If an existing sketch point is input, that point becomes the line's start point. |
| EndPoint | Object | Input object that defines the end point of the line. This can be either a vertex object, a workpoint, a SketchPoint, or an existing SketchPoint3D object. If an existing sketch point is input, that point becomes the line's end point. |
| UseAutoBend | Boolean | Optional input Boolean that indicates whether a bend should be automatically applied if the StartPoint or the EndPoint is shared by another sketch line. The default is True, which means that the bend will be automatically applied. |
| BendRadius | Variant | Optional input variant that defines the radius of the auto-bend. If the UseAutoBend flag is set to true and this variant is not supplied, a default value is used for the bend radius. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a 3D sketch dimension](../../sample-programs/DimensionConstraints3D_AddTwoPointDistance_Sample.md) | This sample demonstrates the creation of a 3d sketch line and a dimension between the start and the end points of the line. |
| [Loft Feature With Non-Planar Section](../../sample-programs/LoftFeature_Sample.md) | This sample demonstrates the creation of a loft feature. It uses two sections for the loft, one is from a 2d sketch and the other is a non-planar section from a 3d sketch. Because one of the sketches isn't planar, a surface is created instead of a solid. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |