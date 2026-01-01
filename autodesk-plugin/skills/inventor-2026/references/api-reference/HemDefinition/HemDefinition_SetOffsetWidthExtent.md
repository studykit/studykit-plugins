# HemDefinition.SetOffsetWidthExtent Method

Parent Object: [HemDefinition](../HemDefinition/HemDefinition.md)

## Description

Method that changes the HemDefinition object to define a hem whose width is defined with respect to two entities.

## Syntax

HemDefinition.**SetOffsetWidthExtent**( ***OffsetEntityOne*** As Object, ***OffsetDistanceOne*** As Variant, ***OffsetEntityTwo*** As Object, ***OffsetDistanceTwo*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| OffsetEntityOne | Object | Input Object that defines the first entity the distance is measured relative to. This can be a point (WorkPoint or a Vertex object) or a plane (Face or WorkPlane object that is perpendicular to the selected edge). |
| OffsetDistanceOne | Variant | Input Variant that defines the distance of the hem from offset entity one. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| OffsetEntityTwo | Object | Input Object that defines the second entity the distance is measured relative to. This can be a point (WorkPoint or a Vertex object) or a plane (Face or WorkPlane object that is perpendicular to the selected edge). |
| OffsetDistanceTwo | Variant | Input Variant that defines the distance of the hem from offset entity two. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2010
