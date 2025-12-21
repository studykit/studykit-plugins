# FlangeEdgeSet.SetCenteredWidthExtent Method

Parent Object: [FlangeEdgeSet](../FlangeEdgeSet/FlangeEdgeSet.md)

## Description

Method that sets the width extent of the specified physical flange to define a flange that’s centered along the edge and has a defined width.

## Syntax

FlangeEdgeSet.**SetCenteredWidthExtent**( ***Width*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Width | Variant | Input Variant that defines the distance used for the width extent of the flange.  This value is used to define that distance. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2025
