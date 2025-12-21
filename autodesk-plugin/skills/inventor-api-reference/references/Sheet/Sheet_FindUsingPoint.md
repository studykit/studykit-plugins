# Sheet.FindUsingPoint Method

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Method that finds drawing curve segments, entities on a sheet sketch, centerlines and centermarks that the given point lies on.

## Syntax

Sheet.**FindUsingPoint**( ***PointOnSheet*** As [Point2d](../Point2d/Point2d.md), [***ProximityTolerance***] As Variant ) As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOnSheet | [Point2d](../Point2d/Point2d.md) | Input Point2d object that specifies a sheet point. |
| ProximityTolerance | Variant | Input Double that specifies the tolerance value for the search. If not specified, the default internal tolerance is used. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |