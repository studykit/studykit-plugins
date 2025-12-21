# BOMRow Object

## Description

The BOMRow object represents an item in the BOM based on the parent BOMView.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetReferenceKey](../BOMRow/BOMRow_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BOMRow/BOMRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BOMRow/BOMRow_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BOMStructure](../BOMRow/BOMRow_BOMStructure.md) | Gets and sets how the BOM item represented by this row is used/viewed relating to design. |
| [ChildRows](../BOMRow/BOMRow_ChildRows.md) | Property that gets the BOMRowsEnumerator object containing the locally-stored rows under this BOMRow. This property will return Nothing for BOMRows in a parts-only view and if there are no sub-rows for this BOMRow. |
| [ComponentDefinitions](../BOMRow/BOMRow_ComponentDefinitions.md) | Property that returns the ComponentDefinitions associated with this row in the BOM. These could be part, sheet metal, assembly, weldment or a virtual component definitions. This enumerator will return just one component definition unless this row is a merged one, in which case all associated component definitions are returned. The first component definition in the enumerator is always the primary component definition. |
| [ComponentOccurrences](../BOMRow/BOMRow_ComponentOccurrences.md) | Gets the ComponentOccurrences associated with this row in the BOM. |
| [ItemNumber](../BOMRow/BOMRow_ItemNumber.md) | Gets and sets the item number of the BOM item. |
| [ItemNumberLocked](../BOMRow/BOMRow_ItemNumberLocked.md) | Gets and sets whether the item identifier can be edited. |
| [ItemQuantity](../BOMRow/BOMRow_ItemQuantity.md) | Property that gets the number of instances not marked as phantom or reference represented by this BOM row. |
| [Merged](../BOMRow/BOMRow_Merged.md) | Property that returns whether this row is a result of a merging multiple rows. If true, the ComponentDefinitions property returns all the associated component definitions. This property will return False for all rows in the data BOMView. |
| [OccurrencePropertySets](../BOMRow/BOMRow_OccurrencePropertySets.md) | Read-only property that returns a PropertySets object associated with this BOMRow. This only applies to non merged component rows with Instance Properties. |
| [Parent](../BOMRow/BOMRow_Parent.md) | Property that returns the parent BOMView or the BOMRow object. |
| [Promoted](../BOMRow/BOMRow_Promoted.md) | Property that returns whether this row was promoted (for instance, as a result of the parent subassembly being marked phantom). This property will return False for all rows in the data BOMView. |
| [ReferencedFileDescriptor](../BOMRow/BOMRow_ReferencedFileDescriptor.md) | Gets the FileDescriptor for the component referenced by this row. This only applies to non merged component rows and non local components and immediately referenced components. Therefore this would only be useful in the data view. |
| [RolledUp](../BOMRow/BOMRow_RolledUp.md) | Indicates whether this row is a result of rolling up multiple promoted rows of the same ComponentDefinition. |
| [TotalQuantity](../BOMRow/BOMRow_TotalQuantity.md) | Gets and sets the total quantity of the BOM item. Overrides cannot be set for parts only views. |
| [TotalQuantityOverridden](../BOMRow/BOMRow_TotalQuantityOverridden.md) | Gets and sets whether the TotalQuantity property has been overridden. This property can only be set to False, in which case the override on the value will be removed. |
| [Type](../BOMRow/BOMRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BOMRowsEnumerator.Item](../BOMRowsEnumerator/BOMRowsEnumerator_Item.md), [DrawingBOMRow.BOMRow](../DrawingBOMRow/DrawingBOMRow_BOMRow.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |

## Version

Introduced in version 10
