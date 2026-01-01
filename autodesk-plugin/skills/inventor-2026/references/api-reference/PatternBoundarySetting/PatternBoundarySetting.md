# PatternBoundarySetting Object

## Description

Pattern Boundary Settings object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../PatternBoundarySetting/PatternBoundarySetting_Copy.md) | Method that creates a copy of this PatternBoundarySetting object. |
| [GetBoundarySettingData](../PatternBoundarySetting/PatternBoundarySetting_GetBoundarySettingData.md) | Method that gets the boundary setting data. |
| [SetBoundarySettingData](../PatternBoundarySetting/PatternBoundarySetting_SetBoundarySettingData.md) | Method that sets the boundary setting data. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PatternBoundarySetting/PatternBoundarySetting_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Boundary](../PatternBoundarySetting/PatternBoundarySetting_Boundary.md) | Read-write property that gets and sets the boundary object for the pattern. This can be a FaceCollection object containing planar Face objects or a Profile object. |
| [BoundaryInclusionType](../PatternBoundarySetting/PatternBoundarySetting_BoundaryInclusionType.md) | Read-write property that gets and sets boundary inclusion type. Use the SetBoundarySettingData method when set this to kOccurrenceBasePointInclusionType so the OccurrenceBasePoint can be specified also. |
| [OccurrenceBasePoint](../PatternBoundarySetting/PatternBoundarySetting_OccurrenceBasePoint.md) | Read-write property that gets and sets the occurrence base point. This can be a WorkPoint, Vertex or GeometryIntent indicating the mid point of an edge or center of circular/elliptical edge. |
| [Offset](../PatternBoundarySetting/PatternBoundarySetting_Offset.md) | Read-write property that gets and sets the offset value for the pattern. |
| [OffsetFlipped](../PatternBoundarySetting/PatternBoundarySetting_OffsetFlipped.md) | Read-write property that gets and sets whether the offset is flipped or not. |
| [Type](../PatternBoundarySetting/PatternBoundarySetting_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[CircularPatternFeatureDefinition.BoundarySetting](../CircularPatternFeatureDefinition/CircularPatternFeatureDefinition_BoundarySetting.md), [PatternBoundarySetting.Copy](../PatternBoundarySetting/PatternBoundarySetting_Copy.md), [RectangularPatternFeatureDefinition.BoundarySetting](../RectangularPatternFeatureDefinition/RectangularPatternFeatureDefinition_BoundarySetting.md), [SketchCircularPatternDefinition.BoundarySetting](../SketchCircularPatternDefinition/SketchCircularPatternDefinition_BoundarySetting.md), [SketchRectangularPatternDefinition.BoundarySetting](../SketchRectangularPatternDefinition/SketchRectangularPatternDefinition_BoundarySetting.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Pattern Feature with PatternBoundarySetting Sample](../../sample-programs/CreatePatternBoundarySettingSample_Sample.md) | This sample demonstrates how to create a rectangular pattern feature with boundary settings. |

## Version

Introduced in version 2025
