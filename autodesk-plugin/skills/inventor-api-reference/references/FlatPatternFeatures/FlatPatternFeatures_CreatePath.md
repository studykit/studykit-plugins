# FlatPatternFeatures.CreatePath Method

Parent Object: [FlatPatternFeatures](../FlatPatternFeatures/FlatPatternFeatures.md)

## Description

Method that creates a path used to define the shape of several part features such as sweep, rectangular pattern, split, etc. All other 2D and 3D curves that are connected to the input curve are obtained and used to create a Path object. The new Path is returned.

## Syntax

FlatPatternFeatures.**CreatePath**( ***SketchCurve*** As Object ) As [Path](../Path/Path.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchCurve | Object | Input sketch (planar or 3D) entity. This can be any entity that is part of the desired path. All curves that are end point connected will be found and used to create the path. |

## Version

Introduced in version 2010
