# GraphicsDataSets.CreateImageSet Method

Parent Object: [GraphicsDataSets](../GraphicsDataSets/GraphicsDataSets.md)

## Description

Method that creates a new GraphicsImageSet object. You use methods provided by the GraphicsImageSet object to define the images.

## Remarks

This method will fail in the case where the GraphicDataSets object can be saved with the document. This occurs when the GraphicDataSets object was created using the Add2 method and the SaveWithDocument argument was True.

## Syntax

GraphicsDataSets.**CreateImageSet**( ***DataSetId*** As Long ) As [GraphicsImageSet](../GraphicsImageSet/GraphicsImageSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DataSetId | Long | Specifies the unique identifier for the GraphicsImageSet object. This must be unique with respect to all other GraphicsDataSet objects within this GraphicDataSets collection object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |

## Version

Introduced in version 2011
