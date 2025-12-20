# PropertySet Object

## Description

Object that represents a PropertySet. This is a collection of related Properties. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../PropertySet/PropertySet_Add.md) | Adds a new Property to this PropertySet. |
| [Delete](../PropertySet/PropertySet_Delete.md) | Method that deletes this PropertySet. |
| [GetPropertyInfo](../PropertySet/PropertySet_GetPropertyInfo.md) | Method that returns property info in the PropertySet. |
| [SetPropertyValues](../PropertySet/PropertySet_SetPropertyValues.md) | Method that batch sets property values in the PropertySet. If a specified name is not existent in the property set a new property with the specified name will be created. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../PropertySet/PropertySet_Count.md) | Property that returns the number of items in this collection. |
| [Dirty](../PropertySet/PropertySet_Dirty.md) | Property that returns a Boolean flag that indicates whether any of the Properties have been edited, deleted or created. |
| [DisplayName](../PropertySet/PropertySet_DisplayName.md) | Gets/Sets the human-readable name associated with this Property Set. |
| [InternalName](../PropertySet/PropertySet_InternalName.md) | Gets the unambiguous, internal name (FMTID) associated with this PropertySet. |
| [Item](../PropertySet/PropertySet_Item.md) | Gets the Property given either its name or its sequential index. |
| [ItemByPropId](../PropertySet/PropertySet_ItemByPropId.md) | Gets the Property in this set by its PropId. |
| [Name](../PropertySet/PropertySet_Name.md) | Gets the name of this PropertySet. |
| [Parent](../PropertySet/PropertySet_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Type](../PropertySet/PropertySet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Property.Parent](../Property/Property_Parent.md), [PropertySets.Add](../PropertySets/PropertySets_Add.md), [PropertySets.Item](../PropertySets/PropertySets_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |
| [Update iProperty values using Apprentice](../../sample-programs/iPropertyApprentice_Sample.md) | Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist. |
| [Create custom iProperties](../../sample-programs/iPropertyCreateCustom_Sample.md) | Creates custom iProperties of various types. A document must be open when this sample is run. |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Get value of iProperty](../../sample-programs/iPropertyGetValue_Sample.md) | Demonstrates getting the values of the "Part Number" iProperty. Any property can be retrieved by accesing the correct property set and property.  A document must be open when this sample is run. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |