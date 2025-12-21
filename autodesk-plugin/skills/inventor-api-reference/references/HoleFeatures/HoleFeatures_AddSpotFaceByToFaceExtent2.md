# HoleFeatures.AddSpotFaceByToFaceExtent2 Method

Parent Object: [HoleFeatures](../HoleFeatures/HoleFeatures.md)

## Description

Creates a new SpotFace HoleFeature using to face extents.

## Syntax

HoleFeatures.**AddSpotFaceByToFaceExtent2**( ***PlacementDefinition*** As Object, ***DiameterOrTapInfo*** As Variant, ***ToFace*** As Object, ***ExtendToFace*** As Boolean, ***SpotFaceDiameter*** As Variant, ***SpotFaceDepth*** As Variant, [***DrillPointType***] As Variant, [***BottomTipAngle***] As Variant ) As [HoleFeature](../HoleFeature/HoleFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PlacementDefinition | Object | Object that defines the centerpoint(s) of the hole feature. This object can be one of the following four objects that derive from the HolePlacementDefinition object: SketchHolePlacementDefinition, LinearHolePlacementDefinition, ConcentricHolePlacementDefinition, PointHolePlacementDefinition. These objects can be created using methods provided on this HoleFeatures object. This argument also supports an ObjectCollection of SketchPoints for compatibility with the older version of this method. |
| DiameterOrTapInfo | Variant | Defines either the diameter of the hole or the tap information (using a HoleTapInfo object). In the case of a tapped hole, the tap information defines the diameter of the hole. When the diameter is supplied, this can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ToFace | Object | Input Object that defines the 'to face.' This can be either a or WorkPlane object. |
| ExtendToFace | Boolean | Input Boolean that defines whether the 'to face' should be extended to contain the extents of the hole. |
| SpotFaceDiameter | Variant | Input Variant that defines the diameter of the spotface. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| SpotFaceDepth | Variant | Input Variant that defines the depth of the spotface. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| DrillPointType | Variant | Optional input HoleDrillPointTypeEnum that specifies the drill point of the hole. If specifies an angled drill point then the BottomTipAngle argument needs to be provided to specify the angle. The default value is kFlatDrillPointType. |
| BottomTipAngle | Variant | Optional input Variant that defines the angle of the tip at the bottom of a hole. This argument is only used when the DrillPointType argument is kAngledDrillPointType, kAngledVDrillPointType or kAngledYDrillPointType. If this argument is not supplied a default value of 118 degrees is assigned.    This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |