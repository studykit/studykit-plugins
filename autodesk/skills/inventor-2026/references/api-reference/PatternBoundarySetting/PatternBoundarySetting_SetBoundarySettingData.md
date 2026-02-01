# PatternBoundarySetting.SetBoundarySettingData Method

Parent Object: [PatternBoundarySetting](../PatternBoundarySetting/PatternBoundarySetting.md)

## Description

Method that sets the boundary setting data.

## Syntax

PatternBoundarySetting.**SetBoundarySettingData**( ***Boundary*** As Variant, [***BoundaryInclusionType***] As Variant, [***OccurrenceBasePoint***] As Variant, [***Offset***] As Variant, [***OffsetFlipped***] As Variant, [***Reserved***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Boundary | Variant | Input object that specifies the boundary for the pattern feature. This can be a FaceCollection object containing planar Face objects or a Profile object. If a FaceCollection object is specified, all the planar Face objects should be co-planar. |
| BoundaryInclusionType | Variant | Optional input PatternBoundaryInclusionEnum that specifies the boundary inclusion type. If not provided the default kEnclosedGeometryInclusionType will be used. If set this to kOccurrenceBasePointInclusionType the OccurrenceBasePoint should be specified. |
| OccurrenceBasePoint | Variant | Optional input point to specify the occurrence base point position. This can be a WorkPoint, Vertex or GeometryIntent indicating the mid point of an edge or center of circular/elliptical edges. This is ignored if the BoundaryInclusionType is not set to kOccurrenceBasePointInclusionType.   This is an optional argument whose default value is null. |
| Offset | Variant | Optional input value to specify the offset. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a numeric value is input, the units are centimeters. If a String is input, the units can be specified as part of the string or it will default to the current length units of the document. If not provided this default to 0.   This is an optional argument whose default value is null. |
| OffsetFlipped | Variant | Optional input Boolean value that specifies whether the offset is flipped or not. If not provided this default to False and the boundary is shrunk based on the offset value. If set to True the boundary is grown based on the offset value.   This is an optional argument whose default value is null. |
| Reserved | Variant | Reserved argument for future use.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Pattern Feature with PatternBoundarySetting Sample](../../sample-programs/CreatePatternBoundarySettingSample_Sample.md) | This sample demonstrates how to create a rectangular pattern feature with boundary settings. |

## Version

Introduced in version 2025
