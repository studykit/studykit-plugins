# HoleFeatures.AddCSinkByDistanceExtent2 Method

Parent Object: [HoleFeatures](../HoleFeatures/HoleFeatures.md)

## Description

Method that creates a new countersink HoleFeature using distance extents. The new HoleFeature is returned.

## Syntax

HoleFeatures.**AddCSinkByDistanceExtent2**( ***PlacementDefinition*** As Object, ***DiameterOrTapInfo*** As Variant, ***Depth*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***CSinkDiameter*** As Variant, ***CSinkAngle*** As Variant, [***DrillPointType***] As Variant, [***BottomTipAngle***] As Variant ) As [HoleFeature](../HoleFeature/HoleFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PlacementDefinition | Object | Object that defines the centerpoint(s) of the hole feature. This object can be one of the following four objects that derive from the HolePlacementDefinition object: SketchHolePlacementDefinition, LinearHolePlacementDefinition, ConcentricHolePlacementDefinition, PointHolePlacementDefinition. These objects can be created using methods provided on this HoleFeatures object. This argument also supports an ObjectCollection of SketchPoints for compatibility with the older version of this method. |
| DiameterOrTapInfo | Variant | Defines either the diameter of the hole or the tap information (using a HoleTapInfo object). In the case of a tapped hole, the tap information defines the diameter of the hole. When the diameter is supplied, this can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. |
| Depth | Variant | Input Variant that defines the depth of the hole. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the sketch plane to extrude toward. Valid input is kPositive or kNegative. kPositive defines the offset direction to be in the same direction as the normal of the sketch plane. |
| CSinkDiameter | Variant | Input Variant that defines the diameter of the countersink. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or it will default to the current length units of the document. |
| CSinkAngle | Variant | Input Variant that defines the angle of the countersink. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |
| DrillPointType | Variant | Optional input HoleDrillPointTypeEnum that specifies the drill point of the hole. If specifies an angled drill point then the BottomTipAngle argument needs to be provided to specify the angle. The default value is kFlatDrillPointType. |
| BottomTipAngle | Variant | Optional input Variant that defines the angle of the tip at the bottom of a hole. This argument is only used when the DrillPointType argument is kAngledDrillPointType, kAngledVDrillPointType or kAngledYDrillPointType. If this argument is not supplied a default value of 118 degrees is assigned.    This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |