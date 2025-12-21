# TransientGeometry.CreateCone Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Cone object. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateCone**( ***RootPoint*** As [Point](../Point/Point.md), ***Axis*** As [UnitVector](../UnitVector/UnitVector.md), ***Radius*** As Double, ***HalfAngle*** As Double, ***IsExpanding*** As Boolean ) As [Cone](../Cone/Cone.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RootPoint | [Point](../Point/Point.md) | Input Point object that specifies the base of the cone. |
| Axis | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object that specifies the direction of the axis of the cone. |
| Radius | Double | Input Double that specifies the radius of the cone at the base point. |
| HalfAngle | Double | Input Double that specifies the taper angle of the cone. This is the angle measured from the axis to the side of the cone. |
| IsExpanding | Boolean | Input Boolean that if the taper of the cone is expanding outwards or inwards in the direction of the axis vector. If True and the HalfAngle is positive, then the cone is expanding outward along the axis vector. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |