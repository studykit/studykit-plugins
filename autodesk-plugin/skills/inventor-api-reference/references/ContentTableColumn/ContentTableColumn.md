# ContentTableColumn Object

## Description

The ContentTableColumn object represents the column of the table associated with a particular content center family.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ClearPropertyMap](../ContentTableColumn/ContentTableColumn_ClearPropertyMap.md) | Method that removes any property mapping for this column. |
| [GetPropertyMap](../ContentTableColumn/ContentTableColumn_GetPropertyMap.md) | Method that gets the information associated with a custom expression. This method is only valid when the HasPropertyMap property returns True. |
| [SetPropertyMap](../ContentTableColumn/ContentTableColumn_SetPropertyMap.md) | Method that sets the information associated with a custom expression. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ContentTableColumn/ContentTableColumn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DataType](../ContentTableColumn/ContentTableColumn_DataType.md) | Property that indicates the type of value defined for this column. Values this property can return are kIntegerType, kDoubleType, kStringType, and kBooleanType. |
| [DisplayHeading](../ContentTableColumn/ContentTableColumn_DisplayHeading.md) | Gets/Sets the display name of this column. |
| [Expression](../ContentTableColumn/ContentTableColumn_Expression.md) | Gets/Sets the expression to use to automatically populate the rows of this column. |
| [HasPropertyMap](../ContentTableColumn/ContentTableColumn_HasPropertyMap.md) | Property that indicates if this column is mapped to an iProperty. |
| [InternalName](../ContentTableColumn/ContentTableColumn_InternalName.md) | Property that gets and sets the name of this column. |
| [IsCustom](../ContentTableColumn/ContentTableColumn_IsCustom.md) | Read-only property that returns True if the column is a custom column. |
| [KeyColumnOrder](../ContentTableColumn/ContentTableColumn_KeyColumnOrder.md) | Read-write Property that allows you to get and set the KeyWeight of the column. |
| [Parent](../ContentTableColumn/ContentTableColumn_Parent.md) | Property that returns the ContentFamily object this column is associated with. |
| [Type](../ContentTableColumn/ContentTableColumn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Units](../ContentTableColumn/ContentTableColumn_Units.md) | Read-write Property that allows you to get and set the units of the column. |

## Accessed From

[ContentFamily.DesignationColumn](../ContentFamily/ContentFamily_DesignationColumn.md), [ContentFamily.FileNameColumn](../ContentFamily/ContentFamily_FileNameColumn.md), [ContentTableColumns.Add](../ContentTableColumns/ContentTableColumns_Add.md), [ContentTableColumns.Item](../ContentTableColumns/ContentTableColumns_Item.md)

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |