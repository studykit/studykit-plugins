# ParameterTable Object

## Description

The ParameterTable object represents the connection to a spreadsheet. From the ParameterTable object you can access the spreadsheet and the properties that define how the spreadsheet is read. In addition, the ParameterTable object provides access to the parameters that were created as a result of reading in the spreadsheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ParameterTable/ParameterTable_Delete.md) | Method that deletes the ParameterTable object. |
| [Export](../ParameterTable/ParameterTable_Export.md) | Exports the ParameterTable to an external file. |
| [GetReferenceKey](../ParameterTable/ParameterTable_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AttributeSets](../ParameterTable/ParameterTable_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [FileName](../ParameterTable/ParameterTable_FileName.md) | Gets/Sets the File Name of this linked table. Fails if this table is embedded. Setting a new File Name may add new parameters, update existing ones, and may turn some to DriverLost. |
| [Linked](../ParameterTable/ParameterTable_Linked.md) | Property that specifies if the Excel document is linked or embedded to the Autodesk Inventor document. |
| [Parent](../ParameterTable/ParameterTable_Parent.md) | Property that returns the parent object of this ParameterTable. This property will return different types of objects depending on the document type the ParameterTable is contained in. If the ParameterTable is in a part document then the parent is a PartComponentDefinition object. If the ParameterTable is in an assembly document then the parent is an AssemblyComponentDefinition. If the document is a drawing document then the parent is a DraftDocument. |
| [ReferencedFileDescriptor](../ParameterTable/ParameterTable_ReferencedFileDescriptor.md) | Gets the description of the linked file. |
| [StartCell](../ParameterTable/ParameterTable_StartCell.md) | Gets the starting cell in the WorkSheet from which the table is derived. |
| [TableParameters](../ParameterTable/ParameterTable_TableParameters.md) | Property that returns the TableParameters collection object. |
| [Type](../ParameterTable/ParameterTable_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WorkSheet](../ParameterTable/ParameterTable_WorkSheet.md) | Property that returns the Excel WorkSheet object. Using the Excel Automation interface you can query and modify the contents of the sheet. |

## Accessed From

[ParameterTables.AddExcelTable](../ParameterTables/ParameterTables_AddExcelTable.md), [ParameterTables.Item](../ParameterTables/ParameterTables_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Table Parameters](../../sample-programs/ParameterTables_Sample.md) | This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet. |

## Version

Introduced in version 4
