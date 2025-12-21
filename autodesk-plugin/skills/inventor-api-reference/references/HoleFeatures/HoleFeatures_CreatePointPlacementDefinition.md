# HoleFeatures.CreatePointPlacementDefinition Method

Parent Object: [HoleFeatures](../HoleFeatures/HoleFeatures.md)

## Description

Method that creates a new PointHolePlacementDefinition object that can be used for defining the placement of Hole features coincident with a work point and positioned with respect to an axis, edge or work plane.

## Syntax

HoleFeatures.**CreatePointPlacementDefinition**( ***Point*** As Object, ***Direction*** As Object ) As [PointHolePlacementDefinition](../PointHolePlacementDefinition/PointHolePlacementDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | Object | Object that specifies the point to set as the hole center. The only valid input is a WorkPoint. |
| Direction | Object | Object that specifies the direction of the hole axis. This can be a planar Face object or a WorkPlane object with which the axis of the hole is perpendicular, or an Edge or WorkAxis object with which the axis of the hole is parallel. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |