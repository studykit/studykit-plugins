# FlangeDefinition.SetDistanceHeightExtent Method

Parent Object: [FlangeDefinition](../FlangeDefinition/FlangeDefinition.md)

## Description

Method that changes the FlangeDefinition object to define a flange whose height is measured by a distance.

## Syntax

FlangeDefinition.**SetDistanceHeightExtent**( ***Distance*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***HeightDatumType*** As [HeightDatumTypeEnum](../HeightDatumTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Distance | Variant | Input Variant that defines the distance used for the height extent of the flange. When the FlangeDefinition object is created it defaults to a distance height extent. This value is used to define that distance.  This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input value from PartFeatureExtentDirectionEnum that defines the direction of the flange. kPositiveExtentDirection indicates that the direction of the flange is on the side of the selected edge. kNegativeExtentDirection indicates the flange is on the opposite side of the select edge. kSymmetricExtentDirection is not valid for a flange direction. |
| HeightDatumType | [HeightDatumTypeEnum](../HeightDatumTypeEnum.md) | Input value from HeightDatumTypeEnum that defines how the height of the flange is defined. There are five options to define the height. Three of these are measured along the flange and two are measured in an orthogonal direction. These are illustrated in the figures below, along with the corresponding option as shown in the Flange dialog. In the examples below the flange distance is 1.00, the angle is 135.0 and the position of the bend is outside of the base face extents. |

## Version

Introduced in version 2011
