# iPartTableColumn Object

## Description

The iPartTableColumn object represents a column in the iPart factory table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../iPartTableColumn/iPartTableColumn_Delete.md) | Method that deletes this column in the factory. The "Member" and "Part Number" columns cannot be deleted. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iPartTableColumn/iPartTableColumn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../iPartTableColumn/iPartTableColumn_Count.md) | Property that returns the number of items in this collection. |
| [CustomColumn](../iPartTableColumn/iPartTableColumn_CustomColumn.md) | Gets and sets whether this is a custom parameter column. |
| [CustomIncrement](../iPartTableColumn/iPartTableColumn_CustomIncrement.md) | Gets and sets the increment value for custom parameter columns. |
| [CustomRangeMaximum](../iPartTableColumn/iPartTableColumn_CustomRangeMaximum.md) | Gets and sets the maximum value for a custom parameter. |
| [CustomRangeMinimum](../iPartTableColumn/iPartTableColumn_CustomRangeMinimum.md) | Gets and sets the minimum value for a custom parameter. |
| [DisplayHeading](../iPartTableColumn/iPartTableColumn_DisplayHeading.md) | Property that returns the localized heading of the column. |
| [FormattedHeading](../iPartTableColumn/iPartTableColumn_FormattedHeading.md) | Property that returns the heading of the column in XML format. |
| [Heading](../iPartTableColumn/iPartTableColumn_Heading.md) | Property that returns the heading of the column. |
| [Index](../iPartTableColumn/iPartTableColumn_Index.md) | Property that returns the index of this column within the iPart factory table. |
| [Item](../iPartTableColumn/iPartTableColumn_Item.md) | Returns the specified iPartTableCell object from the collection. This is the default property of the iPartTableColumn object. |
| [Key](../iPartTableColumn/iPartTableColumn_Key.md) | Gets and sets the key order for the column. |
| [Parent](../iPartTableColumn/iPartTableColumn_Parent.md) | Property that returns the parent iPartFactory object. |
| [ReferencedDataType](../iPartTableColumn/iPartTableColumn_ReferencedDataType.md) | Property that returns the data type contained in the column. |
| [ReferencedObject](../iPartTableColumn/iPartTableColumn_ReferencedObject.md) | Property that returns the object referenced by the column. For instance, if the column references a fillet feature suppression, the corresponding FilletFeature object is returned. Similarly, if a file property is referenced, the corresponding Property object is returned. |
| [Type](../iPartTableColumn/iPartTableColumn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iPartFactory.DisplayStyleColumn](../iPartFactory/iPartFactory_DisplayStyleColumn.md), [iPartFactory.FileNameColumn](../iPartFactory/iPartFactory_FileNameColumn.md), [iPartFactory.MaterialColumn](../iPartFactory/iPartFactory_MaterialColumn.md), [iPartTableColumns.Item](../iPartTableColumns/iPartTableColumns_Item.md)

## Version

Introduced in version 6
