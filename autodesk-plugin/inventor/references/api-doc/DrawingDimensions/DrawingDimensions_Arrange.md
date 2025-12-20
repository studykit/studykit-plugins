# DrawingDimensions.Arrange Method

Parent Object: [DrawingDimensions](../DrawingDimensions/DrawingDimensions.md)

## Description

Method that automatically arranges the input drawing dimensions.

## Syntax

DrawingDimensions.**Arrange**( ***DrawingDimensions*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***ContourEntity***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DrawingDimensions | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the drawing dimensions to arrange. The collection can contains dimensions from different drawing views. The collection can contain DrawingDimension and ChainDimensionSet objects. The input DrawingDimension objects should not be a member of an ordinate dimension set, a baseline dimension set or a chain dimension set. |
| ContourEntity | Variant | Optional input object that specifies a contour entity to use for dimension arrangement. This can either be a GeometryIntent object (which specifies a geometry) or a Point2d object (which specifies a 2d point in sheet space). This argument is applicable only when all the input dimension objects are along an axis (i.e. they are parallel). |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |