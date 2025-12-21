# ContourFlangeDefinition.SetToExtent Method

Parent Object: [ContourFlangeDefinition](../ContourFlangeDefinition/ContourFlangeDefinition.md)

## Description

Method that sets the width extent to define a contour flange whose width is defined as being between original sketch plane and another entity. This is applicable when the WidthExtentsFromSketchPlane is True or when Operation is kJoinOperation.

## Syntax

ContourFlangeDefinition.**SetToExtent**( ***ToEntity*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToEntity | Object | Input Object that defines the “to” extents. This can be a planar Face or WorkPlane that is parallel to the original sketch plane.. |

## Version

Introduced in version 2026
