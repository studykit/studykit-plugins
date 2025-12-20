# GraphicsDataSets.CreateTextureCoordinateSet Method

Parent Object: [GraphicsDataSets](../GraphicsDataSets/GraphicsDataSets.md)

## Description

Method that creates a new GraphicsTextureCoordinateSet object. You use methods provided by the GraphicsTextureCoordinateSet object to define the coordinates.

## Syntax

GraphicsDataSets.**CreateTextureCoordinateSet**( ***DataSetId*** As Long ) As [GraphicsTextureCoordinateSet](../GraphicsTextureCoordinateSet/GraphicsTextureCoordinateSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DataSetId | Long | Specifies the unique identifier for the GraphicsTextureCoordinateSet object. This must be unique with respect to all other GraphicsDataSet objects within this GraphicDataSets collection object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |