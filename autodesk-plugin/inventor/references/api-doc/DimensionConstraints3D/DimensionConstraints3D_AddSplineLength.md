# DimensionConstraints3D.AddSplineLength Method

Parent Object: [DimensionConstraints3D](../DimensionConstraints3D/DimensionConstraints3D.md)

## Description

Method that creates a new spline length dimension constraint that defines the length of a 3D sketch spline.

## Syntax

DimensionConstraints3D.**AddSplineLength**( ***SketchSpline*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md), [***TextPoint***] As Variant, [***Driven***] As Boolean ) As [SplineLengthDimConstraint3D](../SplineLengthDimConstraint3D/SplineLengthDimConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchSpline | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | Input SketchSpline3D object that specifies a 3D sketch spline to add dimension constraint to. Currently only the SkechSpline3D is supported to add this dimension, other 3D sketch splines are not supported yet. |
| TextPoint | Variant | Optional input Point object that defines the position of the dimension text. If no input is specified for the position of the dimension text, a default position on the dimension plane will be calculated and used to place the dimension text. If a valid point for the dimension text is specified, then either of the following conditions will apply:  * If the specified point already lies on the dimension plane, then this point will be directly used to place the dimension text. * If the specified point does not lie on the dimension plane, it will be projected onto the dimension plane. Therefore, the resultant placement position for the dimension text will be different from the specified one. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |