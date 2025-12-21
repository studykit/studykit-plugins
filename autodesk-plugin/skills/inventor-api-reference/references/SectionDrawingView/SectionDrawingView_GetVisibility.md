# SectionDrawingView.GetVisibility Method

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Method that gets the visibility of the input object in the drawing view. This returns error if the input object has partial visibility status.

## Syntax

SectionDrawingView.**GetVisibility**( ***Object*** As Object ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Object | Object | Input object to get the visibility state of. Valid objects are 2d and 3d sketches, work features, surface features, occurrences and proxies for all of these. The object needs to be supplied in the context of the document referenced by the drawing view. For instance, to set the visibility state of a 3D sketch within a part instanced in an assembly (and the drawing view is of the assembly), the input should be a Sketch3DProxy object created in context of the assembly. An error will occur if no corresponding object exists in the drawing view. |

## Version

Introduced in version 10
