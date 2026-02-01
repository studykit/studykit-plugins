# RuledSurfaceDefinition.SetToSweep Method

Parent Object: [RuledSurfaceDefinition](../RuledSurfaceDefinition/RuledSurfaceDefinition.md)

## Description

Method that sets ruled surface to sweep type.

## Syntax

RuledSurfaceDefinition.**SetToSweep**( ***GeneratrixCurves*** As Object, ***Distance*** As Variant, ***Vector*** As Object, [***FlipExtendDirection***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeneratrixCurves | Object | Input RuledSurfaceEdgeFacePairs object containing edge face pairs that the edges are connected end-to-end with each other, or Path object containing the 2D/3D sketch curves. |
| Distance | Variant | Input Variant that defines the length of the ruled surface. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| Vector | Object | Input object that defines the extend direction of ruled surface. Valid inputs are Edge, Face, WorkAxis, WorkPlane, SketchLine, and SketchLine3D. |
| FlipExtendDirection | Boolean | Optional input Boolean that specifies whether flip the extend direction or not. |

## Version

Introduced in version 2016
