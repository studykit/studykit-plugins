# GeneralDimensions Object

## Description

The GeneralDimensions collection object provides access to all of the general dimensions ( objects) on the sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAngular](../GeneralDimensions/GeneralDimensions_AddAngular.md) | Method that creates an angular dimension. Valid intent combinations are Three points, Two non-parallel linear curves, One arc curve. |
| [AddAngularForeshortened](../GeneralDimensions/GeneralDimensions_AddAngularForeshortened.md) | Creates an angular foreshortened dimension on the drawing sheet. |
| [AddArcLengthForeshortened](../GeneralDimensions/GeneralDimensions_AddArcLengthForeshortened.md) | Creates an arc length foreshortened dimension on the drawing sheet. |
| [AddDiameter](../GeneralDimensions/GeneralDimensions_AddDiameter.md) | Method that creates a diameter dimension. |
| [AddLinear](../GeneralDimensions/GeneralDimensions_AddLinear.md) | Method that creates a linear dimension. Valid intent combinations are: Two points, Two curves, Point and a curve, One linear curve, One arc curve (with DimensionType set to kAlignedDimensionType for chord length and kArcLengthDimensionType for arc length). |
| [AddLinear2](../GeneralDimensions/GeneralDimensions_AddLinear2.md) | Creates a linear dimension on the drawing sheet. |
| [AddLinearForeshortened](../GeneralDimensions/GeneralDimensions_AddLinearForeshortened.md) | Creates a linear foreshortened dimension on the drawing sheet. |
| [AddRadius](../GeneralDimensions/GeneralDimensions_AddRadius.md) | Method that creates a radius dimension. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GeneralDimensions/GeneralDimensions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../GeneralDimensions/GeneralDimensions_Count.md) | Property that returns the number of items in the collection. |
| [Item](../GeneralDimensions/GeneralDimensions_Item.md) | Method that returns the specified dimension object from the collection. |
| [Type](../GeneralDimensions/GeneralDimensions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingDimensions.GeneralDimensions](../DrawingDimensions/DrawingDimensions_GeneralDimensions.md)

## Version

Introduced in version 9
