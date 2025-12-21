# ExtrudeDefinition.SetDistanceFromFaceExtent Method

Parent Object: [ExtrudeDefinition](../ExtrudeDefinition/ExtrudeDefinition.md)

## Description

Method that changes the extents to be “Distance From Face” extents.

## Syntax

ExtrudeDefinition.**SetDistanceFromFaceExtent**( ***FromFace*** As Object, ***ExtendFromFace*** As Boolean, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***Distance*** As Variant, [***IsTwoDirectional***] As Variant, [***DistanceTwo***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FromFace | Object | Input object that indicates from which to do the offset extrusion. This can be a Face or WorkPlane object. |
| ExtendFromFace | Boolean | Input Boolean that defines whether the “from face” should be extended to contain the extents of the profile. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input PartFeatureExtentDirectionEnum that defines the distance direction of the feature. Valid input is kPositiveExtentDirection, kNegativeExtentDirection, or kSymmetricExtentDirection. kPositiveExtentDirection defines the offset direction to be in the same direction as the normal of the sketch plane. |
| Distance | Variant | Input Variant that defines the length of the extrusion. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| IsTwoDirectional | Variant | Optional input Boolean that indicates if the extents have been defined in two directions for the extrusion. This is ignored if the ExtentDirection is set to kSymmetricExtentDirection. This defaults to False if not specified. |
| DistanceTwo | Variant | Optional input Variant that defines the length of the extrusion in the other direction for an asymmetric extrude. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. This is ignored if the IsTwoDirectional is set to False, otherwise this is required to specify the distance for the extrusion in the other direction for an asymmetric extrude.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2019
