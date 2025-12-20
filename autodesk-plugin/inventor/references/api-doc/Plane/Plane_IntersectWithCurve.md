# Plane.IntersectWithCurve Method

Parent Object: [Plane](../Plane/Plane.md)

## Description

Gets the intersection points of the Plane and the input curve. Note that 3D transient geometry should be supplied. Obtain 3D transient geometry from any sktech entities or 2D geometry before calling this method (for example, by calling the Geometry method of the entity).

## Syntax

Plane.**IntersectWithCurve**( ***Curve*** As Object, [***Tolerance***] As Double ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input object that represents a Curve. |
| Tolerance | Double | Input Double that specifies the tolerance. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |