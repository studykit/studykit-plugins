# ContourFlangeDefinition.SetFromToExtent Method

Parent Object: [ContourFlangeDefinition](../ContourFlangeDefinition/ContourFlangeDefinition.md)

## Description

Method that sets the width extent to define a contour flange whose width is defined as being between two entities. Calling this method will set WidthExtentsFromSketchPlane to True when the Operation is kJoinOperation.

## Syntax

ContourFlangeDefinition.**SetFromToExtent**( ***FromEntity*** As Object, ***ToEntity*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromEntity | Object | Input Object that defines the “from” extents. This can be a planar Face or WorkPlane, object that is parallel to the original sketch plane. |
| ToEntity | Object | Input Object that defines the “to” extents. This can be a planar Face or WorkPlane that is parallel to the original sketch plane. |

## Version

Introduced in version 2026

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |