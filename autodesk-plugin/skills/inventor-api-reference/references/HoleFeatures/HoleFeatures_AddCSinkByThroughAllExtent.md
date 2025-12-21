# HoleFeatures.AddCSinkByThroughAllExtent Method

Parent Object: [HoleFeatures](../HoleFeatures/HoleFeatures.md)

## Description

Method that creates a new counter sink HoleFeature using 'through all' extents. The new HoleFeature is returned.

## Syntax

HoleFeatures.**AddCSinkByThroughAllExtent**( ***PlacementDefinition*** As Object, ***DiameterOrTapInfo*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***CSinkDiameter*** As Variant, ***CSinkAngle*** As Variant ) As [HoleFeature](../HoleFeature/HoleFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PlacementDefinition | Object | Object that defines the centerpoint(s) of the hole feature. This object can be one of the following four objects that derive from the HolePlacementDefinition object: SketchHolePlacementDefinition, LinearHolePlacementDefinition, ConcentricHolePlacementDefinition, PointHolePlacementDefinition. These objects can be created using methods provided on this HoleFeatures object. This argument also supports an ObjectCollection of SketchPoints for compatibility with the older version of this method. |
| DiameterOrTapInfo | Variant | Defines either the diameter of the hole or the tap information (using a HoleTapInfo or a TaperedThreadInfo object). In the case of a tapped hole, the tap information defines the diameter of the hole. When the diameter is supplied, this can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude toward. Valid input is kPositive or kNegative. kPositive defines the offset direction to be in the same direction as the normal of the sketch plane. |
| CSinkDiameter | Variant | Input Variant that defines the diameter of the countersink. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| CSinkAngle | Variant | Input Variant that defines the angle of the countersink. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Version

Introduced in version 5
