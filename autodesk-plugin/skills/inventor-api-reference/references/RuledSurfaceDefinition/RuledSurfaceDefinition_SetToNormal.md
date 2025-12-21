# RuledSurfaceDefinition.SetToNormal Method

Parent Object: [RuledSurfaceDefinition](../RuledSurfaceDefinition/RuledSurfaceDefinition.md)

## Description

Method that sets ruled surface to normal to face type.

## Syntax

RuledSurfaceDefinition.**SetToNormal**( ***GeneratrixCurves*** As [RuledSurfaceEdgeFacePairs](../RuledSurfaceEdgeFacePairs/RuledSurfaceEdgeFacePairs.md), ***Distance*** As Variant, [***FlipExtendDirection***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeneratrixCurves | [RuledSurfaceEdgeFacePairs](../RuledSurfaceEdgeFacePairs/RuledSurfaceEdgeFacePairs.md) | Input RuledSurfaceEdgeFacePairs object containing the edges base on which to create the ruled surface. The edges should be connected end-to-end with each other. |
| Distance | Variant | Input Variant that defines the length of the ruled surface. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| FlipExtendDirection | Boolean | Optional input Boolean that specifies whether flip the extend direction or not. |

## Version

Introduced in version 2016
