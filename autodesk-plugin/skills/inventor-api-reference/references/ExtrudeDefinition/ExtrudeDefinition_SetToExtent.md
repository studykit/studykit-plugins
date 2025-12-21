# ExtrudeDefinition.SetToExtent Method

Parent Object: [ExtrudeDefinition](../ExtrudeDefinition/ExtrudeDefinition.md)

## Description

Method that changes the extents to be “to entity” extents.

## Syntax

ExtrudeDefinition.**SetToExtent**( ***ToEntity*** As Object, [***ExtendToFace***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToEntity | Object | Input Object that defines the “to entity”.  This can be one of the following types:  * Planar entity: Face or WorkPlane object. * Point entity: Vertex, SketchPoint, SketchPoint3D, WorkPoint or Edge object.   If an Edge object is specified, only its mid-point will be used as input. If other points (e.g. start point or end point) of the edge need to be used as input, they have to be specified using the corresponding Vertex object. |
| ExtendToFace | Boolean | Optional Input Boolean that defines whether the plane defined by the “to entity” should be extended to contain the extents of the profile.  This argument is applicable only if the ToEntity argument is a Face. If no value is explicitly specified, a default value of False will be assumed.  If the ToEntity argument is not a Face, this argument will be ignored.    This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |

## Version

Introduced in version 2012
