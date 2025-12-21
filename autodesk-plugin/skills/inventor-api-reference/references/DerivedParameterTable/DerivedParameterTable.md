# DerivedParameterTable Object

## Description

The DerivedParameterTable object represents the connection to an Inventor document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DerivedParameterTable/DerivedParameterTable_Delete.md) | Method that deletes the DerivedParameterTable object. This method will fail if the HasReferenceComponent property returns true. |
| [GetReferenceKey](../DerivedParameterTable/DerivedParameterTable_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AttributeSets](../DerivedParameterTable/DerivedParameterTable_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DerivedParameters](../DerivedParameterTable/DerivedParameterTable_DerivedParameters.md) | Property that returns the DerivedParameters collection object. |
| [HasReferenceComponent](../DerivedParameterTable/DerivedParameterTable_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [LinkedParameters](../DerivedParameterTable/DerivedParameterTable_LinkedParameters.md) | Gets and sets the collection of parameters that have been linked from the referenced document. |
| [Parent](../DerivedParameterTable/DerivedParameterTable_Parent.md) | Property that returns the parent object of this DerivedParameterTable. This property will return different types of objects depending on the document type the DerivedParameterTable is contained in. If the DerivedParameterTable is in a part document then the parent is a PartComponentDefinition object. If the DerivedParameterTable is in an assembly document then the parent is an AssemblyComponentDefinition. |
| [ReferenceComponent](../DerivedParameterTable/DerivedParameterTable_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedDocumentDescriptor](../DerivedParameterTable/DerivedParameterTable_ReferencedDocumentDescriptor.md) | Property that returns the referenced Inventor document. |
| [Type](../DerivedParameterTable/DerivedParameterTable_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedParameterTables.Add](../DerivedParameterTables/DerivedParameterTables_Add.md), [DerivedParameterTables.Add2](../DerivedParameterTables/DerivedParameterTables_Add2.md), [DerivedParameterTables.Item](../DerivedParameterTables/DerivedParameterTables_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |

## Version

Introduced in version 11
