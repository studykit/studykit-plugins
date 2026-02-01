# OriginIndicator Object

## Description

The OriginIndicator object represents an origin indicator for ordinate dimensions and hole tables placed on a drawing view.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../OriginIndicator/OriginIndicator_Delete.md) | Method that deletes this origin indicator. This fails if this origin indicator is referenced by ordinate dimensions or hole tables. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../OriginIndicator/OriginIndicator_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Attached](../OriginIndicator/OriginIndicator_Attached.md) | Property that specifies whether the origin indicator is attached to an origin point. |
| [Intent](../OriginIndicator/OriginIndicator_Intent.md) | Gets and sets the origin point to which the origin indicator is attached. Valid intent values are points that specify geometry to which the origin indicator can be attached. |
| [InUse](../OriginIndicator/OriginIndicator_InUse.md) | Read-only property that returns whether the origin indicator is used by any dimensions or tables. |
| [Layer](../OriginIndicator/OriginIndicator_Layer.md) | Gets and sets the layer associated with the origin indicator. |
| [LeaderStyle](../OriginIndicator/OriginIndicator_LeaderStyle.md) | Gets and sets the leader style associated with the origin indicator. The line format properties are the only properties of the leader style that are applicable to the origin indicator; other leader style properties have no effect on the origin indicator. |
| [RelativeX](../OriginIndicator/OriginIndicator_RelativeX.md) | Gets and sets the relative X coordinate of the origin indicator, this property will return a double value in centimeter units. When setting a value, the units of the specified value will be assumed to be centimeters. |
| [RelativeY](../OriginIndicator/OriginIndicator_RelativeY.md) | Gets and sets the relative Y coordinate of the origin indicator, this property will return a double value in centimeter units. When setting a value, the units of the specified value will be assumed to be centimeters. |
| [Type](../OriginIndicator/OriginIndicator_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../OriginIndicator/OriginIndicator_Visible.md) | Gets and sets whether the origin indicator should be hidden. |

## Accessed From

[DetailDrawingView.OriginIndicator](../DetailDrawingView/DetailDrawingView_OriginIndicator.md), [DrawingView.OriginIndicator](../DrawingView/DrawingView_OriginIndicator.md), [SectionDrawingView.OriginIndicator](../SectionDrawingView/SectionDrawingView_OriginIndicator.md)

## Version

Introduced in version 2009
