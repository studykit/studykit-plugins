# RefoldFeatures.Add Method

Parent Object: [RefoldFeatures](../RefoldFeatures/RefoldFeatures.md)

## Description

Method that creates a new refold feature.

## Remarks

For most models the Face specified in the StationaryFace parameter must be on the top or bottom of the part, not around the edge. The exception to this is a part where all of the faces on the top and bottom of the part are cylindrical, as shown below.

![](../images/RefoldFeatures_Add1.png)

When using the Refold command in the user interface for parts like this, the user must specify one of the ends. The user interface displays what looks like work planes at each end of the part, as shown below, for the user to select. When using the API you must supply the equivalent Face objects at the end of the part.

![](../images/RefoldFeatures_Add2.png)

## Syntax

RefoldFeatures.**Add**( ***StationaryFace*** As [Face](../Face/Face.md), [***Bends***] As Variant, [***Sketches***] As Variant ) As [RefoldFeature](../RefoldFeature/RefoldFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StationaryFace | [Face](../Face/Face.md) | Input Face object that specifies the geometry that will remain fixed while other geometry refolds. See Remarks. |
| Bends | Variant | Optional input ObjectCollection that defines the bend(s) to refold. The bends specified must be in an unfolded state (IsFlat equals True). Not providing this argument or inputting Nothing indicates that all flat bends are to be refolded. |
| Sketches | Variant | Optional input ObjectCollection that specifies any sketches to be copied and transformed as part of the folding operation. The input sketches must be a child of one of the faces being folded. Also only one sketch per folded face is allowed.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
