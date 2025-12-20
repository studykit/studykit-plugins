# ContentTableColumns Object

## Description

The ContentTableColumns object is a collection that provides access to the columns of the table associated with a particular content center family.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ContentTableColumns/ContentTableColumns_Add.md) | Method that creates a new column. Any changes to the table are not actually applied until the Save method of the parent ContentFamily object is called. |
| [CreateExpressionLimits](../ContentTableColumns/ContentTableColumns_CreateExpressionLimits.md) | Method that creates an ExpressionLimits object. This object can be used to define the limits of a custom expression associated with a table column. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ContentTableColumns/ContentTableColumns_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ContentTableColumns/ContentTableColumns_Count.md) | Property that returns the number of ContentTableColumn objects in the collection. |
| [Item](../ContentTableColumns/ContentTableColumns_Item.md) | Returns the specified ContentTableColumn object from the collection. |
| [Type](../ContentTableColumns/ContentTableColumns_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ContentFamily.TableColumns](../ContentFamily/ContentFamily_TableColumns.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |