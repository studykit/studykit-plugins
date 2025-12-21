# DrawingBOMColumn Object

## Description

The DrawingBOMColumn object represents a column within the drawing BOM.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetFilePropertyId](../DrawingBOMColumn/DrawingBOMColumn_GetFilePropertyId.md) | Method that returns the id of the property associated with the column. This method will return an error if the PropertyType property does not return a value of kFilePropertyType. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingBOMColumn/DrawingBOMColumn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CustomPropertyName](../DrawingBOMColumn/DrawingBOMColumn_CustomPropertyName.md) | Property that returns the name of the custom property associated with this column. |
| [Parent](../DrawingBOMColumn/DrawingBOMColumn_Parent.md) | Property that returns the parent DrawingBOM object. |
| [PropertyType](../DrawingBOMColumn/DrawingBOMColumn_PropertyType.md) | Property that returns the property type associated with this column. |
| [Title](../DrawingBOMColumn/DrawingBOMColumn_Title.md) | Property that returns the title of the column. |
| [Type](../DrawingBOMColumn/DrawingBOMColumn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingBOMColumns.Item](../DrawingBOMColumns/DrawingBOMColumns_Item.md)

## Version

Introduced in version 2009
