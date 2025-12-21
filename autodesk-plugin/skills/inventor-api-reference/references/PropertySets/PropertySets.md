# PropertySets Object

## Description

Object that manages the collection of objects and provides the ability to add new property sets to the collection. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../PropertySets/PropertySets_Add.md) | Adds a new PropertySet. The new set's FMTID can be optionally provided (as a string). |
| [FlushToFile](../PropertySets/PropertySets_FlushToFile.md) | Flush all of the Properties in each of the PropertySets onto the file. The 'dirty' flags are reset. Please note that this method is available in Apprentice only. |
| [PropertySetExists](../PropertySets/PropertySets_PropertySetExists.md) | Function that returns a Boolean to indicate whether a PropertySet with the specified name exists in the PropertySets collection. |
| [RefreshFromFile](../PropertySets/PropertySets_RefreshFromFile.md) | Refresh all of the Properties in each of the PropertySets from the File. The 'dirty' flags are reset and any edits are lost. Please note that this method is available in Apprentice only. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../PropertySets/PropertySets_Count.md) | Property that returns the number of items in this collection. |
| [Dirty](../PropertySets/PropertySets_Dirty.md) | Property that returns a Boolean flag that indicates whether any of the Properties have been edited, deleted or created. |
| [Item](../PropertySets/PropertySets_Item.md) | Gets the set in this collection in a sequences fashion; by index, or by its name -- Display or Internal. |
| [Parent](../PropertySets/PropertySets_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../PropertySets/PropertySets_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDocument.FilePropertySets](../ApprenticeServerDocument/ApprenticeServerDocument_FilePropertySets.md), [ApprenticeServerDocument.PropertySets](../ApprenticeServerDocument/ApprenticeServerDocument_PropertySets.md), [ApprenticeServerDrawingDocument.FilePropertySets](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_FilePropertySets.md), [ApprenticeServerDrawingDocument.PropertySets](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_PropertySets.md), [AssemblyDocument.FilePropertySets](../AssemblyDocument/AssemblyDocument_FilePropertySets.md), [AssemblyDocument.PropertySets](../AssemblyDocument/AssemblyDocument_PropertySets.md), [BOMRow.OccurrencePropertySets](../BOMRow/BOMRow_OccurrencePropertySets.md), [ComponentOccurrence.OccurrencePropertySets](../ComponentOccurrence/ComponentOccurrence_OccurrencePropertySets.md), [ComponentOccurrenceProxy.OccurrencePropertySets](../ComponentOccurrenceProxy/ComponentOccurrenceProxy_OccurrencePropertySets.md), [Document.FilePropertySets](../Document/Document_FilePropertySets.md), [Document.PropertySets](../Document/Document_PropertySets.md), [DrawingDocument.FilePropertySets](../DrawingDocument/DrawingDocument_FilePropertySets.md), [DrawingDocument.PropertySets](../DrawingDocument/DrawingDocument_PropertySets.md), [PartDocument.FilePropertySets](../PartDocument/PartDocument_FilePropertySets.md), [PartDocument.PropertySets](../PartDocument/PartDocument_PropertySets.md), [PresentationDocument.FilePropertySets](../PresentationDocument/PresentationDocument_FilePropertySets.md), [PresentationDocument.PropertySets](../PresentationDocument/PresentationDocument_PropertySets.md), [PropertySet.Parent](../PropertySet/PropertySet_Parent.md), [VirtualComponentDefinition.PropertySets](../VirtualComponentDefinition/VirtualComponentDefinition_PropertySets.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |
| [Update iProperty values using Apprentice](../../sample-programs/iPropertyApprentice_Sample.md) | Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist. |
| [Create custom iProperties](../../sample-programs/iPropertyCreateCustom_Sample.md) | Creates custom iProperties of various types. A document must be open when this sample is run. |
| [Get value of iProperty](../../sample-programs/iPropertyGetValue_Sample.md) | Demonstrates getting the values of the "Part Number" iProperty. Any property can be retrieved by accesing the correct property set and property.  A document must be open when this sample is run. |

## Version

Introduced in version 4
