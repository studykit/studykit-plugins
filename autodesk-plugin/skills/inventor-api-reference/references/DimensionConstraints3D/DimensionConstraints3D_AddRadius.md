# DimensionConstraints3D.AddRadius Method

Parent Object: [DimensionConstraints3D](../DimensionConstraints3D/DimensionConstraints3D.md)

## Description

Method that creates a new radius dimension constraint on the input circle or arc.

## Remarks

The picture below illustrates the result of adding an arc dimension constraint.

![](../Images/DimensionConstraints3D_AddRadius.png)

## Syntax

DimensionConstraints3D.**AddRadius**( ***Entity*** As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md), [***TextPoint***] As Variant, [***Driven***] As Boolean ) As [RadiusDimConstraint3D](../RadiusDimConstraint3D/RadiusDimConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md) | Input SketchCircle3D or SketchArc3D object. |
| TextPoint | Variant | The dimension text can only be placed on the plane that contains the two input sketch lines to which the dimension is being applied. The orientation of this dimension plane will be automatically determined using the input sketch lines. The dimension plane is a transient geometric plane which is only used to define the placement plane for the dimension text and does not have a graphical representation. The position of the text point defines which of the four quadrants on the dimension plane the constraint is placed within.  If no input is specified for the position of the dimension text, a default position on the dimension plane will be calculated and used to place the dimension text.  If a valid point for the dimension text is specified, then either of the following conditions will apply: \* If the specified point already lies on the dimension plane, then this point will be directly used to place the dimension text. \* If the specified point does not lie on the dimension plane, it will be projected onto the dimension plane. Therefore, the resultant placement position for the dimension text will be different from the specified one. The GetDimensionPlane method of the DimensionConstraints3D object can be used to get the dimension plane object which provides access to the dimension plane geometry. |
| Driven | Boolean | Optional input Boolean that specifies whether the dimension should be a driven or driving dimension. The default value is False, which causes a driving dimension constraint to be created.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |