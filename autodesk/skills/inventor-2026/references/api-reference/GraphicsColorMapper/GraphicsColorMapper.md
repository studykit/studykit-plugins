# GraphicsColorMapper Object

## Description

The GraphicsColorMapper object maps scalar values to colors. Use methods provided on the object to define the scalar values and colors. The same object can be used to define the mapping for multiple graphics primitives using the ColorMapper property on the primitives.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../GraphicsColorMapper/GraphicsColorMapper_Delete.md) | Method that deletes the GraphicsColorMapper object. |
| [GetColors](../GraphicsColorMapper/GraphicsColorMapper_GetColors.md) | Method that gets all of the colors in the map. |
| [GetValues](../GraphicsColorMapper/GraphicsColorMapper_GetValues.md) | Method that gets all of the values in the map. |
| [PutColors](../GraphicsColorMapper/GraphicsColorMapper_PutColors.md) | Method that sets all of the colors in the map. This will replace all existing colors currently defined for the map. |
| [PutValues](../GraphicsColorMapper/GraphicsColorMapper_PutValues.md) | Method that sets all of the values in the map. This will replace all existing values currently defined for the map. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Color](../GraphicsColorMapper/GraphicsColorMapper_Color.md) | Read-write property that gets and sets the color at a given index in the set. |
| [ColorCount](../GraphicsColorMapper/GraphicsColorMapper_ColorCount.md) | Property that returns the number of colors defined within the set. |
| [MappedColor](../GraphicsColorMapper/GraphicsColorMapper_MappedColor.md) | Property that returns the color at a given value in the map. This property is informational only and need not be used when assigning a color map to a primitive. |
| [Type](../GraphicsColorMapper/GraphicsColorMapper_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../GraphicsColorMapper/GraphicsColorMapper_Value.md) | Read-write property that gets and sets the value at a given index in the set. |
| [ValueCount](../GraphicsColorMapper/GraphicsColorMapper_ValueCount.md) | Property that returns the number of values defined within the set. |

## Accessed From

[GraphicsDataSets.CreateColorMapper](../GraphicsDataSets/GraphicsDataSets_CreateColorMapper.md), [TriangleFanGraphics.ColorMapper](../TriangleFanGraphics/TriangleFanGraphics_ColorMapper.md), [TriangleGraphics.ColorMapper](../TriangleGraphics/TriangleGraphics_ColorMapper.md), [TriangleStripGraphics.ColorMapper](../TriangleStripGraphics/TriangleStripGraphics_ColorMapper.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |

## Version

Introduced in version 2010
