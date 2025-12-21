# ThickenFeatures.Add Method

Parent Object: [ThickenFeatures](../ThickenFeatures/ThickenFeatures.md)

## Description

Method that creates a new ThickenFeature. The new created ThickenFeature is returned.

## Syntax

ThickenFeatures.**Add**( ***Faces*** As Object, ***Distance*** As Variant, ***ExtentDirection*** As [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md), ***Operation*** As [PartFeatureOperationEnum](../PartFeatureOperationEnum.md), [***AutomaticFaceChain***] As Boolean, [***CreateVerticalSurfaces***] As Boolean, [***AutomaticBlending***] As Boolean ) As [ThickenFeature](../ThickenFeature/ThickenFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Faces | Object | Input object that defines the faces to thicken or faces from which to create an offset surface. This can either be a WorkSurface or a FaceCollection. If multiple faces are provided, they must be connected. |
| Distance | Variant | Input Variant that defines the thickness of the Thicken feature or specifies distance for the Offset feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. When the output is a surface, the offset distance can be zero. |
| ExtentDirection | [PartFeatureExtentDirectionEnum](../PartFeatureExtentDirectionEnum.md) | Input constant that indicates which side of the input faces to thicken or offset towards. Valid input is kPositive, kNegative, or kSymmetric. kPositive defines the offset direction to be in the same direction as the normal of the input faces. |
| Operation | [PartFeatureOperationEnum](../PartFeatureOperationEnum.md) | Input constant that indicates the type of operation to perform. Valid \input is kJoinOperation, kCutOperation, kIntersectOperation, or kSurfaceOperation. |
| AutomaticFaceChain | Boolean | Optional input Boolean that specifies whether or not to perform chaining of tangent continuous faces. The default value is False indicating that automatic chaining will not be performed. |
| CreateVerticalSurfaces | Boolean | Optional input Boolean that specifies whether or not to create vertical or "side" faces connecting the offset faces to the original work surface. Vertical surfaces are created only at internal surface edges, not at boundary edges of surfaces. The default value is False.   This is an optional argument whose default value is False. |
| AutomaticBlending | Boolean | Optional input Boolean that specifies whether or not to perform automatic blending or not. The default value is False.   This is an optional argument whose default value is False. |

## Version

Introduced in version 9
