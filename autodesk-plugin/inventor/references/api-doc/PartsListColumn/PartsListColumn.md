# PartsListColumn Object

## Description

The PartsListColumn object represents a column in a parts list table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetFilePropertyId](../PartsListColumn/PartsListColumn_GetFilePropertyId.md) | Method that returns the id of the property associated with the column. This method will return an error if the PropertyType property does not return a value of kFilePropertyType. |
| [Remove](../PartsListColumn/PartsListColumn_Remove.md) | Method that removes this column from the parts list. |
| [Reposition](../PartsListColumn/PartsListColumn_Reposition.md) | Method that repositions the column within the parts list. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PartsListColumn/PartsListColumn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CustomPropertyName](../PartsListColumn/PartsListColumn_CustomPropertyName.md) | Property that returns the name of the custom property associated with this object. This method will return an error if the PropertyType property does not return a value of kCustomPropertyType. |
| [Parent](../PartsListColumn/PartsListColumn_Parent.md) | Property that gets the parent object from whom this object can logically be reached. |
| [PropertyType](../PartsListColumn/PartsListColumn_PropertyType.md) | Property that returns the property type associated with this column. If this property returns kFilePropertyType, the GetFilePropertyId method returns the identity of the file property. If this property returns kCustomPropertyType, use the CustomPropertyName property to get the name of the custom property. |
| [Title](../PartsListColumn/PartsListColumn_Title.md) | Gets and sets the title of the column header in the parts list table. |
| [TitleHorizontalJustification](../PartsListColumn/PartsListColumn_TitleHorizontalJustification.md) | Gets and sets the justification of the column title. |
| [Type](../PartsListColumn/PartsListColumn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [ValueHorizontalJustification](../PartsListColumn/PartsListColumn_ValueHorizontalJustification.md) | Gets and sets the justification of the values in the column. |
| [Width](../PartsListColumn/PartsListColumn_Width.md) | Gets and sets the width of the column. |

## Accessed From

[PartsListColumns.Add](../PartsListColumns/PartsListColumns_Add.md), [PartsListColumns.Item](../PartsListColumns/PartsListColumns_Item.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |