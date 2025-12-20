# SketchLines.AddAsPolygon Method

Parent Object: [SketchLines](../SketchLines/SketchLines.md)

## Description

Method that creates a polygon with up to 120 sides. The sketch lines representing the polygon are returned.

## Syntax

SketchLines.**AddAsPolygon**( ***NumberOfSides*** As Long, ***CenterPoint*** As Object, ***CircumferencePoint*** As Object, ***Inscribed*** As Boolean ) As [SketchEntitiesEnumerator](../SketchEntitiesEnumerator/SketchEntitiesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| NumberOfSides | Long | Input Long that specifies the number of sides of the polygon. If a value lesser than 3 or greater than 120 is provided, the method returns an error. |
| CenterPoint | Object | Input object that specifies the center of the polygon. This can either be a SketchPoint or a Point2d object. |
| CircumferencePoint | Object | Input object that specifies a point on the circumference of the circle that inscribes or circumscribes the polygon. This can either be a SketchPoint or a Point2d object. |
| Inscribed | Boolean | Input Boolean that specifies whether the specified CircumferencePoint is on a circle that inscribes or circumscribes the polygon. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |